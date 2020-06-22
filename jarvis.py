import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wk
import webbrowser as wb
import os

# Initialization
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe(uname):
    hour = int(datetime.datetime.now().hour)
    print(f"Hello {uname} Sir!")
    speak("Hello " + uname + " Sir!")
    if hour >= 0 and hour < 12:
        print("Good Morning!")
        speak("good morning!")
    elif hour >= 12 and hour < 18:
        print("Good Afternoon!")
        speak("good afternoon!")
    else:
        print("Good Evening!")
        speak("good evening!")
    print("I am Jarvis, your personal assistant, like in IronMan Movie. How may I help you today sir?")
    speak("I am Jarvis, your personal assistant, like in IronMan Movie. How may I help you today sir?")

def getName():
    print("Hello sir! May I know your name please?")
    speak("Hello sir! May I know your name please?")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting for your name...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognising...")
            query = r.recognize_google(audio, language='en-in')
            speak(f"You said: {query}, is this right?")
            print(f"You said: {query}, is this right?")
            ans = takeCommand().lower()
            if 'yes' in ans:
                return query
            else:
                return "None"
        except Exception as e:
            speak("Didn't get you sir?")
            print("Say your name again please!")
            return "None"


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognising...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}")
        except Exception as e:
            speak("Say that again please!")
            print("Say that again please!")
            return "None"
        return query

if __name__ == "__main__":
    uname = getName()
    while uname.__contains__("None"):
        uname = getName()
    wishMe(uname)
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            print("Searching Wikipedia...")
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wk.summary(query, sentences=2)
            print("According to Wikipedia, " + results)
            speak("According to Wikipedia, " + results)
            print("You need anything else sir?")
            speak("You need anything else sir?")
        elif 'stop' in query or 'bye-bye' in query or 'exit' in query:
            print(f"Thank you {uname} sir. Have a nice day!")
            speak(f"Thank you {uname} sir. Have a nice day!")
            print("Exiting Jarvis...")
            os._exit(1)
        elif 'open youtube' in query:
            speak("Opening YouTube sir")
            wb.open("https://youtube.com")
        elif 'open google' in query:
            speak("opening google sir")
            wb.open("https://google.com")
        elif 'play music' in query:
            speak("Playing music from gaana")
            wb.open_new_tab(
                "https://gaana.com/playlist/gaana-dj-best-of-arijit-singh")
        elif 'stackoverflow' in query:
            speak("Opening stackoverflow")
            wb.open("https://stackoverflow.com")
        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M %p")
            print(f"The time is: {time}")
            speak(f"Sir, The time is: {time}")
            print("Is there anything else I can do sir?")
            speak("Is there anything else I can do sir?")
        elif 'date' in query:
            date = datetime.datetime.now().strftime("%A. %d, %B, %Y")
            print(f"Sir, Today is: {date}.")
            speak(f"Sir, Today is: {date}.")
            print("Is there anything else I can help with sir?")
            speak("Is there anything else I can help with sir?")
        elif 'command prompt' in query or 'cmd' in query:
            print("Opening Command Prompt...")
            speak("Opening Command Prompt")
            os.startfile("cmd.exe")
        elif 'powershell' in query:
            print("Opening Powershell...")
            speak("opening powershell")
            os.startfile("powershell.exe")
        elif 'hello' in query:
            print(f"Hello {uname} Sir.")
            speak(f"Hello {uname} Sir.")
