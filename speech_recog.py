import speech_recognition as sr
import pyttsx3 as p
from selenium import webdriver


def speak(ip):
    e=p.init()
    e.say(ip)
    e.runAndWait()

def recogonise():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak")
        input = r.listen(source)
        try:
            processed_text = r.recognize_google(input)
            return processed_text
        except sr.UnknownValueError:
            return "Raven cannot recognise your voice"

x=recogonise()
print(x)
speak(x)
