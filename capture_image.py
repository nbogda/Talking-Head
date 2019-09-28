from cv2 import *
import os
import face_recognition
import numpy as np

def capture_image():

    cam = VideoCapture(0)
    success, img = cam.read()

    if success:
        imwrite("new.png", img)
        #check to see if face is able to be detected, if not, ask
        #i havent seen you before, whats your name
        #or
        #hello, nice to see you again <name>


if __name__ == "__main__":

    capture_image()
