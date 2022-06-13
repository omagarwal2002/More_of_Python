import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12: 
        speak("Good Morning!")
    elif hour>=12 and hour<=18: 
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you ")

def takeCommand():
    #it takes microphone input from user mic and gives string output
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...........")
        r.pause_threshold = 1
        audio= r.listen(source)

    try:
        print("Recognizing....")
        query= r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please.....")
        return "None"
    return query

def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('omagarwal000001@gmail.com', 'o123a567')
    server.sendmail('omagarwal000001@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for executing tastks based on quesry
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query= query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'play music' in query:
            music_dir='C:\\Users\\Dell\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath =  "D:\\vs code\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open java' in query:
            codePath =  "C:\\Users\\Dell\\eclipse\\java-2021-06\\eclipse\\eclipse.exe"
            os.startfile(codePath)

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content= takeCommand()
                to="omagarwal2002@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry Om bro. I am a=unable to send this email.")

        elif 'jarvis stop' in query:
            speak("Thank you sir!")
            break
