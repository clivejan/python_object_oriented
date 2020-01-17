def funny_division(divider):

	try:
		if divider == 13:
			raise ValueError("13 is an unlucky number to the author")
		return 100 / divider
	except (ZeroDivisionError, TypeError):
		return "Enter a number other than zero"

for value in [0, 'hello', 50.0, 13]:
	print(f"Testing {value}:", end=" ")
	print(funny_division(value))
