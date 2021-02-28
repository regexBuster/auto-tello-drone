import socket

ip = '192.168.10.1'
port = 8889
droneAddress = (ip,port)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('',port))
print('waiting on port:', port)

#send commands to startup the drone and turn on the video stream
s.sendto('command'.encode('utf-8'), droneAddress)
s.sendto('streamon'.encode('utf-8'), droneAddress)

flying = True

while flying:
	x = raw_input("Flight Command: ")

	#grounds the drone and turns of the stream if the exit command is sent
	if(x == 'exit'):
		flying = False
		s.sendto('land'.encode('utf-8'), droneAddress)
		s.sendto('streamoff'.encode('utf-8'), droneAddress)
		pass
	#sends the command until the drone replies that it heard it properly
	else:
		response = 'error'

		while (response == 'error'):
			s.sendto(str(x).encode('utf-8'), droneAddress)
			data, addr = s.recvfrom(1024)
			response = data
			print(response)

#cleanup
cap.release()
cv2.destroyAllWindows()
s.close()