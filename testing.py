import socket
import time

ip = '192.168.10.1'
port = 8889
droneAddress = (ip,port)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('',port))
print('waiting on port:', port)

s.sendto('command'.encode('utf-8'), droneAddress)
s.sendto('takeoff'.encode('utf-8'), droneAddress)
s.sendto('land'.encode('utf-8'), droneAddress)

# while 1:
# 	data, addr = s.recvfrom(1024)
# 	print(data)