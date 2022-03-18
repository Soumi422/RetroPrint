from sys import stdout
from time import sleep
from random import choice


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

colors = [
          bcolors.HEADER, bcolors.OKBLUE,
          bcolors.OKGREEN, bcolors.WARNING,
          bcolors.FAIL
        ]



def retro_print(text):
    last_color = None
    for l in text:
        if l == " ":
            typing_speed = 0
        else:
            typing_speed = 0.13

        new_color = choice(colors)
        while new_color == last_color:
            new_color = choice(colors)
        char = f"{new_color}{l}{bcolors.ENDC}"
        stdout.write(char)
        stdout.flush()
        last_color = new_color
        sleep(typing_speed)
    print("")


retro_print("Hello World!")