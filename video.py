import socket
import pickle
import numpy as np
import cv2

ip = '0.0.0.0'
port = 11111
droneAddress = (ip,port)

max_length = 65540

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind(droneAddress)

def get_udp_video_address():
	address_schema = 'udp://@{ip}:{port}'
	address = address_schema.format(ip=ip, port=port)
	return address

cap = cv2.VideoCapture(get_udp_video_address())
# cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()

	gray = frame # cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	cv2.imshow('frame', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
s.close()