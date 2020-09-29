import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    input = r.listen(source)

    try:
        processed_text = r.recognize_google(input)
        print(processed_text)
    except sr.UnknownValueError:
        print("Google cannot recognise your voice one")
