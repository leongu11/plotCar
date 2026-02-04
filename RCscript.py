import RPi.GPIO as GPIO
import time
import websockets
import asyncio


# setting up motors 
GPIO.setmode(GPIO.BCM)

lBack = 17
rBack = 27

lFor = 4
rFor = 22

GPIO.setup(rBack,GPIO.OUT)
GPIO.setup(lFor,GPIO.OUT)
GPIO.setup(lBack,GPIO.OUT)
GPIO.setup(rFor,GPIO.OUT)

#initializing pwm instances and starting at 0

##frequency

throttleBack = GPIO.PWM(lFor,100)
steerRight = GPIO.PWM(rFor,100)
steerLeft = GPIO.PWM(lBack,100)
throttleForwards = GPIO.PWM(rBack,100)

throttleForwards.start(0)
steerLeft.start(0)
steerRight.start(0)
throttleBack.start(0)

GPIO.cleanup()
