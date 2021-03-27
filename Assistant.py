# This is an assistant
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    newVoiceRate = 130
    engine.setProperty('rate', newVoiceRate)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning sir")
    elif 12 <= hour < 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("I am zerix,  how may i help you ")


def takecommand():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        listener.pause_threshold = 1
        audio = listener.listen(source)
    try:
        print("Recognizing...")
        query = listener.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()  # Converting user query into lower case

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
        elif 'slow songs' in query:
            webbrowser.open("https://www.youtube.com/watch?v=etDblzZq_BU&list=RDetDblzZq_BU&start_radio=1")
