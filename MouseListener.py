
import pynput, time


import ReportUtil

def on_click(x, y, button, pressed):
    if button == pynput.mouse.Button.left and pressed:
        print(time.time()-ReportUtil.currentTime)
        ReportUtil.currentTime= time.time()
        # ReportUtil.toLine("click",ReportUtil.currentTime)
    elif button == pynput.mouse.Button.right:
        return False
