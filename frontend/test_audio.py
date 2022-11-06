from gtts import gTTS
import io
from playsound import playsound
import time
import pygame.mixer
tts = gTTS("Dette er en test", lang="no")
tts.save("audio.mp3")
pygame.mixer.init()
pygame.mixer.music.load("audio.mp3")

pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    time.sleep(0.04)
pygame.mixer.quit()