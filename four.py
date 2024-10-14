import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

four = pyttsx3.init()
voice = four.getProperty('voices')
four.setProperty('voice',voice[1].id)

def speak(audio):
    print('F.O.U.R :' + audio)
    four.say(audio)
    four.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)

def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning BABY Boss")
        speak("Have a stunning day")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon BABY Boss")
    if hour >= 18 and hour <24:
        speak("Good Night BABY Boss")
    speak("How can I help you?")

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 1
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio,language='en')
        print("BABY :" + query)
    except sr.UnknownValueError:
        print("Sorry BABY Boss")
        print("Please repeat again")
        query = c.recognize_google(audio,language='en')
    return query

if __name__ == '__main__':
    welcome()
    while True:
        query = command().lower()
        if "google" in query:
            speak("What should I search BABY Boss?")
            search = command().lower()
            url = f"https://www.google.com.vn/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')

        if "youtube" in query:
            speak("What should I search BABY Boss?")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
        elif "open video" in query:
            meme = r"C:\Users\Admin\Documents\League of Legends\Highlights"
            os.startfile(meme)
        elif "time" in query:
            time()
        elif "quit" in query:
            speak("FOUR is quitting. Goodbye BABY Boss")
            quit()