from dataclasses import dataclass

@dataclass(order=True)
class StockDecorated:
	name: str
	current: float = 0.0
	high: float = 0.0
	low: float = 0.0

# using default value to constrcut a object
stock = StockDecorated("FB")
print(stock)

# assgin values to constrcut a object
stock2 = StockDecorated("FB", 177.46, high=178.67, low=175.79)
print(stock2)

# add comparasons after orderred
print(stock > stock2)
print(stock < stock2)
