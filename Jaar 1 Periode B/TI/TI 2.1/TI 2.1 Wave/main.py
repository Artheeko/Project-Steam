from machine import Pin
import time


servo_pin = Pin(21, Pin.OUT)

def pulse(delay1, delay2 ):
    """ kopieer hier je implementatie van de pulse functie """

    servo_pin.high()
    time.sleep_ms(delay1)
    servo_pin.low()
    time.sleep_ms(delay2)

    return delay1, delay2

def servo_pulse(position):
    test = position * (2 / 180) + 0.5
    pulse(test, 20)


    # pulse(1.5, 20)
    # pulse(2.5, 20)

    # 0 = 0?
    # 50 = 90?
    # 100 = 180?

    """
    Send a servo pulse on the specified gpio pin
    that causes the servo to turn to the specified position, and
    then waits 20 ms.

    The position must be in the range 0 .. 100.
    For this range, the pulse must be in the range 0.5 ms .. 2.5 ms

    Before this function is called,
    the gpio pin must be configured as output.
     
    Leo: Je moet pulse maar 1 keer an roepen per servo pulse.  
    Met een totale lengte van 20ms en een. High time die aan geeft welke positie.
    
    """

# In de span van 20ms
# 0.5 = links	  0 graden
# 1.5 = midden	 90 graden
# 2.5 = rechts	180 graden


while True:
    for i in range(0, 100, 1):
        servo_pulse(i)
    for i in range(100, 0, -1):
        servo_pulse(i)

    """
20ms (50hz)
Het stuursignaal is een puls die om de (ongeveer) 20 milliseconden (dus 50 keer per seconde) naar de servo gestuurd moet worden. 
Die pulsen moeten tussen de 0.5 en 2.5 milliseconden lang zijn. 
Als de pulsen 0.5 ms lang zijn draait de servo zijn asje naar de ene uiterste stand, bij 2.5 ms draait hij naar de andere uiterste stand. 
Meestal is het verschil tussen die twee standen 180 graden.
    """
