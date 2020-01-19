class WeirdSortee:

	def __init__(self, string, number, sort_num):
		self.string = string
		self.number = number
		self.sort_num = sort_num

	def __lt__(self, object):
		# list.sort() woll use this method
		if self.sort_num:
			return self.number < object.number
		return self.string < object.string

	def __repr__(self):
		# using to print()
		return f"{self.string}:{self.number}"

a = WeirdSortee('a', 4, True) 
b = WeirdSortee('b', 3, True) 
c = WeirdSortee('c', 2, True) 
d = WeirdSortee('d', 1, True) 

# a list of objects
lst = [a, b, c, d]

# sort by object.number attribute
lst.sort()
print(lst)

# sort by object.string attribute
for item in lst:
	item.sort_num = False
lst.sort()
print(lst)
