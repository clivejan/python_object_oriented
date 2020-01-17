import time

# define a decorator to add more actions on oraginal function
def log_calls(func):

	def wrapper(*args, **kwargs):
		now = time.time()
		print(f"Calling {func.__name__} with {args} and {kwargs}")
		return_value = func(*args, **kwargs)
		print(f"Executed {func.__name__} in {time.time() - now}ms")
		return return_value

	return wrapper

def test1(a, b, c):
	print("\ttest1 called")

def test2(a, b):
	print("\ttest2 called")

def test3(a, b):
	print("\ttest3 called")
	time.sleep(1)

# pass function to decorator and replace original one
test1 = log_calls(test1)
test2 = log_calls(test2)
test3 = log_calls(test3)

test1(1, 2, 3)
test2(4, b=5)
test3(6, 7)