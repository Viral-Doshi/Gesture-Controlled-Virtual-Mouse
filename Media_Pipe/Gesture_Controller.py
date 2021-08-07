import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import math
from enum import IntEnum
#system volume control
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from google.protobuf.json_format import MessageToDict

pyautogui.FAILSAFE = False

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

class Gest(IntEnum):
    FIST = 0
    PINKY = 1
    RING = 2
    MID = 4
    INDEX = 8
    THUMB = 16
    LAST3 = 7
    LAST4 = 15
    PALM = 31
    FIRST2 = 12
    V_GEST = 33
    TWO_FINGER_CLOSED = 34
    PINCH = 35



class Hand_Recog:
    finger = 0
    ori_gesture = Gest.PALM
    prev_gesture = Gest.PALM
    frame_count = 0
    
    def get_signed_dist(point):
        sign = -1
        if Gest_Ctrl.hand_result.landmark[point[0]].y < Gest_Ctrl.hand_result.landmark[point[1]].y:
            sign = 1
        dist = (Gest_Ctrl.hand_result.landmark[point[0]].x - Gest_Ctrl.hand_result.landmark[point[1]].x)**2
        dist += (Gest_Ctrl.hand_result.landmark[point[0]].y - Gest_Ctrl.hand_result.landmark[point[1]].y)**2
        dist = math.sqrt(dist)
        return dist*sign
    
    def get_dist(point):
        dist = (Gest_Ctrl.hand_result.landmark[point[0]].x - Gest_Ctrl.hand_result.landmark[point[1]].x)**2
        dist += (Gest_Ctrl.hand_result.landmark[point[0]].y - Gest_Ctrl.hand_result.landmark[point[1]].y)**2
        dist = math.sqrt(dist)
        return dist

    def render_finger_state(frame):
        points = [[8,5,0],[12,9,0],[16,13,0],[20,17,0]]
        label = ["dist_ratio :"]
        Hand_Recog.finger = 0
        Hand_Recog.finger = Hand_Recog.finger | 0 #thumb
        for idx,point in enumerate(points):
            
            dist = Hand_Recog.get_signed_dist(point[:2])
            dist2 = Hand_Recog.get_signed_dist(point[1:])
            
            try:
                ratio = round(dist/dist2,1)
                Hand_Recog.finger = Hand_Recog.finger << 1
                if ratio > 0.5 :
                    Hand_Recog.finger = Hand_Recog.finger | 1
                label[0] += str(ratio) + ','
            except:
                label[0] += "Division by 0"
        
        frame = cv2.putText(frame, label[0], (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
        #frame = cv2.putText(frame, fingstr, (10,150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
        
        return frame
    
    def get_gesture():
        current_gesture = Gest.PALM
        if Hand_Recog.finger in [Gest.LAST3,Gest.LAST4] and Hand_Recog.get_dist([8,4]) < 0.05:
            current_gesture = Gest.PINCH
            #print(Hand_Recog.get_dist([8,4]))
        elif Gest.FIRST2 == Hand_Recog.finger :
            point = [[8,12],[5,9]]
            dist1 = Hand_Recog.get_dist(point[0])
            dist2 = Hand_Recog.get_dist(point[1])
            ratio = dist1/dist2
            #print(ratio)
            if ratio > 1.7:
                #print('V Gesture')
                current_gesture = Gest.V_GEST
            else:
                #print("z : ",Mouse.get_dz([8,12]))
                if Mouse.get_dz([8,12]) < 0.1:
                    #print('2 fingers closed')
                    current_gesture =  Gest.TWO_FINGER_CLOSED
                else:
                    current_gesture =  Gest.MID
        else:
            current_gesture =  Hand_Recog.finger
        
        if current_gesture == Hand_Recog.prev_gesture:
            Hand_Recog.frame_count += 1
        else:
            Hand_Recog.frame_count = 0

        Hand_Recog.prev_gesture = current_gesture

        if Hand_Recog.frame_count > 4 :
            Hand_Recog.ori_gesture = current_gesture
        return Hand_Recog.ori_gesture

class Mouse:
    tx_old = 0
    ty_old = 0
    trial = True
    flag = False
    grabflag = False
    pinchstartycoord = None
    prevpinchlv = 0
    pinchlv = 0
    framecount = 0
    prev_hand = None

    def getpinchlv():
        dist = round((Mouse.pinchstartycoord - Gest_Ctrl.hand_result.landmark[8].y)*10,1)
        #print("pinch lv ",dist)
        return dist
    def changesystemvolume():
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        # Get current volume 
        currentVolumeLv = volume.GetMasterVolumeLevelScalar()
        #print("curr vol",currentVolumeLv)
        currentVolumeLv += Mouse.pinchlv/50.0
        if currentVolumeLv > 1.0:
            currentVolumeLv = 1.0
        elif currentVolumeLv < 0.0:
            currentVolumeLv = 0.0
        volume.SetMasterVolumeLevelScalar(currentVolumeLv, None)
        #print("changed vol",volume.GetMasterVolumeLevelScalar())
    
    def get_dz(point):
        return abs(Gest_Ctrl.hand_result.landmark[point[0]].z - Gest_Ctrl.hand_result.landmark[point[1]].z)
    
    def get_position():
        point = 9
        position = [Gest_Ctrl.hand_result.landmark[point].x ,Gest_Ctrl.hand_result.landmark[point].y]
        sx,sy = pyautogui.size()
        x_old,y_old = pyautogui.position()
        x = int(position[0]*sx)
        y = int(position[1]*sy)
        if Mouse.prev_hand is None:
            Mouse.prev_hand = x,y
        delta_x = x - Mouse.prev_hand[0]
        delta_y = y - Mouse.prev_hand[1]

        distsq = delta_x**2 + delta_y**2
        ratio = 1
        Mouse.prev_hand = [x,y]

        if distsq <= 25:
            ratio = 0
        elif distsq <= 900:
            ratio = 0.07 * (distsq ** (1/2))
        else:
            ratio = 2.1

        #if distsq < 25:
        #    ratio = 0
        #elif distsq <= 900:
        #    ratio = math.e ** (0.042 * math.sqrt(distsq)) - 0.9
        #else:
        #    ratio = 2.625

        x , y = x_old + delta_x*ratio , y_old + delta_y*ratio
        #print("r " , ratio)
        return (x,y)

    def move_mouse(gesture):
        
        x,y = Mouse.get_position()
        
        #flag reset
        if gesture != Gest.FIST and Mouse.grabflag:
            Mouse.grabflag = False
            pyautogui.mouseUp(button = "left")
        if gesture != Gest.PINCH and Mouse.pinchstartycoord is not None:
            print("pinch lv STOP " , Mouse.pinchlv)
            Mouse.pinchstartycoord = None
        
        #gesture
        if gesture == Gest.V_GEST:
            print('Move Mouse')
            Mouse.flag = True
            pyautogui.moveTo(x, y, duration = 0.1)
        elif gesture == Gest.FIST:
            print('Grab')
            if not Mouse.grabflag : 
                Mouse.grabflag = True
                pyautogui.mouseDown(button = "left")
            pyautogui.moveTo(x, y, duration = 0.1)
        elif gesture == Gest.MID and Mouse.flag:
            pyautogui.click()
            print('Left Click')
            Mouse.flag = False
        elif gesture == Gest.INDEX and Mouse.flag:
            pyautogui.click(button='right')
            print('Right Click')
            Mouse.flag = False
        elif gesture == Gest.TWO_FINGER_CLOSED and Mouse.flag:
            pyautogui.doubleClick()
            print('Double Click')
            Mouse.flag = False
        elif gesture == Gest.PINCH:
            if Mouse.pinchstartycoord is None:
                Mouse.pinchstartycoord = Gest_Ctrl.hand_result.landmark[8].y
                Mouse.pinchlv = 0
                Mouse.prevpinchlv = 0
                Mouse.framecount = 0
                print("pinch INIT")
            else:
                #hold final position for 5 frames to change volume
                if Mouse.framecount == 5:
                    Mouse.framecount = 0
                    Mouse.pinchlv = Mouse.prevpinchlv
                    Mouse.changesystemvolume()
                    print("pinch lv set to ", Mouse.pinchlv)
                lv =  Mouse.getpinchlv()
                if abs(Mouse.prevpinchlv - lv) < 0.3 :
                    Mouse.framecount += 1
                else:
                    Mouse.prevpinchlv = lv
                    Mouse.framecount = 0
                
            
        

class Gest_Ctrl:
    gc_mode = 0
    cap = None
    CAM_HEIGHT = None
    CAM_WIDTH = None
    hand_result = None

    def __init__(self):
        Gest_Ctrl.gc_mode = 1
        Gest_Ctrl.cap = cv2.VideoCapture(0)
        Gest_Ctrl.CAM_HEIGHT = Gest_Ctrl.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        Gest_Ctrl.CAM_WIDTH = Gest_Ctrl.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    
    def calculate_position(self):
        final_x = (Gest_Ctrl.hand_result.landmark[8].x +  Gest_Ctrl.hand_result.landmark[12].x)/2
        final_y = (Gest_Ctrl.hand_result.landmark[8].y +  Gest_Ctrl.hand_result.landmark[12].y)/2
        return [final_x,final_y]
    
    def ShowLocation(self):
        try:
            print(Gest_Ctrl.hand_result.landmark[12].z)
        except:
            print('Hi')
    
    def start(self):
        with mp_hands.Hands(max_num_hands = 2,min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
            while Gest_Ctrl.cap.isOpened() and Gest_Ctrl.gc_mode:
                success, image = Gest_Ctrl.cap.read()
                if not success:
                    print("Ignoring empty camera frame.")
                    continue
                
                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = hands.process(image)
                
                try:
                    
                    handedness_dict = MessageToDict(results.multi_handedness[0])
                    print(handedness_dict['classification'][0]['label'])
                except:
                    print("No hand Label")
                try:
                    handedness_dict = MessageToDict(results.multi_handedness[1])
                    print(handedness_dict['classification'][0]['label'])
                except:
                    print("No hand Label")
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                if results.multi_hand_landmarks:
                    Gest_Ctrl.hand_result = results.multi_hand_landmarks[0]
                    pos = self.calculate_position()
                    ##hand
                    image = Hand_Recog.render_finger_state(image)
                    gest_name = Hand_Recog.get_gesture()
                    Mouse.move_mouse(gest_name)
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                else:
                    Mouse.prev_hand = None
                cv2.imshow('MediaPipe Hands', image)
                if cv2.waitKey(5) & 0xFF == 13:
                    break
        Gest_Ctrl.cap.release()
        cv2.destroyAllWindows()

gc1 = Gest_Ctrl()
gc1.start()


