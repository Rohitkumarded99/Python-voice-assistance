import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import googlesearch
import requests 
import sys
from selenium import webdriver
import selenium




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishme ():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak ("good afternoon")
    else:
        speak("Good Evening!")  

    speak("Hello I Am your assistance sir, How May i Help You!")


def takecommand():
    #this will take microphone input fron the the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("listening...")
        r.pause_threshold = 0.5
        r.energy_threshold = 1200
        #r.dynamic_energy_ratio = 1.5
        #r.phrase_threshold = 0.2
        #r.energy_threshold = 300  # minimum audio energy to consider for recording
        r.dynamic_energy_threshold = 500
        #r.dynamic_energy_adjustment_damping = 0.15
        #r.dynamic_energy_ratio = 1.5
        #r.pause_threshold = 0.8  # seconds of non-speaking audio before a phrase is considered complete
        #r.operation_timeout = None  # seconds after an internal operation (e.g., an API request) starts before it times out, or ``None`` for no timeout

        #r.phrase_threshold = 0.3  # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
        #r.non_speaking_duration = 0.3  # seconds of non-speaking audio to keep on both sides of the recording
        audio = r.listen(source)
    try:
        print("recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print("user said\n",query)

    except Exception :
        # print ("E")
        print("say that again please....")
        speak("say that again please....")
        return "None"
    return query


if __name__=="__main__":
    wishme()
    while True :
    #if 1 :
        query = takecommand().lower()
        # logic for executing task based on query          
        if 'who is' in query:
            #speak('searching wikipedia...')
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=2)
            speak ("according to google")
            #print(results)
            speak(results) 

        elif 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak ("according to wikipedia")
            print(results)
            speak(results)

        elif 'ok jarvis' in query:
            wishme()

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        
        

        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")    

        elif 'open facebook' in query:
            speak("Opening facebook")
            webbrowser.open("facebook.com")

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            speak("playing music")
            # print(songs)
            x = random.choice(songs)
            os.startfile(os.path.join(music_dir,x))

        elif 'next music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            speak("changing music")
            x = random.choice(songs)
            os.startfile(os.path.join(music_dir,x))
       
        elif 'the time'  in query:
            strTime = datetime.datetime.now().strftime("%H:%M:S")
            speak(f"sir, the time is {strTime}")

        elif 'open chrome' in query:
            path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
        elif 'open torrent folder' in query:
            path="D:\\torrent"
            os.startfile(path) 

        elif 'open sublime text' in query:
            path="C:\\Program Files\\Sublime Text 3\\sublime_text.exe"   
            os.startfile(path)   

        elif 'open visual studio' in query:
            path="C:\\Users\\Rohit kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'open gamefolder' in query:
            path="F:\\game"
            os.startfile(path)

        elif 'open nfs' in query:
            path="F:\\game\\NEED FOR SPEED MOST WANTED\\speed.exe"
            os.startfile(path)

        elif 'open igi' in query:
            path="F:\\game\\Project IGI 1\\Project IGI 1\\IGI.exe"
            os.startfile(path)

        elif 'open max 3' in query:
            path="F:\\game\\Max Payne 3\\MaxPayne3.exe"
            os.startfile(path)    

        elif 'open D drive' in query:
            path="D:\\"
            os.startfile(path)

        elif 'open filmora' in query:
            path="C:\\Program Files\\Wondershare\\Wondershare Filmora (CPC)\\Wondershare Filmora9.exe"
            os.startfile(path)
        elif 'how are you' in query:
            speak("i am fine sir,Thanks for asking. What can i help you with?")

        elif 'i am bored' in query:
            speak("O i see !, Can i play some song or do you want to play game?")
        
        elif 'i want to play game' in query:
            speak ("which game do want to play? i have nfs, gta, IGI.")

        elif 'which game do you have' in query:
            speak (" i have nfs, gta, IGI.")

        elif 'play some songs' in query:
            speak("playing songs")
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            x = random.choice(songs)
            os.startfile(os.path.join(music_dir,x))
        elif 'play songs' in query:
            speak("playing songs")
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            x = random.choice(songs)
            os.startfile(os.path.join(music_dir,x))

        elif 'can you sing a song for me' in query:
            speak("i am really sorry!, i cant sing!, but i can play some songs for you" )

        elif 'what is ' in query:
            #speak('searching wikipedia...')
            query = query.replace("google", "")
            results = wikipedia.summary(query, sentences=2)
            speak ("according to google")
            #print(results)
            speak(results)

        elif 'what is the' in query:
            #speak('searching wikipedia...')
            query = query.replace("what is the", "")
            results = wikipedia.summary(query, sentences=2)
            speak ("according to google")
            print(results)
            speak(results) 

        elif 'where is ' in query:
            #speak('searching wikipedia...')
            query = query.replace("google", "")
            results = wikipedia.summary(query, sentences=2)
            speak ("according to google")
            print(results)
            speak(results)     
#joke
        elif 'joke' in query:
            res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"})
            if res.status_code == requests.codes.ok:
                speak(str(res.json()['joke']))
            else:
                speak('oops!I ran out of jokes')

        elif 'search' in query: 
            query = query.replace("search", "")

            #for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
            ab = webbrowser.open("https://google.com/search?q=%s" % query)
            print (ab)
        
        elif 'what do you mean by' in query: 
            query = query.replace("search", "")
            #for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
            ab = webbrowser.open("https://google.com/search?q=%s" % query)
            print (ab)
             
            
        elif 'shutdown' in query:
            speak('Bye bye Sir. Have a nice day')
            sys.exit()
               
 
        
              
        
