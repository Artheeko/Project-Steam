import machine
import neopixel
import dashboard

np = neopixel.NeoPixel(machine.Pin(15), 8)

test = dashboard
if dashboard.x:
    np[0] = [0, 255, 0]
    np.write()
else:
    np[0] = [255, 0, 0]
    np.write()