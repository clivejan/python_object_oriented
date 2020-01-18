from dataclasses import dataclass

@dataclass
class StockDecorated:
	name: str
	current: float
	high: float
	low: float

stock = StockDecorated("FB", 177.46, high=178.67, low=175.79)
print(stock.current)
