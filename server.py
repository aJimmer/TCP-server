#import socket module
from socket import *

#Prepare a sever socket
port = 3000
serverSocket = socket(AF_INET, SOCK_STREAM) 

serverSocket.bind(('',port))
serverSocket.listen(1)

while True:
#Establish the connection
	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept()

	try:
		message = connectionSocket.recv(1024)
		print message,'::', message.split()[0],':', message.split()[1]
		filename = message.split()[1]
		print filename,'||', filename[1:]
		f = open(filename[1:])
		outputdata = f.read()
		print outputdata

		#Send one HTTP header line into socket
		connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
		
		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
	except IOError:
	    #Send response message for file not found
	    connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')


#Close client socket
connectionSocket.close()