# 도레미파솔라시도 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

#주파수 설정 (262Hz)
pwm = GPIO.PWM(BUZZER_PIN,  262)
pwm.start(10) # duty cycle (0~10)

#도레미파솔라시도'
melody = [392, 392, 440, 440, 392, 392, 330, 392, 392, 330, 330, 294, 392, 392, 440, 440, 392, 392, 330, 392, 330, 294, 330, 262] #솔솔라라솔솔미솔솔미미레솔솔라라솔솔미솔미레미도

try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)

finally:
    pwm.stop()
    GPIO.cleanup()

