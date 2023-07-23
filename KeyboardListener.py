from pynput.keyboard import Key, Listener

from logWriter import toTxt


def on_press(key):
    print(key)

def on_release(key):
    print(key)
    if key == Key.esc:
        # 停止监听
        return False
    elif key == Key.enter:
        toTxt("")

