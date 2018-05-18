from time import sleep

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

pin = 40

GPIO.setup(pin, GPIO.OUT)


for a in range(0,3):
    GPIO.output(pin, GPIO.HIGH)
    sleep(.25)
    GPIO.output(pin, GPIO.LOW)
    sleep(1)
    
GPIO.cleanup()