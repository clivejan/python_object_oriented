from .database import Database

class Products:

	def __init__(self):
		self.name = 'Products'

	def get_database(self):
		database = Database()
		return database.name
