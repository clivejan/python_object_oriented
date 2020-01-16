class LongNameDict(dict):

	def longest_key(self):
		longest = None
		for key in self:
			if not longest or len(key) > len(longest):
				longest = key
		return longest

# test the new longest_ley method from a extened dict object
longkeys = LongNameDict()
longkeys['hello'] = 1
longkeys['longest yet'] = 5
longkeys['hello2'] = 'world'

print(longkeys.longest_key())
