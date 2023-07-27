import time

from pynput.keyboard import Key, Listener

import LogWriter

class KeyboardListener:

    def on_press(key):
        print(key)

    def on_release(key):
        print(key)
        if key == Key.esc:
            return False
        elif key == Key.enter:
            LogWriter.toTxt(key, time.time())
