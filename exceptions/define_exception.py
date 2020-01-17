class InvalidWithdrawal(Exception):
	pass

raise InvalidWithdrawal("Wake up! You don't have $50 in your account.")
