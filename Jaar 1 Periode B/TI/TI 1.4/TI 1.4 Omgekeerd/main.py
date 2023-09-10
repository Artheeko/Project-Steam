from machine import ADC, PWM, Pin
import time

led = PWM(Pin(20))
led.freq(1000)

adc = ADC(Pin(26))

def led_brightness(value):
    """ Zet de led intensiteit.
    Waarde tussen de 0 en 65535 """

    led.duty_u16(value)

#door een - toe te voegen voor 'adc_value' werkt de potmeter omgekeerd
# while True:
#     adc_value = adc.read_u16()
#     led_brightness(-adc_value)
#     time.sleep(0.01)

while True:
    adc_value = adc.read_u16()
    led_brightness(65535-adc_value)
    time.sleep(0.01)