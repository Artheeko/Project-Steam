from machine import Pin
import time

servo_pin = Pin(21, Pin.OUT)


def pulse(delay1, delay2 ):
    """ kopier hier je implementatie van de pulse functie """
    # delay1 = lowtime
    # delay2 = hightime

    servo_pin.value(1)
    time.sleep_ms(delay1)
    servo_pin.value(0)
    time.sleep_ms(delay2)

    return delay1, delay2

# hightime = x*(2/180) + 0.5            x = position in graden
# lowtime = 20 - hightime
# 20 = ms(50hz)
def servo_pulse(position):
    pulse(20, 0.5 )
    position * (2/180) + 0.5
    time.sleep_ms(20)
    pulse(0.5, 20)

    """
    Send a servo pulse on the specified gpio pin
    that causes the servo to turn to the specified position, and
    then waits 20 ms.

    The position must be in the range 0 .. 100.
    For this range, the pulse must be in the range 0.5 ms .. 2.5 ms

    Before this function is called,
    the gpio pin must be configured as output.
    """

while True:
    for i in range(0, 100, 1):
        servo_pulse(i)
    for i in range(100, 0, -1):
        servo_pulse(i)