from __future__ import division
import speech_recognition as sr
import pygame
import time
import Adafruit_PCA9685

# sudo pip install adafruit-pca9685

pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)

pwm.set_pwm_freq(60)

living = True

pygame.mixer.init()

offline = False

def main():
    playSounds("intro")
    playSounds("commands")
    while living:
        command = listen()
        pickAction(command)
        time.sleep(0.1)

def playSounds(name):
    time.sleep(0.1)
    pygame.mixer.music.load("/home/pi/mole/audio/" + name + "N.mp3")
    time.sleep(0.1)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        pwm.set_pwm(1, 0, 375)
        pwm.set_pwm(0, 0, 375)
        pwm.set_pwm(2, 0, 250)
        time.sleep(.25)

        pwm.set_pwm(2, 0, 325)
        time.sleep(.25)

        pwm.set_pwm(1, 0, 500)
        pwm.set_pwm(0, 0, 250)
        pwm.set_pwm(2, 0, 250)
        time.sleep(.25)

        pwm.set_pwm(2, 0, 325)
        time.sleep(.25)
        continue

    if (name == "magic"):
        pwm.set_pwm(1, 0, 375)
        time.sleep(0.5)
        pwm.set_pwm(1, 0, 500)
        time.sleep(0.5)
        pwm.set_pwm(1, 0, 375)
    elif (name == "dance"):
        for i in range(2):
            pwm.set_pwm(1, 0, 375)
            pwm.set_pwm(0, 0, 250)
            time.sleep(.5)
            pwm.set_pwm(1, 0, 500)
            pwm.set_pwm(0, 0, 375)
            time.sleep(.5)
        pwm.set_pwm(1, 0, 375)

def listen():
    global offline
    print("Ready")
    pygame.mixer.music.load("/home/pi/mole/audio/readyN.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        print("Recognizing ...")
        pygame.mixer.music.load("/home/pi/mole/audio/recognizing.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        if (offline):
            pygame.mixer.music.load("/home/pi/mole/audio/offline.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
            output = r.recognize_sphinx(audio)
        else:
            output = r.recognize_google(audio)
        print("You said: " + output)
        return output
    except sr.UnknownValueError:
        return "Unknown"
    except sr.RequestError as e:
        offline = True
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return "Error"
    return "Error"

def pickAction(command):
    command = command.lower()
    if (command == "mole" or command == "information" or command == "chemistry"):
        playSounds("mole")
    elif (command == "magic"):
        playSounds("magic")
    elif (command == "dance"):
        playSounds("dance")
    elif (command == "command"):
        playSounds("commands")
    elif (command == "jump"):
        playSounds("other")
    elif (command == "Error"):
        playSounds("error")
    elif (command == "Unknown"):
        playSounds("confused")
    elif (command == "halt"):
        exit()
    else:
        playSounds("confused")

main()
