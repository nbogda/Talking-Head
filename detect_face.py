import os
import face_recognition
import re
from gtts import gTTS
import pyttsx3
from playsound import playsound
import pyaudio
import ibm_watson
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from queue import Queue, Full
import cv2

def detect_face():

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    
    images = os.listdir('images')
    img_o = face_recognition.load_image_file("new.png")
    img = face_recognition.face_encodings(img_o)
    #if there was not a face in the frame
    if not img:
        engine.say("I don't see anyone there.")
        engine.runAndWait()
        return False
    
    for image in images:
        curr = face_recognition.load_image_file("images/" + image)
        curr = face_recognition.face_encodings(curr)[0]
        result = face_recognition.compare_faces(img, curr)
        #if face was recognized, greet the person by name
        if result[0]:
            name = re.search(r"(.*).png", image).group(1) 
            engine.say("Hello %s, nice to see you again." % name)
            engine.runAndWait()
            return True
    #if face was not recognized, ask for name and store face
    engine.say("I don't think I've met you before, what's your name?")
    engine.runAndWait()
    name = input()
    engine.say("Nice to meet you %s, my name is Jeremy." % name)
    engine.runAndWait()
    cv2.imwrite("images/%s.png" % name, img_o) 
    return True

if __name__ == "__main__":
   
    if not detect_face():
        print("No face detected")
