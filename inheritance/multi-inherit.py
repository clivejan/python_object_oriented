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

class MailSender:

	def send_mail(self, message):
		print(f"Sendmail mail to {self.email}")
		# Add e-mail logic here by smtplib

# define a multiple inheritance class
class EmailableContact(Contact, MailSender):
	pass

# test the multiple inheritance class
e = EmailableContact('John Smith', 'jsmith@example.net')
e.send_mail('Hello, test email here')
