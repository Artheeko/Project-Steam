from machine import ADC, PWM, Pin
import time

led = Pin(20, Pin.OUT)
adc = ADC(Pin(26))

def pulse(pin, high_time, low_time):

    pin.value(1)
    time.sleep(high_time)
    pin.value(0)
    time.sleep(low_time)

    # implementeer deze functie

while True:
    adc_value = adc.read_u16()
    tijd = adc_value / 65535
    pulse(led, tijd, tijd)
    time.sleep(0.01)

# while True:
#     adc_value = adc.read_u16()
#     time.sleep(0.01)
#     if adc.read_u16() == 0:
#         pulse(led, 1, 1)
#     if adc.read_u16() == 65535:
#         pulse(led, 0.5, 0.5)
# ik kon denk ik ook een for loop gebruiken maar dit werkt.