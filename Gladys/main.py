#from doctest import master
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio

print("Iinitializing Jarvis")

lord = "lord"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

# speech function
# takes string as input
# reads aloud 
def speak(text):
    engine.say(text)
    engine.runAndWait()



#welcome funtion
#welcome message depends on hour
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour < 12:
        speak("Good Morning my" + lord)

    elif hour >=12 and hour<18:
        speak("Good Afternoon my" + lord)

    else:
        speak("Good Evening my" + lord)
    
 #   speak("How may I help you sir?")


#function takes input/command via the microphone
#and returns as a string
def takeCommand():
    #reconizes speech using mic
    #classes Rec and Mic from speech_recognition module
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source,duration=1)
        print("Listening")
        audio = r.listen(source)
            
            

        try:
            print("Recognizing...")
            #recognizes input from microphone in english
            #using google engine
            query = r.recognize_google(audio, language = 'en-GB')
            #returns input as a string
            print(f"user said: {query}\n")

        except:
            print("Could you repeat please?")
            query = None
        return query



#main program starts here
speak("Initializing Jarvis")
wishMe()
query = takeCommand()



#logic to execute taks from query
#passes input to wikipedia search engine
#returns 2 sentces from wiki article
if 'wikipedia' in query.lower():
    speak('Searching wikipedia...')
    #removing work 'wikipedia' from search results
    query = query.replace('wikipedia', '')
    results = wikipedia.summary(query, sentences =2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
        speak("Opening Youtube")
        url = "youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)