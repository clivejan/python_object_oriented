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

# test the new search method from a extened list object
c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@example.net")
c3 = Contact("Jenna C", "jennac@example.net")
result = [c.name for c in Contact.all_contacks.search('John')]
print(result)
