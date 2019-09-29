from cleverwrap import CleverWrap
import speech_recognition as sr
import pyttsx3
from random import randrange

def chat():

    cw = CleverWrap('CC8x7w095WZ9FNYrDEvwgR5qK7w')

    #random greetings to start off the conversation
    greetings = ["How are you doing today?", "What's up dude?", "How goes it?", "How are you?", "What's on your mind?", "How's it hanging bro?", "What's going on my dude?"]

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(greetings[randrange(len(greetings))])
    engine.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone(device_index=7) as source:
        while(1):
            r.adjust_for_ambient_noise(source)
            print("Waiting on speech from user")
            audio = r.listen(source)
            print("Converting to text")
            text = r.recognize_google(audio)
            print("Thinking of a reply")
            reply = cw.say(text)
            engine.say(reply)
            engine.runAndWait()
    cw.close()
    

if __name__ == "__main__":

    chat()
