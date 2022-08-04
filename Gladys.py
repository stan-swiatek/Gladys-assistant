import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing Gladys...")
MASTER = "my lord"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)
    
    speak("I am Gladys, how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")
    

    except Exception as e:
        speak("Say that again please")
        query = None
    return query

def main():
    wishMe()
    query = takeCommand()

    if 'wikipedia' in query.lower():
        speak('Searching Wikipedia...')
        query = query.replace("Wikipedia", "")
        results = wikipedia.summary(query, sentences =2)
        print(results)
        speak(results)

    elif 'open google' in query.lower():
        speak("Opening Google")
        url = "google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url) 

    elif 'open youtube' in query.lower():
        speak("Opening Youtube")
        url = "youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url) 

    elif 'open reddit' in query.lower():
        speak("Opening Reddit")
        url = "reddit.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url) 

    elif 'play music' in query.lower():
        songs_dir = "C:\\Users\\ENTERUSERNAME\\Downloads\\music" 
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir,songs[0])) 

    elif 'time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")
        print(strTime)

    elif 'open code' in query.lower():
        codePath = "C:\\Users\\ENTERUSERNAME\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)


main()