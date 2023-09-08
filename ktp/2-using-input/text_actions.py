import sys
import time


def animated_text(text: str, speed: int = 0.05):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        # pause
        time.sleep(speed)


def animated_text_with_input(text: str, speed: int = 0.05):
    animated_text(text, speed)
    return input()


def leave():
    sys.exit()
