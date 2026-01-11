import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

lFor = 17
rFor = 27

lBack = 22
rBack = 23

GPIO.setup(rBack,GPIO.OUT)
GPIO.setup(lFor,GPIO.OUT)
GPIO.setup(lBack,GPIO.OUT)
GPIO.setup(rFor,GPIO.OUT)


while True:

    i = input()
    
    if i == 'w':
        GPIO.output(rFor,GPIO.HIGH)
        GPIO.output(lFor,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(rFor,GPIO.LOW)
        GPIO.output(rBack,GPIO.LOW)
        GPIO.output(lFor,GPIO.LOW)
        GPIO.output(lBack,GPIO.LOW)
        
    if i == 'a':
        GPIO.output(lFor,GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(rFor,GPIO.LOW)
        GPIO.output(rBack,GPIO.LOW)
        GPIO.output(lFor,GPIO.LOW)
        GPIO.output(lBack,GPIO.LOW)
        
    if i == 'd':
        GPIO.output(rFor,GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(rFor,GPIO.LOW)
        GPIO.output(rBack,GPIO.LOW)
        GPIO.output(lFor,GPIO.LOW)
        GPIO.output(lBack,GPIO.LOW)
    if i == 'r':
        GPIO.output(rBack,GPIO.HIGH)
        GPIO.output(lBack,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(rFor,GPIO.LOW)
        GPIO.output(rBack,GPIO.LOW)
        GPIO.output(lFor,GPIO.LOW)
        GPIO.output(lBack,GPIO.LOW)


##
##    i = input()
##    
##    if i == 'w':
##        GPIO.output(rFor,GPIO.HIGH)
##        GPIO.output(lFor,GPIO.HIGH)
##    if i == 'a':
##        GPIO.output(lFor,GPIO.HIGH)
##    if i == 'd':
##        GPIO.output(rFor,GPIO.HIGH)
##    if i == 'r':
##        GPIO.output(rBack,GPIO.HIGH)
##        GPIO.output(lBack,GPIO.HIGH)
##    if i == 's':
##        GPIO.output(rFor,GPIO.LOW)
##        GPIO.output(rBack,GPIO.LOW)
##        GPIO.output(lFor,GPIO.LOW)
##        GPIO.output(lBack,GPIO.LOW)

        
##GPIO.output(rFor,GPIO.HIGH)
##GPIO.output(lFor,GPIO.HIGH)
##time.sleep(2)
##GPIO.output(rFor,GPIO.LOW)
##GPIO.output(lFor,GPIO.LOW)
##
##GPIO.output(rFor,GPIO.LOW)
##GPIO.output(lFor,GPIO.HIGH)
##time.sleep(0.5)
##GPIO.output(rFor,GPIO.LOW)
##GPIO.output(lFor,GPIO.LOW)
##
##GPIO.output(rBack,GPIO.HIGH)
##GPIO.output(lBack,GPIO.HIGH)
##time.sleep(1)
##GPIO.output(rBack,GPIO.LOW)
##GPIO.output(lBack,GPIO.LOW)

GPIO.cleanup()
