import socket
import pickle
import numpy as np
import cv2

cv2.setUseOptimized(True)

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
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# cap = cv2.VideoCapture(0)

fps = 0

while True:
	ret, frame = cap.read()

	if(fps == 10):
		fps = 0

		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		#smallg = cv2.resize(gray, (int(gray.shape[1] * 0.5), int(gray.shape[0] * 0.5)))
		faces = face_cascade.detectMultiScale(gray, 1.1, 4)

		for (x,y,w,h) in faces:
			cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

		cv2.imshow('frame', frame)

	else:
		fps += 1

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
s.close()