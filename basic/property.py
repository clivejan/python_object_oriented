class Color_direct:

	def __init__(self, rgb_value, name):
		self.rgb_value = rgb_value
		self.name = name


class Color_property:

	def __init__(self, rgb_value, name):
		self.rgb_value = rgb_value
		self._name = name

	def _set_name(self, name):
		if not name:
			raise Exception("Invalid name")
		self._name = name

	def _get_name(self):
		return self._name

	name = property(_get_name, _set_name)

# using direct access version
c1 = Color_direct("#ff0000", "bright red")
print(c1.name)
c1.name = "red"
print(c1.name)
c1.name = ""
print(c1.name)

# using property access version
c2 = Color_property("#ff0000", "bright red")
print(c2.name)
c2.name = "red"
print(c2.name)
c2.name = ""
print(c2.name)