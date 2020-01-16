class ContactList(list):

	def search(self, name):
		"""
		Return all contacts that contain the search value
		in their name. 
		"""
		matching_contacts = []
		for contact in self:
			if name in contact.name:
				matching_contacts.append(contact)
		return matching_contacts

class Contact:
	all_contacks = ContactList()

	#def __init__(self, name, email):
	def __init__(self, name="", email="", **kwargs)
		super().__init__(**kwargs)
		self.name = name
		self.email = email
		Contact.all_contacks.append(self)

class AddressHoder:

	#def __init__(self, street, city, state, code):
	def __init__(self, street="", city="", state="", code="", **kwargs):
		super().__init__(**kwargs)
		self.street = street
		self.city = city
		self.state = state
		self.code = code

class Friend(Contact, AddressHoder):

	# using keyword arguments to mitigate diamond problem
	#def __init__(, self, name, email, phone, street, city, state, code)
	def __init__(, self, phone="", **kwargs)
		self.phone = phone
