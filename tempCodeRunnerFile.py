import pygame
from gtts import gTTS 
import os 
def speak(text):
        tts = gTTS(text)
        tts.save('temp.mp3')
        
        #initialize pygame mixer
        pygame.mixer.init()
        
        #load the mp3 file
        pygame.mixer.music.load('temp.mp3')

        # play the mp3 file
        pygame.mixer.music.play()

        #keep the progra running until the music stops playing
        while pygame.mixer.music.get_busy:
            pygame.time.clock().tick(10)

            pygame.mixer.music.unload()
            os.remove("temp.mp3")
        speak("initializing jarvis...")