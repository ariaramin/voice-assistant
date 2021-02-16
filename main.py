
import webbrowser
import speech_recognition as sr
from time import ctime
import pyttsx3

r = sr.Recognizer()
web = webbrowser.Chrome()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    rate = engine.getProperty('rate')
    engine.setProperty(rate, 90)
    engine.runAndWait()

def rec(ask=False):
    with sr.Microphone(1) as source:
        if ask:
            print(ask)
        else:
            print('say something...')                                                      
            speak('say something')       

        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = audio.recognize_google(audio)
                
        except sr.UnknownValueError:
            speak("Sorry, I did not get that")
        except sr.RequestError:
            speak('Sorry, my speech service is down')
        return voice_data

def respons(data):
        if "hello" in data:
            speak("hello, how are you?")
        elif "what's your name" in data:
            speak("My name is Siri, what's your name")
        elif "my name is" in data:
            speak("nice to meet you")
        elif "how are you" in data:
            speak("i'm fine")
        elif 'what time is it' in data:
            print(ctime())
            speak(ctime())
        elif 'search' in data:
            search = rec('what do you want to search?')
            speak('what do you want to search?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)

            
respons(rec())