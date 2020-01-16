from ..database import Database

class Square:

	def __init__(self):
		self.name = 'Square'

	def get_database(self):
		database = Database()
		return database.name
