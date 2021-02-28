import socket
import time

ip = '192.168.10.1'
port = 8889
droneAddress = (ip,port)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('',port))
print('waiting on port:', port)

s.sendto('command'.encode('utf-8'), droneAddress)
s.sendto('streamon'.encode('utf-8'), droneAddress)

flying = True

while flying:
	x = raw_input("Flight Command: ")

	if(x == 'exit'):
		flying = False
		s.sendto('land'.encode('utf-8'), droneAddress)
		s.sendto('streamoff'.encode('utf-8'), droneAddress)
		pass
	else:
		response = 'error'

		while (response == 'error'):
			s.sendto(str(x).encode('utf-8'), droneAddress)
			data, addr = s.recvfrom(1024)
			response = data
			print(response)

cap.release()
cv2.destroyAllWindows()
s.close()

# while 1:
# 	data, addr = s.recvfrom(1024)
# 	print(data)