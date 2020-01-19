"""
sort() accept a function to tanslate each object in a list 
before sorting items
"""

# default is by ASCII
lst = ['hello', 'HELP', 'Helo']
lst.sort()
print(lst)

# assgin the key argument
lst.sort(key=str.lower)
print(lst)
