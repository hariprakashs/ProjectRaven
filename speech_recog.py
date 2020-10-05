import speech_recognition as sr
import pyttsx3 as p
from selenium import webdriver
import datetime
import webbrowser
e = p.init('sapi5')
voices = e.getProperty('voices')
e.setProperty('voice', voices[0].id)
class Raven():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:/Program Files/Google/Chrome/Application/chromedriver.exe')
    def speak(self,ip):
        e.say(ip)
        e.runAndWait()
    def looped(self):
        self.speak("Anything else I can help you with Sir?")
        ip=self.recogonise()
        ip=ip.lower()
        if 'yes' in ip:
            return True
        else:
            self.speak("Thank You")
            return False

    def greet(self):
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            self.speak("Good Morning!")

        elif hour>=12 and hour<18:
            self.speak("Good Afternoon!")

        else:
            self.speak("Good Evening!")

        self.speak("Raven at your Service Sir. Please tell me how may I help you")

    def play(self,name):
        self.name=name
        self.driver.get(url = "https://www.youtube.com/results?search_query="+name)
        video = self.driver.find_element_by_xpath('//*[@id="dismissable"]')
        video.click()

    def process(self,p_input):
        self.query=p_input.lower()

        if 'wikipedia' in self.query:
            self.speak("According to Wikipedia")
            self.get_info(self.query)

        elif 'youtube' in self.query:
            self.speak("Opening Youtube")
            self.play(self.query)

        elif 'google' in self.query:
            self.speak("Opening Google")
            webbrowser.open("google.com")

        elif 'stackoverflow' in self.query:
            self.speak("Opening Stack OverFlow")
            webbrowser.open("stackoverflow.com")


        elif 'the time' in self.query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            self.speak(f"Sir, the time is {strTime}")


        elif 'how are you' in self.query:
            self.speak("I am fine, Thank you")
            self.speak("How are you, Sir")

        elif 'fine' in self.query or "good" in self.query:
            self.speak("It's good to know that your fine")


        elif "what's your name" in self.query or "What is your name" in self.query:
            self.speak("My friends call me Raven")

        elif 'exit' in self.query:
            self.speak("Thanks for giving me your time")
            exit()

        elif "who made you" in self.query or "who created you" in self.query:
            self.speak("I have been created by Hari.")

        elif 'joke' in self.query:
            self.speak(pyjokes.get_joke())

        elif "calculate" in self.query:

            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = self.query.lower().split().index('calculate')
            self.query = self.query.split()[indx + 1:]
            res = client.self.query(' '.join(self.query))
            answer = next(res.results).text
            print("The answer is " + answer)
            self.speak("The answer is " + answer)

        elif "where is" in self.query:
            self.query = self.query.replace("where is", "")
            location = self.query
            self.speak("User asked to Locate")
            self.speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif 'news' in self.query:

            try:
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1

                self.speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')

                for item in data['articles']:

                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    self.speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))


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
        self.speak(read_text)



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
one.greet()
while True:
    x=one.recogonise()
    one.process(x)
    check=one.looped()
    if not check:
        break
