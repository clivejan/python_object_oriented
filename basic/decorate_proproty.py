class Silly:

	@property
	def silly(self):
		""""This is a silly property")"""
		print("Your are getting silly")
		return self._silly

	@silly.setter
	def silly(self, value):
		print(f"You are making silly {value}")
		self._silly = value

	@silly.deleter
	def silly(self):
		print("Whoah, you killed silly!")
		del self._silly

s = Silly()
s.silly = 'funny'
print(s.silly)
del s.silly
help(s)
