def funny_division(divider):
	try:
		return 100 / divider
	except ZeroDivisionError:
		return "Zero is not a good idea!"

# ZeroDivisionError will be habdled
print(funny_division(0))

print(funny_division(50.0))

# TypeError won't be handled
print(funny_division('hello'))
