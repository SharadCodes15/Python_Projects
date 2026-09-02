import pyautogui as pag
import time

class pyAuto:
    def __init__(self):
        self.version = 1.0
        self.format = "CLI"
        self.pyGui = pag
    def spamMessages(self,message,num=1,interval=0.5):
        try:
            self.pyGui.write(message);
            self.pyGui.press("ENTER")
            time.sleep(interval)    
            return 1
        except Exception as e:
            return e

    