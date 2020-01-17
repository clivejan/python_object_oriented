def no_return():
	print("I am about to raise an exception")
	raise Exception("This is always raised")
	print("This line will never executed")
	return "I won't be returned"

#no_return()

def call_exceptor():
	print("call_exception starts here...")
	no_return()
	print("an exception was raised...")
	print("...so these lines don't run")

call_exceptor()
