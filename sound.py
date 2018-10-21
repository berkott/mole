import pygame
import time

pygame.mixer.init()

def playSound(name):
    time.sleep(0.1)
    pygame.mixer.music.load("audio/" + name + "N.mp3")
    time.sleep(0.1)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

if __name__ == "__main__":
    playSound("mole")
