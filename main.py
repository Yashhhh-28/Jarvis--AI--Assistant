import speech_recognition as sr
import pyttsx3
import musiclibrary
import webbrowser
from openai import OpenAI
from gtts import gTTS
import pygame
import os
import requests



#initializing recognizer and enignes
recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsapi = "<Your Key Here>"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()
#Text-To-Speech using gtts and pygame
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiProcess(command):
    client = OpenAI(api_key="<Your Key Here>",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone()  as source:
        print("Listening.....")
        audio= recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"you said:{query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that")
        return""
    except sr.RequestError:
        print("Network Error")
        return""
    
def open_file(path):
    if os.path.exists(path):
       os.startfile(path)
       print("Opening File")
    else:
        print("File not found")

def open_recycle_bin():
    os.system("start shell:RecycleBinFolder")

#Handle command

def processCommand(c):
    if "open google" in c.lower():
        print("opening google")
        speak("opening google")
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        print("opening facbook")
        speak("opening facebook")
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        print("opening youtube")
        speak("opening  youtube")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        print("opening linkedin")
        speak("opening  linkedin")
        webbrowser.open("https://linkedin.com")
        
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        if link:
            webbrowser.open(link)
        else:
            speak("sorry,I couldn't find that song.")
    
    elif "open file" in c.lower():
        speak("Tell me the file path")
        path= listen()
        open_file(path)
    
    elif "open recycle bin" in c.lower():
        speak("opening recycle bin")
        open_recycle_bin()

    
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
     
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

    # Stop jarvis if user says 'exit' or 'stop'  
    elif "exit" in command or"stop" in command:
            speak("Goodbye")
            exit()

    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output) 


# main jarvis loop

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes!")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))