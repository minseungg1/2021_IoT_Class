import RPi.GPIO as GPIO
import time

LED_PIN = 26
SWITCH_PIN = 18

LED_PIN2 = 19
SWITCH_PIN2 = 15

LED_PIN3 = 13
SWITCH_PIN3 = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        GPIO.output(LED_PIN, val)
        val = GPIO.input(SWITCH_PIN2)
        print(val)
        GPIO.output(LED_PIN2, val)
        val = GPIO.input(SWITCH_PIN3)
        print(val)
        GPIO.output(LED_PIN3, val)
        time.sleep(0.1)
finally:
    GPIO.cleanup()
    print('cleanup and exit')
