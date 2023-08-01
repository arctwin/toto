from threading import Thread

import pynput, time
from pynput import keyboard

import ReportUtil
# # from ReportUtil import toTxt
#






def on_click(x, y, button, pressed):
    if button == pynput.mouse.Button.left and pressed:
        print(time.time()-ReportUtil.currentTime)
        ReportUtil.currentTime= time.time()
        # ReportUtil.toLine("click",ReportUtil.currentTime)
    elif button == pynput.mouse.Button.right:
        return False
