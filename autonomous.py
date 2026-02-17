import RPi.GPIO as GPIO
import time

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

steerLeft = GPIO.PWM(lFor,100)
steerRight = GPIO.PWM(rFor,100)
throttleBack = GPIO.PWM(lBack,100)
throttleForwards = GPIO.PWM(rBack,100)

throttleForwards.start(0)
steerRight.start(0)
steerLeft.start(0)
throttleBack.start(0)


echo = 24
trig = 23

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

while True:
    
    throttleForwards.ChangeDutyCycle(75)

    #collision-detection

    GPIO.output(trig, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig,GPIO.LOW)

    print(GPIO.input(echo))

    while GPIO.input(echo) == 0:
        pulseSent = time.time()
    while GPIO.input(echo) == 1:
        pulseRec = time.time()
        
    print(pulseRec,pulseSent)

    pulseTime = pulseRec-pulseSent

    pulseTime = round(pulseTime,4)
    ## in cm
    distance = pulseTime*34400/2

    print(distance)

    if distance<50:
        throttleForwards.ChangeDutyCycle(0)
        time.sleep(0.5)
        throttleBack.ChangeDutyCycle(100)
        steerRight.ChangeDutyCycle(100)
        ##CALIBRATE
        time.sleep(5)
        throttleBack.ChangeDutyCycle(0)
        steerRight.ChangeDutyCycle(0)

    GPIO.output(trig,GPIO.LOW)
    time.sleep(0.1)

GPIO.cleanup()
