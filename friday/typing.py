import sys
from time import sleep

def typing(words):
    print("Friday: ", end="" if words.endswith("?") else "\n")
    for char in words:
        sleep(0.5)
        sys.stdout.write(char)
        sys.stdout.flush()