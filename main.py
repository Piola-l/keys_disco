
import os
import time

lights = [0, 0, 1]
delay = 0.2

def lights_update():
    global lights
    lights = lights[1:] + [lights[0]]

while True:
    os.system(f"brightnessctl -d input5::numlock set {lights[0]}")
    os.system(f"brightnessctl -d input5::capslock set {lights[1]}")
    os.system(f"brightnessctl -d input5::scrolllock set {lights[2]}")

    time.sleep(delay)

    lights_update()
