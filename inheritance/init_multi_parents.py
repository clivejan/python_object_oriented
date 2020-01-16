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

	def __init__(self, name, email):
		self.name = name
		self.email = email
		Contact.all_contacks.append(self)

class AddressHoder:

	def __init__(self, street, city, state, code):
		self.street = street
		self.city = city
		self.state = state
		self.code = code

class Friend(Contact, AddressHoder):

	# initialize all parents by passing required arguments
	def __init__(, self, name, email, phone, street, city, state, code)
		Contact.__init__(self, name, email)
		AddressHoder.init_(self, street, city, state, code)
		self.phone = phone
