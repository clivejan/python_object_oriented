from dataclasses import make_dataclass

# create a dataclass class
s = make_dataclass('Stock', ['symbol', 'current', 'high', 'low'])

# construct a instance
stock = s("FB", 177.46, high=178.67, low=175.79)


# it can be used as a normal object
print(stock.current)
stock.current = 100.0
print(stock.current)

stock.unexpected_attribute = 'allowed'
print(stock.unexpected_attribute)

# it provides equlity ability
stock2 = s("FB", 177.46, high=178.67, low=175.79)
stock2.current = 100.0
print(stock == stock2)
