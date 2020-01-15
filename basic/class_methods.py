# Define a class
class Point:
	
	def reset(self):
		"""setting x, y coordinates to zero"""
		self.x = 0
		self.y = 0

# Instantiate a object from the defined class
p = Point()

# calling method on the object
p.reset()

# verify the method has executed successfully
print(p.x, p.y)
