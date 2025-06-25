import RPi.GPIO as GPIO
import time
from config import RADAR_GPIO_PIN

GPIO.setmode(GPIO.BCM)
GPIO.setup(RADAR_GPIO_PIN, GPIO.IN)

def measure_speed(sample_time=1.0):
    pulse_count = 0
    start = time.time()

    while time.time() - start < sample_time:
        if GPIO.input(RADAR_GPIO_PIN):
            pulse_count += 1
            while GPIO.input(RADAR_GPIO_PIN):  # Debounce
                pass

    freq = pulse_count / sample_time
    speed_mph = freq * 0.062  # HB100 approximation
    return round(speed_mph, 2)
