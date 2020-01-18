import datetime

def middle(stock, date):
	# tuple unpacks
	symbol, current, high, low = stock
	return ((high + low) / 2, date)

# using parenthses to separate tuple from other parameters
mid_value, date = middle(("FB", 177.46, 178.67, 175.79), \
	datetime.date(2020, 1, 18))

print(mid_value, date)
