class InvalidWithdrawal(Exception):
	
	def __init__(self, balance, amount):
		super().__init__(f"Wake up! You don't have ${amount} in your account.")
		self.balance = balance
		self.amount = amount

	def overage(self):
		return self.amount - self.balance

try:
	raise InvalidWithdrawal(25, 50)
except InvalidWithdrawal as e:
	print("I'm sorry, but your withdrawal is "
		"more than your balance by "
		f"{e.overage()}.")
