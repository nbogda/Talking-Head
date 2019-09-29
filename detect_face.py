import os
import face_recognition
import re
import pyttsx3
import cv2
from random import randrange

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
        return None
    
    name = None

    for image in images:
        curr = face_recognition.load_image_file("images/" + image)
        curr = face_recognition.face_encodings(curr)[0]
        result = face_recognition.compare_faces(img, curr)
        #if face was recognized, greet the person by name
        if result[0]:
            name = re.search(r"(.*)_", image).group(1) 
            engine.say("Hello %s, nice to see you again." % name)
            engine.runAndWait()
            return name
    #if face was not recognized, ask for name and store face
    engine.say("I haven't met you before, what's your name?")
    engine.runAndWait()
    name = input()
    engine.say("Nice to meet you %s, my name is Jeremy." % name)
    engine.runAndWait()
    cv2.imwrite("images/%s_%s.png" % (name, randrange(10000000)), img_o) 
    return name

if __name__ == "__main__":
   
    result = detect_face()

    if result is not None:
        curr_name = open("curr_name.txt", "w")
        curr_name.write(result)
