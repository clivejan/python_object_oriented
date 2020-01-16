class Contact:
	# class variables can be accessed from all objects derived from this class. 
	all_contacks = []

	def __init__(self, name, email):
		self.name = name
		self.email = email
		Contact.all_contacks.append(self)

class Supplier(Contact):

	def order(self, order):
		print("If this were a real system we would send "
			f"{order} order to {self.name}")

c = Contact('some body', 'somebody@example.com')
s = Supplier('sup Plier', 'supplier@example.com')

# Verify subclss has the same attributes as superclass
print(c.name, c.email, s.name, s.email)

# Access class variable from differenets instances
print(c.all_contacks)
print(s.all_contacks)

# Access specified subclass method
s.order('job')

# Access subclass method from superclass will raise error
c.order('job')
