import socket

# initliize a client socket and connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 24011))

# print out anything recieved from the conntection and close socket
print(f"Received: {client.recv(1024)}")
client.close()
