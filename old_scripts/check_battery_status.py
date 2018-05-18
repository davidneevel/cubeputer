from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

chargingPin = 10
lowBattPin = 12

GPIO.setup(chargingPin, GPIO.IN)
GPIO.setup(lowBattPin, GPIO.IN)

try:
    while True:
        chargingVar = GPIO.input(chargingPin)
        print "charging = %d" % chargingVar
        lowBattVar = GPIO.input(lowBattPin)
        print "lowBattVar = %d" % lowBattVar

        sleep(.5)

except KeyboardInterrupt:
    GPIO.cleanup()
    print "cleaning up GPIO"