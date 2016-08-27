#!/usr/bin/env python
# LED Test Program

import RPi.GPIO as GPIO, time

def led_double_blink():
        GPIO.output(greenLed, False)
        GPIO.output(orangeLed, True)
        time.sleep(0.1)
        GPIO.output(orangeLed, False)
        time.sleep(0.1)
        GPIO.output(orangeLed, True)
        time.sleep(0.2)
        GPIO.output(greenLed, True)
        GPIO.output(orangeLed, False)
        time.sleep(0.1)
        GPIO.output(greenLed, False)
        time.sleep(0.1)
        GPIO.output(greenLed, True)
        time.sleep(0.2)

def led_single_blink():
        GPIO.output(greenLed, False)
        GPIO.output(orangeLed, True)
        time.sleep(0.2)
        GPIO.output(greenLed, True)
        GPIO.output(orangeLed, False)
        time.sleep(0.2)
    
def ledOn():
    print "LED cycling..."
    for i in range(0,20):
        print i
        led_single_blink()
        led_single_blink()
        led_single_blink()
        led_single_blink()
        led_double_blink()
        led_double_blink()
        led_double_blink()
        led_double_blink()

if __name__ == '__main__':
    orangeLed = 11
    greenLed = 12
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(orangeLed, GPIO.OUT)
    GPIO.setup(greenLed, GPIO.OUT)
    ledOn()
    # clear outputs
    GPIO.output(greenLed, False)
    GPIO.output(orangeLed, False)
    
