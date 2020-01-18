from collections import namedtuple

# create a namedtuple class
s = namedtuple('Stock', ['symbol', 'current', 'high', 'low'])
# construct a instance
stock = s("FB", 177.46, high=178.67, low=175.79)

# treat as a normal tuple
print(stock[1])

# treat as a named tuple
print(stock.symbol)

# the variables from named tuple is read only
stock.current = 100.0
