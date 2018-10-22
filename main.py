from __future__ import division
import speech_recognition as sr
import pygame
import time
import Adafruit_PCA9685

# sudo pip install adafruit-pca9685

# pwm = Adafruit_PCA9685.PCA9685()

pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)

servo_min = 300  # Min pulse length out of 4096
servo_max = 400  # Max pulse length out of 4096
pwm.set_pwm_freq(60)

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
        #pwm.set_pwm(0, 0, servo_min)
        #time.sleep(1)
        #pwm.set_pwm(0, 0, servo_max)
        #time.sleep(1)

        # ___ Arm motor
        pwm.set_pwm(1, 0, 375)
        pwm.set_pwm(0, 0, 375)
        pwm.set_pwm(2, 0, 250)
        print("first command")
        time.sleep(1)
        pwm.set_pwm(1, 0, 500)
        pwm.set_pwm(0, 0, 250)
        pwm.set_pwm(2, 0, 325)
        print("second command")
        time.sleep(1)
        
        # Mouth motor
        #pwm.set_pwm(2, 0, 250)
        #time.sleep(1)
        #pwm.set_pwm(2, 0, 325)
        #time.sleep(1)
        
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
    if (command == "mole"):
        playSounds("mole")
    elif (command == "magic"):
        playSounds("magicNew")
    elif (command == "dance"):
        playSounds("dance")
    elif (command == "repeat"):
        playSounds("commands")
    elif (command == "jump"):
        playSounds("other")
    elif (command == "Error"):
        playSounds("error")
    elif (command == "Unknown"):
        playSounds("confused")
    else:
        playSounds("confused")

def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

main()
