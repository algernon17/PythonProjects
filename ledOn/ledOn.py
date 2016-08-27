#!/usr/bin/env python
# LED Test Program

import RPi.GPIO as GPIO, time



def ledOn():
    print "LED is ON"
    print
    for i in range(0,5):
        print i, ' : orange'
        GPIO.output(greenLed, False)
        GPIO.output(orangeLed, True)
        time.sleep(0.1)
        GPIO.output(orangeLed, False)
        time.sleep(0.1)
        GPIO.output(orangeLed, True)
        time.sleep(0.2)
        print i, ' : green'
        GPIO.output(orangeLed, False)
        GPIO.output(greenLed, True)
        time.sleep(0.1)
        GPIO.output(greenLed, False)
        time.sleep(0.1)
        GPIO.output(greenLed, True)
        time.sleep(0.2)
        # clear outputs
        GPIO.output(greenLed, False)
        GPIO.output(orangeLed, False)

if __name__ == '__main__':
    orangeLed = 11
    greenLed = 12
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(orangeLed, GPIO.OUT)
    GPIO.setup(greenLed, GPIO.OUT)
    ledOn()
