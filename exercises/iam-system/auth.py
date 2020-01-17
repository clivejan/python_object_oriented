import hashlib

# define customer exceptions
class AuthException(Exception):

	def __init__(self, username, user=None):
		super().__init__(username, user)
		self.username = username
		self.user = user

class UsernameAlreadyExists(AuthException):
	pass

class PasswordTooShort(AuthException):
	pass

class InvalidUsername(AuthException):
	pass

class InvalidPassword(AuthException):
	pass

class NotLoggedInError(AuthException):
	pass

class NotPermittedError(AuthException):
	pass

class PermissionError(Exception):
	pass


class User:

	def __init__(self, username, password):
		"""
		Create a new user object. The password
		will be ecvrypted before storing.
		"""
		self.username = username
		self.password = self.__encrypt_pw(password)
		self.is_logged_in = False

	def __encrypt_pw(self, password):
		"""
		Encrypt the password with the username and return
		the sha digest.
		"""
		hash_string = self.username + password
		hash_string = hash_string.encode("utf8")
		hash_string = hashlib.sha256(hash_string).hexdigest()
		return hash_string

	def check_password(self, password):
		"""
		Return True if the password is valid for this
		user, False otherwise.
		"""
		encrypted = self.__encrypt_pw(password)
		return encrypted == self.password

class Authenticator:
	"""
	Construct an authenticator to manage
	users loggin in and out.
	"""

	def __init__(self):
		self.users = {}

	def add_user(self, username, password):
		if username in self.users:
			raise UsernameAlreadyExists(username)
		if len(password) < 6:
			raise PasswordTooShort(username)
		self.users[username] = User(username, password)

	def login(self, username, password):
		
		try:
			user = self.users[username]
		except KeyError:
			# handle the KeyError to our own InvalidUsername exception
			raise InvalidUsername(username)

		if not user.check_password(password):
			raise InvalidPassword(username, user)

		user.is_logged_in = True
		return True

	def is_logged_in(self, username):

		if username in self.users:
			return self.users[username].is_logged_in
		return False

# create a module-level Authenticator instance
authenticator = Authenticator()

class Authorizor():

	def __init__(self,authenticator):
		self.authenticator = authenticator
		self.permissions = {}

	def add_permission(self, perm_name):
		"""
		Create a new permission that users
		can be added to.
		"""
		try:
			perm_set = self.permissions[perm_name]
		except KeyError:
			# handle KeyError to create a new key-pair
			self.permissions[perm_name] = set()
		else:
			raise PermissionError("Permission Exists")

	def permit_user(self, perm_name, username):
		"""
		Grant the given permission to the user
		"""
		try:
			perm_set = self.permissions[perm_name]
		except KeyError:
			raise PermissionError("Permission does not exist")
		else:
			if username not in self.authenticator.users:
				raise InvalidUsername(username)
			perm_set.add(username)

	def check_permission(self, perm_name, username):
		"""
		Check whether a user has a specific permission or not
		"""
		if not self.authenticator.is_logged_in(username):
			raise NotLoggedInError(username)

		try:
			perm_set = self.permissions[perm_name]
		except KeyError:
			raise PermissionError("Permission does not exist")
		else:
			if username not in perm_set:
				raise NotPermittedError(username)
			else:
				return True

# create a module-level Authorizor instance
authorizor = Authorizor(authenticator)
