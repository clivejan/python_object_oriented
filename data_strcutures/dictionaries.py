stocks = {
	"GOOG": (1235.20, 1242.54, 1231.06),
	"MSFT": (110.41, 110.45, 109.84),
}

print(stocks['GOOG'])

# using a method of dict to access a non-existed key
print(stocks.get('RIM', 'Not Found'))

# setting values if the key didn't exist
stocks.setdefault("BERY", (10.87, 10.76, 10.90))
print(stocks['BERY'])

stocks.setdefault("BERY", (100.0, 110.0, 120.0))
print(stocks['BERY'])

# keys(), valies(), items()
for stock, values in stocks.items():
	print(f"{stock} last value is {values[0]}")
