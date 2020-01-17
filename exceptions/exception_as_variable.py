try:
	raise ValueError("This is an argument.")
except ValueError as e:
	print(f"The exception arguments were {e.args}")
