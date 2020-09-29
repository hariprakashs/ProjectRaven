import speech_recognition as sr
import pyttsx3 as p
from selenium import webdriver
class Raven():
    def __init__(self):
        speak("Hi, I am Raven.")
        self.driver=webdriver.Ie(executable_path='C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')



    def speak(self,ip):
        e=p.init()
        e.say(ip)
        e.runAndWait()

    def recogonise(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("speak")
            input = r.listen(source)
            try:
                processed_text = r.recognize_google(input)
                return processed_text
            except sr.UnknownValueError:
                return "Raven cannot recognise your voice"

one=Raven()
x=one.recogonise()
print(x)
one.speak(x)
