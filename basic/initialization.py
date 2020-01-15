class Point:

	def __init__(self, x=0, y=0):
		"""using initializer to initialize object's attributes"""
		self.move(x, y)

	def move(self, x, y):
		"""setting x, y coordinates by arguments"""
		self.x = x
		self.y = y

	def reset(self):
		"""setting x, y coordinates to zero"""
		self.move(0, 0)

# constructing a Point
point = Point(3, 5)
print(point.x, point.y)
