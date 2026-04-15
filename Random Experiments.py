import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# Initialize TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use voices[1].id for female voice

# Speak text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Greet the user
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you! ")

# Listen to microphone and return voice as text
def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Better noise handling
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

    try:
        print("🔍 Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"👤 User said: {query}\n")
    except sr.UnknownValueError:
        print("😕 Couldn't understand. Please repeat...")
        speak("Sorry, I didn't catch that. Can you say it again?")
        return None
    except sr.RequestError:
        print("⚠️ Could not request results from Google Speech Recognition service.")
        speak("Speech service is down. Please check your internet connection.")
        return None
    return query

# Send email function
def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('youremail@gmail.com', 'your-password')  # Use env vars instead!
        server.sendmail('youremail@gmail.com', to, content)
        server.quit()
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't send the email.")

# Main execution starts here
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()
        if query is None:
            continue

        query = query.lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                speak("Sorry, I couldn't find any results.")

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            if os.path.exists(music_dir):
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
                else:
                    speak("No songs found in your music folder.")
            else:
                speak("Music folder not found.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            if os.path.exists(codePath):
                os.startfile(codePath)
            else:
                speak("VS Code path not found.")

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                if content:
                    to = "harryyourEmail@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                else:
                    speak("Couldn't get the message content.")
            except Exception as e:
                print(e)
                speak("Sorry my friend Harry. I couldn't send the email.")

        elif 'exit' in query or 'quit' in query or 'stop' in query:
            speak("Goodbye Sir! Have a great day 😊")
            break
