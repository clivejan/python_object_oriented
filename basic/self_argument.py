# Define a class
class Point:
	
	def reset(self):
		"""
		The self augument to a method is a refernce to the object that
		the method is being invoke on.

		setting x, y coordinates to zero
		"""
		self.x = 0
		self.y = 0

# Instantiate objects from the defined class
p1 = Point()
p2 = Point()

# Python will make the p1 as an argument
p1.reset()

# invoking the fuction on the class and passing object as the self argument
Point.reset(p2)

# verify the method has executed successfully
print(p1.x, p1.y)
print(p2.x, p2.y)
