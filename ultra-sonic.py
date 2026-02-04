import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

echo = 24
trig = 23

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

while True:
    GPIO.output(trig, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig,GPIO.LOW)

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

    time.sleep(0.5)
GPIO.cleanup()