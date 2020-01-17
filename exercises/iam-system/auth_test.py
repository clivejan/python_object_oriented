import auth

# Add a new user
auth.authenticator.add_user('clive', '1234567890')

# Add a new permission
auth.authorizor.add_permission("paint")

# check user has 'paint' permission
try:
	auth.authorizor.check_permission('paint', 'clive')
except auth.NotLoggedInError as e:
	print(f"NotLoggedInError: {e}")

# make user log in
auth.authenticator.login('clive', '1234567890')

# check user has 'paint' permission again
try:
	auth.authorizor.check_permission('paint', 'clive')
except auth.NotPermittedError as e:
	print(f"NotPermittedError: {e}")

# check user has 'mix' permission
try:
	auth.authorizor.check_permission('mix', 'clive')
except auth.PermissionError as e:
	print(f"PermissionError: {e}")

# add permission to user
auth.authorizor.permit_user('paint', 'clive')

# check user has 'paint' permission again
print(auth.authorizor.check_permission('paint', 'clive'))
