import speech_recognition as sr
import pyttsx3 as p
from selenium import webdriver
class Raven():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:/Program Files/Google/Chrome/Application/chromedriver.exe')
    def speak(self,ip):
        e=p.init()
        e.say(ip)
        e.runAndWait()

    def get_info(self,query):
        print("INFO")
        self.query = query
        self.driver.get( url = "https://www.wikipedia.org/" )
        search=self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter=self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
        enter.click()
        info=self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[2]')
        read_text=info.text
        print(read_text)
        self.speak(read_text)



    def recogonise(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("speak")
            input = r.listen(source)
            try:
                processed_text = r.recognize_google(input)
                print(processed_text)
                return processed_text
            except sr.UnknownValueError:
                return "Raven cannot recognise your voice"

one=Raven()
one.speak("Hi, I am Raven. Input Please")
x=one.recogonise()

one.get_info(x)


print(x)
one.speak(x)
