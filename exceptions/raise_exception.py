class EvenOnly(list):

	def append(self, integer):
		"""overwritten built-in list method to extend desired functionality"""
		if not isinstance(integer, int):
			raise TypeError("Only integers can be added.")
		if integer % 2:
			raise ValueError("Only envn numbers can be added.")

		# using normal list append method
		super().append(integer)

e = EvenOnly()

# this will raise an TypeError exception
#e.append('a string')

# this will raise an ValueError exception
e.append(3)

e.append(2)
