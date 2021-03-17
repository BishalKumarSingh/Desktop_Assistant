import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import sys
import random
import urllib.request
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'C:\\Users\\bisha\\Desktop\\Songs'
            songs = os.listdir(music_dir)
            rd=random.choice(songs)
            print(songs)    
            os.startfile(os.path.join(music_dir,rd ))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\bisha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to Bishal' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "PersonEmai@gmail.com"  
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Bishal. I am not able to send this email")    
        elif 'you can sleep' in query:
            speak('Thanks for using me sir')
            sys.exit()
        elif 'close notepad' in query:
            speak('Closing notepad sir')
            os.system('taskkill/f/im notepad.exe')
        
        elif 'switch the window' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')
        
        elif 'where i am' in query or 'where we are' in query:
            speak('wait sir, let me check')
            try:
                ipAdd=requests.get('https://api.ipify.org')
                print(ipAdd)
                url='http://ip-api.com/json/'
                get_requests= urllib.request.urlopen(url+ipAdd)
                #get_requests= requests.get(url+ipAdd)
                geo_data= geo_requests.json()
                city= geo_data['city']
                state= geo_data['state']
                country= geo_data['country']
                speak(f'sir,i am not sure but i think we are in {city} city of {state} state of {country} country')

            except Exception as e:
                speak('sorry sir because of network issue i am not able to find where we are')
                pass
