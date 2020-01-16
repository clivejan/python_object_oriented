from collections.abc import Container

# minic the required method for chkeching whether a number is in an odd list
class OddContainer:

	def __contains__(self, x):
		if not isinstance(x, int) or not x % 2 == 0:
			return False
		return True

# whether OddContainer class become subclass of Container automatically
print(issubclass(OddContainer, Container))

# whether the a object of OddContainer is a Container type object
odd_container = OddContainer()
print(isinstance(odd_container, Container))

# OddContainer object can use Container methods for free
print(1 in odd_container)
print(2 in odd_container)
print('two' in odd_container)
