import sys
import subprocess
import time

mode: int = 1
delay: float = 0.2

lights: list[int] = [0, 0, 1]

def toggle_lights(lights: list[int]):
    _ = subprocess.run(
        ["brightnessctl", "-d", "input5::numlock", "set", str(lights[0])],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    _ = subprocess.run(
        ["brightnessctl", "-d", "input5::capslock", "set", str(lights[1])],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    _ = subprocess.run(
        ["brightnessctl", "-d", "input5::scrolllock", "set", str(lights[2])],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


def mode_1():
    global lights

    while True:
        toggle_lights(lights)

        time.sleep(delay)

        lights = lights[1:] + [lights[0]]

def mode_2():
    global lights
    # right true left false
    direction = True 

    while True:
        toggle_lights(lights)

        time.sleep(delay)

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

        time.sleep(delay)


def parse_arguments(args: list[str]) -> None:
    global mode, delay

    for i in range(len(args)):
        n = args[i]

        # Set mode
        if n in ["-m", "--mode"]:
            try:
                mode = int(args[i+1])
            except IndexError:
                print("Not enough arguments!")
                sys.exit()
            except ValueError:
                print("Type error! Please enter an integer.")
                sys.exit()

        # Delay
        elif n in ["-d", "--delay"]:
            try:
                delay = float(args[i+1])
            except IndexError:
                print("Not enough arguments!")
                sys.exit()
            except ValueError:
                print("Type error! Please enter a float or an integer.")

        # Help
        elif n in ["-h", "--help"]:
            print("""
                  -m, --mode <mode> : set disco mode (1..3), default: 1
                  -d, --delay <seconds> : set next iteration wait delay, default: 0.2
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
