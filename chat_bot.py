from cleverwrap import CleverWrap
import speech_recognition as sr
import pyttsx3
from random import randrange
import os

def chat(name):

    cw = CleverWrap('CC8x7w095WZ9FNYrDEvwgR5qK7w')

    #random greetings to start off the conversation
    greetings = ["How are you doing today?", "What's up dude?", "How goes it?", "How are you?", "What's on your mind?", "How's it hanging bro?", "What's going on my dude?"]

    whats = ["What was that?", "Come again?", "Could you repeat that?", "I'm having a hard time hearing you.", "Please say that again.", "What did you say?"]

    byes = ["Good talking with you", "Until next time", "Goodbye", "It's been a pleasure", "I enjoyed speaking with you", "So long", "See you later"]

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(greetings[randrange(len(greetings))])
    engine.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone(device_index=7) as source:
        while(1):
            r.adjust_for_ambient_noise(source)
            print("\n************** SPEAK NOW *************\n")
            audio = None
            text = None
            try:
                audio = r.listen(source)
                print("Converting to text")
                text = r.recognize_google(audio)
                text = text.lower()
            except sr.UnknownValueError as e:
                engine.say(whats[randrange(len(whats))])
                engine.runAndWait()
                continue
            print("You said: %s" % text)
            if text == "goodbye" or text == "bye":
                engine.say("%s %s" % (byes[randrange(len(byes))], name))
                engine.runAndWait()
                break
            print("Thinking of a reply")
            reply = cw.say(text)
            print(reply)
            engine.say(reply)
            engine.runAndWait()
    
if __name__ == "__main__":

    if os.path.exists("curr_name.txt"):
        name = open("curr_name.txt", "r").readlines()[0]
        os.remove("curr_name.txt")
        chat(name)
    

