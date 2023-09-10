#pulse, tatataa en piepen
from machine import Pin
import time


def pulse(pin, high_time, low_time):
    pin.value(1)
    time.sleep(high_time)
    pin.value(0)
    time.sleep(low_time)

gpio_pin = Pin(20, Pin.OUT)

while True:
    pulse(gpio_pin, 0.5, 0.33)
    pulse(gpio_pin, 0.5, 0.33)
    pulse(gpio_pin, 5, 0.33)
