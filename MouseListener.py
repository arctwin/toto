import pynput, time
from pynput import keyboard

def on_click(x, y, button, pressed):
    if button == pynput.mouse.Button.left:
        print('click  '+ str(time.time()))
    elif button == pynput.mouse.Button.right:
        return False





