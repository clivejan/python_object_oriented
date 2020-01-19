"""
operatoe.itemgetter can be used as a key of sort() when sorting a list
"""

from operator import itemgetter

lst = [('h', 4),
	   ('n', 6),
	   ('o', 5),
	   ('p', 1),
	   ('t', 3),
	   ('y', 2)]

lst.sort(key=itemgetter(1))
print(lst)
