#import socket module
from socket import *

port = 3000
serverSocket = socket(AF_INET, SOCK_STREAM) 
#Prepare a sever socket
#Fill in start
serverSocket.bind(('',port))
serverSocket.listen(1)
#Fill in end
while True:
#Establish the connection
	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept()

	try:
	#Fill in start
	#Fill in end
		print 'trying...'
		message = connectionSocket.recv(1024)
		print message,'::', message.split()[0],':', message.split()[1]
		filename = message.split()[1]
		print filename,'||', filename[1:]
		f = open(filename[1:])
		outputdata = f.read()
		print outputdata
		#Send one HTTP header line into socket
		#Fill in start
		connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
		#connectionSocket.send(outputdata);
		#Fill in end
		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
	except IOError:
	    #Send response message for file not found
	    connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')

#Fill in start #Fill in end
#Close client socket #Fill in start #Fill in end
connectionSocket.close()