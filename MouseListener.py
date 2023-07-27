import pynput, time
from pynput import keyboard
from LogWriter import toTxt
def on_click(x, y, button, pressed):
    if button == pynput.mouse.Button.left:
        toTxt("click", time.time())
    elif button == pynput.mouse.Button.right:
        return False





