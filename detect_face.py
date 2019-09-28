import os
import face_recognition
import re
from gtts import gTTS
import pyttsx3
from playsound import playsound
import pyaudio
import speech_recognition as sr

def detect_face():

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    
    images = os.listdir('images')
    img = face_recognition.load_image_file("new.png")
    img = face_recognition.face_encodings(img)
    if not img:
        engine.say("I don't see anyone there.")
        engine.runAndWait()
        return False
    
    for image in images:
        curr = face_recognition.load_image_file("images/" + image)
        curr = face_recognition.face_encodings(curr)[0]
        result = face_recognition.compare_faces(img, curr)
        if result[0]:
            name = re.search(r"(.*).png", image).group(1) 
            engine.say("Hello %s, nice to see you again." % name)
            engine.runAndWait()
            return True
    engine.say("I don't think I've met you before, what's your name?")
    engine.runAndWait()
    r = sr.recognize_google()
    return True


if __name__ == "__main__":

    if not detect_face():
        print("No face detected")
