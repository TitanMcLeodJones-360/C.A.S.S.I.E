import sys
import time

def typewriter_effect(text, delay=0.05):
    """
    Prints text with a typewriter effect.
    :param text: The text to display.
    :param delay: The delay between each character.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Newline at the end
