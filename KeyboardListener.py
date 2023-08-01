import time

from pynput.keyboard import Key

import ReportUtil

def on_press(key):
    pass

def on_release(key):
    if key == Key.esc:
        return False
    elif key == Key.enter:
        return False

