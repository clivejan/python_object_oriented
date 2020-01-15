import math

class Point:

	def move(self, x, y):
		"""setting x, y coordinates by arguments"""
		self.x = x
		self.y = y

	def reset(self):
		"""setting x, y coordinates to zero"""
		self.move(0, 0)

	def calculate_distance(self, other_point):
		"""retrun the distance to other point object"""
		distance = math.sqrt((self.x - other_point.x) ** 2 +
				 (self.y - other_point.y) ** 2) 
		return distance

# Instantiate objects from the defined class
point1 = Point()
point2 = Point()

# initialize the objects coordinates
point1.reset()
point2.move(5, 0)

# calculate the distance between two Point objects
print(point2.calculate_distance(point1))

# ensure the distance is the same regarless of the calling order
assert point2.calculate_distance(point1) == point1.calculate_distance(point2)

# play around
point1.move(3, 4)
print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1))
