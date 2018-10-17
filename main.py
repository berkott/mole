import speech_recognition as sr
import pygame
import time

living = True

pygame.mixer.init()

def main():
    playSounds("intro")
    playSounds("commands")
    while living:
        command = listen()
        pickAction(command)
        time.sleep(0.1)
    
def playSounds(name):
    time.sleep(0.1)
    pygame.mixer.music.load("audio/" + name + "N.mp3")
    time.sleep(0.1)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

def listen():
    print("Ready")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        # output = r.recognize_sphinx(audio)
        output = r.recognize_google(audio)
        print("You said: " + output)
        return output
    except sr.UnknownValueError:
        return "Unknown"
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return "Error"
    return "Error"

def pickAction(command):
    if (command == "what is a mole"):
        playSounds("mole")
    elif (command == "do magic"):

        playSounds("magicNew")
    elif (command == "please dance"):
        playSounds("dance")
    elif (command == "repeat commands"):
        playSounds("commands")
    elif (command == "jumping is fun"):
        playSounds("other")
    elif (command == "Error"):
        playSounds("error")
    elif (command == "Unknown"):
        playSounds("confused")
    else:
        playSounds("confused")

main()