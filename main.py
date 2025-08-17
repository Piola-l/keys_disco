import sys
import os
import time

mode: int = 1
DELAY: float = 0.2

lights: list[int] = [0, 0, 1]

def toggle_lights(lights: list[int]):
    _ = os.system(f"brightnessctl -d input5::numlock set {lights[0]} > /dev/null 2>&1")
    _ = os.system(f"brightnessctl -d input5::capslock set {lights[1]} > /dev/null 2>&1")
    _ = os.system(f"brightnessctl -d input5::scrolllock set {lights[2]} > /dev/null 2>&1")

def mode_1():
    global lights

    while True:
        toggle_lights(lights)

        time.sleep(DELAY)

        lights = lights[1:] + [lights[0]]

def mode_2():
    global lights
    # right true left false
    direction = True 

    while True:
        toggle_lights(lights)

        time.sleep(DELAY)

        if lights == [1, 0, 0]:
            direction = True
        elif lights == [0, 0, 1]:
            direction = False

        if direction:
            lights = [lights[-1]] + lights[:-1]
        else:
            lights = lights[1:] + [lights[0]]

def mode_3():
    global lights
    lights = [0, 1, 0]
    
    while True:
        for i in range(len(lights)):
            lights[i] = 1-lights[i]
        
        toggle_lights(lights)

        time.sleep(DELAY)


def parse_arguments(args: list[str]) -> None:
    global mode

    for i in range(len(args)):
        n = args[i]

        #  Set mode
        if n in ["-m", "--mode"]:
            try:
                mode = int(args[i+1])
            except IndexError:
                print("Not enough arguments!")
                sys.exit()
            except ValueError:
                print("Type error! Pleas enter an integer.")
                sys.exit()

        elif n in ["-h", "--help"]:
            print("""
                  -m, --mode <mode> : set disco mode (1..3)
                  -h, --help        : print this message
                  """)
            sys.exit()        

if __name__ == "__main__":
    args = sys.argv

    if len(args) > 1:
        parse_arguments(args)        

    match mode:
        case 1:
            mode_1()
        case 2:
            mode_2()
        case 3:
            mode_3()
        case _:
            print("Mode does not exist!")
            sys.exit()
