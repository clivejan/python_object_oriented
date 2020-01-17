import socket, gzip
from io import BytesIO

class LogSocket:
	"""
	decorate socket object with overritten original methods (send(), close())

	outputs any data to the server's console before it sends to the client
	"""
	def __init__(self, socket):
		self.socket = socket

	def send(self, date):
		print(f"Sending {date} to {self.socket.getpeername()[0]}")
		self.socket.send(date)

	def close(self):
		self.socket.close()

class GzipSocket:
	"""
	decorate socket object with overritten original methods (send(), close())

	compresses data using gzip compression whenever send() is called
	"""
	def __init__(self, socket):
		self.socket = socket

	def send(self, date):
		buf = BytesIO()
		zipfile = gzip.GzipFile(fileobj=buf, mode='w')
		zipfile.write(date)
		zipfile.close()
		self.socket.send(buf.getvalue())

	def close(self):
		self.socket.close()

def respond(client):
	"""
	prompt user to enter something and send it to client, then close connection
	"""
	response = input("Enter a value: ")
	client.send(bytes(response, 'utf8'))
	client.close()

# initliize a server socket on 24010
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 24011))
server.listen(1)

log_send = False
compress_hosts = []

try:
	while True:
		# calling respond with the client object when a client connected
		client, addr = server.accept()

		# danamically switches between different decorate versions
		if log_send:
			client = LogSocket(client)
		if client.getpeername()[0] in compress_hosts:
			client = GzipSocket(client)
		respond(client)

finally:
	server.close()
