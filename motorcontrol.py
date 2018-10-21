from __future__ import division
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)
pwm.set_pwm_freq(60)

def moveMotor(channel, servo_min, servo_max, waittime):
    pwm.set_pwm(channel, 0, servo_min)
    time.sleep(waittime)
    pwm.set_pwm(channel, 0, servo_max)
    time.sleep(waittime)

def moveMouth():
    moveMotor(2,250,300,0.5)

def moveArm():
    moveMotor(0,150,500,1)

def moveMole():
    moveArm()
    moveMouth()

if __name__=="__main__":
    moveMole()

