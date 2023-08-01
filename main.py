import pynput
import KeyboardListener
import MouseListener


if __name__ == '__main__':
    listener1 = pynput.keyboard.Listener(on_press=KeyboardListener.on_press,on_release=KeyboardListener.on_release)
    listener2 = pynput.mouse.Listener(on_click=MouseListener.on_click)
    listener1.start()
    listener2.start()
    listener1.join()
    listener2.join()