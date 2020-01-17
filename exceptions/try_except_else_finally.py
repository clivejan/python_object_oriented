import random

some_exceptons = [ValueError, TypeError, IndexError, None]

try:
	choice = random.choice(some_exceptons)
	print(f"raising {choice}")
	if choice:
		raise choice("An error")
except ValueError:
	print("Caught a ValueError")
except TypeError:
	print("Caught a TypeError")
except IndexError:
	print("Caught a IndexError")
else:
	print("This code called if there is no exception")
finally:
	print("This cleanup code is always called")
