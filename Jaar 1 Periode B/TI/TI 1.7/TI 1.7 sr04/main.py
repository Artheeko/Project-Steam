from machine import Pin
import time

led_pins = [
    Pin(0, Pin.OUT),
    Pin(1, Pin.OUT),
    Pin(2, Pin.OUT),
    Pin(3, Pin.OUT),
    Pin(4, Pin.OUT)
]

trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)

def measure_distance():
    """
        Meet de afstand met de SR04
    """

    signaalaan = 0
    signaaluit = 0
    trigger.low()
    time.sleep_us(2)
    trigger.high()
    time.sleep_us(5)
    trigger.low()

    while echo.value() == 0:
        signaaluit = time.ticks_us()
    while echo.value() == 1:
        signaalaan = time.ticks_us()

    timepassed = signaalaan - signaaluit
    distance = (timepassed * 0.0343) / 2

    return distance

def leds(value):
    for led in led_pins:
        if value % 2 == 1:
            led.value(1)
        else:
            led.value(0)
        value = value // 2
    time.sleep(0.1)

def display_distance(distance):
    """
        Laat de afstand d.m.v. de leds zien.
        1 led =  10 cm
        2 leds = 15 cm
        3 leds = 20 cm
        4 leds = 25 cm
        5 leds = 30 cm
    """


    if distance <= 10:
        leds(1)
    elif distance <= 15:
        leds(3)
    elif distance <= 20:
        leds(7)
    elif distance <= 25:
        leds(15)
    elif distance <= 30:
        leds(31)


while True:
    distance = measure_distance()
    display_distance(distance)
    time.sleep_ms(50)