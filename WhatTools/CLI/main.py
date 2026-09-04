import pyautogui as pag
import pywhatkit
import time

class pyAuto:
    def __init__(self):
        self.version = 1.0
        self.format = "CLI"
        self.pyGui = pag
    def spamMessages(self,message,num=1,interval=0.5):
        try:
            time.sleep(3)
            for i in range(int(num)):
                self.pyGui.write(message);
                self.pyGui.press("ENTER")
                time.sleep(float(interval))    
            return 1
        except Exception as e:
            return e

    def sendMessagewithNumber(self,number,message):
        try:
            pywhatkit.sendwhatmsg_instantly(number,message)
            return 1
        except Exception as e:
            return e


    