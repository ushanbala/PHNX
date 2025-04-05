import pyttsx3

engine = pyttsx3.init()

def talk(para):
    engine.say(para)
    engine.runAndWait()
