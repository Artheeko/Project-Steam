from machine import Pin
import time

gpio_pin = Pin(20, Pin.OUT)

#
# def pulse(pin, high_time, low_time):
#     pin.value(1)
#     time.sleep(high_time)
#     pin.value(0)
#     time.sleep(low_time)


def morse(pin, dot_length, text):
    for i in text:
        if i == '.':
            pin.value(0)
            time.sleep(dot_length)
            pin.value(1)
            time.sleep(dot_length)
            pin.value(0)
            time.sleep(dot_length)
        else:
            pin.value(0)
            time.sleep(dot_length)
        if i == "-":
            pin.value(0)
            time.sleep(dot_length)
            pin.value(1)
            time.sleep(dot_length)
            pin.value(1)
            time.sleep(dot_length)
            pin.value(1)
            time.sleep(dot_length)
            pin.value(0)
            time.sleep(dot_length)

morse(gpio_pin, 0.2, ".--. -.-- - .... --- -.")