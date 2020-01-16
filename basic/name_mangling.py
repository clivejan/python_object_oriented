class SecertString:
	"""A not-at-all secure way to store a secret string."""

	def __init__(self, plain_string, pass_phrase):
		# using double undersocres to strong indicate privete resources
		self.__plain_string = plain_string
		self.__pass_phrase = pass_phrase

	def decrypt(self, pass_phrase):
		"""Only show the string if the pass_phrase is corrent."""
		if pass_phrase == self.__pass_phrase:
			return self.__plain_string
		else:
			return ""

# following the indicator to using the class
secret_string = SecertString('my_passwd', 'encrypted')
print(secret_string.decrypt('encrypted'))

# try to access privete resources in the class
#print(secret_string.__plain_string)
print(secret_string._SecertString__plain_string)
