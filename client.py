import socket

def main():
	sock = socket.socket()
	sock.setblocking(1)
	print("Connecting to server..")
	sock.connect(('localhost', 9000))

	msg = input("Type in the data: ")
	
	while msg != "exit":
		print("Sending data...")
		
		sock.send(msg.encode())
		print("Accepting data...")

		data = sock.recv(1024)
		print(data.decode())

		msg = input('Enter msg: ')

	print("Closing connection..")
	sock.close()

if __name__ == '__main__':
	main()
