import socket
import numpy as np
import cv2

#ensures opencv's optimized functions
cv2.setUseOptimized(True)

def get_udp_video_address():
	address_schema = 'udp://@0.0.0.0:11111'
	address = address_schema.format(ip=ip, port=port)
	return address

#capture the video stream from a udp connection to the drone
cap = cv2.VideoCapture(get_udp_video_address())

#create a variable holding the cascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#this allows me to lower the frame rate a tad to make the video faster
fps = 0

while True:
	ret, frame = cap.read()

	if(fps == 10):
		fps = 0

		#converts the frame to grayscale and tries to detect faces then you can add a rectangle around the face
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.1, 4)

		for (x,y,w,h) in faces:
			cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

		cv2.imshow('frame', frame)
	else:
		fps += 1

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

#cleanup
cap.release()
cv2.destroyAllWindows()
s.close()