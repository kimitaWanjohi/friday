import sys
from time import sleep

def typing(words):
    print("Friday: ", end="", flush=True)
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()