random_keys = {}
random_keys['asting'] = 'somestring'
random_keys[5] = 'aninteger'
random_keys[25.2] = 'floats work too'
random_keys[('abc', 123)] = 'so do tuples'

class AnObject:
	def __init__(self, avalue):
		self.avalue = avalue

my_object = AnObject(14)
random_keys[my_object] = 'We can even use object as a key'
my_object.avalue = 12

try:
	random_keys[[1, 2, 3]] = 'List cannnot be a dict key'
except:
	print('List is mutable type')

for key, value in random_keys.items():
	print(f"{key} has {value}")
