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

class Friend(Contact):
	# overwritten the method of superclass by using the same name
	def __init__(self, name, email, phone):
		self.name = name
		self.email = email
		self.phone = phone
