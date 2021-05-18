import threading
import time
import Gesture_Controller
import Voice_Controller

gc_mode=0 
#variable to controll gc 
#gc_mode=0 => OFF
#gc_mode=1 => Cursor Mode
#gc_mode=2 => presentation mode

gc = Gesture_Controller.Gest_Ctrl()

#Thread sub class for voice controller
class vcThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)   
    def run(self):
        try:
            vc.init()
        except:
            print("Gesture Controller Initialization Failed")
        try:
            vc.start()
        except:
            print("error while running gesture controller")

#Thread sub class for gesture controller
class gcThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        try:
            gc.init()
        except:
            print("Gesture Controller Initialization Failed")
        try:
            gc.start()
        except:
            print("error while running gesture controller")

gt=gcThread()

gt.start()

gt.join()