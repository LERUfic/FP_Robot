# Import OpenCV2 for image processing
import cv2

# Import numpy for matrices calculations
import numpy as np
import os 
#NXT
import nxt.bluesock
import nxt.locator
import nxt.brick
from nxt.motor import *
from nxt.sensor import *
import time
import sys

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()

assure_path_exists("trainer/")

# Load the trained mode
recognizer.read('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start the video frame capture
cam = cv2.VideoCapture('rtsp://10.151.252.166:8080/h264_pcm.sdp')

# b = nxt.locator.find_one_brick()
b = nxt.bluesock.BlueSock('00:16:53:06:8C:55').connect()
scene =0
# Loop
while True:
    # Read the video frame
    ret, im =cam.read()

    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2,5)

    # For each face in faces
    for(x,y,w,h) in faces:

        # Create rectangle around the face
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

        # Recognize the face belongs to which ID
        Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check the ID if exist 
        if(Id == 1):
            Id = "Peminjam {0:.2f}%".format(round(100 - confidence, 2))

        confidence_percent =  round(100 - confidence, 2)
        print(confidence_percent)
        # Put text describe who is in the picture
        if(confidence_percent > 50):
            cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
            cv2.putText(im, str(Id), (x,y-40), font, 1, (255,255,255), 3)
            m_left = Motor(b, PORT_A)        
            m_right = Motor(b, PORT_B)
            #NXT Code
            if scene==0:
                m_right.turn(-5, 50)
                while Touch(b, PORT_4).get_sample()==False:
                    continue
                time.sleep(1)
                m_right.turn(5, 50)
                time.sleep(1)
                m_left.turn(-5, 50)
                scene=1
            elif scene==1:
                if Touch(b, PORT_1).get_sample()==True:
                    time.sleep(3)
                    m_left.turn(5, 50)
                    time.sleep(1)
                    m_right.turn(-5, 50)
                    while Touch(b, PORT_4).get_sample()==True:
                        continue
                    time.sleep(3)
                    m_right.turn(5, 50)
                    sys.exit(1)

    # Display the video frame with the bounded rectangle
    cv2.imshow('im',im) 

    # If 'q' is pressed, close program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Stop the camera
cam.release()

# Close all windows
cv2.destroyAllWindows()
