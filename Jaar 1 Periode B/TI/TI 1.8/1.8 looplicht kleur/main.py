import time
import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(15), 8)
print(type(np))

while True:
    for i in range(len(np)):
        np[i] = [255, 0, 0]
        time.sleep(0.4)
        np.write()
    for i in range(len(np)):
        np[i] = [0, 255, 0]
        time.sleep(0.4)
        np.write()
    for i in range(len(np)):
        np[i] = [0, 0, 255]
        time.sleep(0.4)
        np.write()

# np[0] = [255, 0, 0]
# np[1] = [255, 0, 0]
# np[2] = [255, 0, 0]
# np[3] = [255, 0, 0]
# np[4] = [255, 0, 0]
# np[5] = [255, 0, 0]
# np[6] = [255, 0, 0]
# np[7] = [255, 0, 0]

# time.sleep(1)

"Zwart is dan [ 0, 0, 0 ]"
"rood is [ 255, 0, 0 ] "
"geel is [ 255, 255, 0 ] (rood + groen)"
"wit is [ 255, 255, 255 ]."
