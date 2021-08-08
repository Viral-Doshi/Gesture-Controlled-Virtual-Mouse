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
import screen_brightness_control as sbcontrol

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
    PINCH_MAJOR = 35
    PINCH_MINOR = 36

class HLabel(IntEnum):
    MINOR = 0
    MAJOR = 1


class Hand_Recog:
    
    def __init__(self, hand_label):
        self.finger = 0
        self.ori_gesture = Gest.PALM
        self.prev_gesture = Gest.PALM
        self.frame_count = 0
        self.hand_result = None
        self.hand_label = hand_label
    
    def set_hand_result(self, hand_result):
        self.hand_result = hand_result

    def get_signed_dist(self, point):
        sign = -1
        if self.hand_result.landmark[point[0]].y < self.hand_result.landmark[point[1]].y:
            sign = 1
        dist = (self.hand_result.landmark[point[0]].x - self.hand_result.landmark[point[1]].x)**2
        dist += (self.hand_result.landmark[point[0]].y - self.hand_result.landmark[point[1]].y)**2
        dist = math.sqrt(dist)
        return dist*sign
    
    def get_dist(self, point):
        dist = (self.hand_result.landmark[point[0]].x - self.hand_result.landmark[point[1]].x)**2
        dist += (self.hand_result.landmark[point[0]].y - self.hand_result.landmark[point[1]].y)**2
        dist = math.sqrt(dist)
        return dist
    
    def get_dz(self,point):
        return abs(self.hand_result.landmark[point[0]].z - self.hand_result.landmark[point[1]].z)
    
    #def get_mxdist(point, hand_result): #manhaten x distance
    #    return hand_result.landmark[point[0]].x - hand_result.landmark[point[1]].x

    def render_finger_state(self, frame):
        if self.hand_result == None:
            return frame

        points = [[8,5,0],[12,9,0],[16,13,0],[20,17,0]]
        label = ["dist_ratio :"]
        self.finger = 0
        self.finger = self.finger | 0 #thumb
        for idx,point in enumerate(points):
            
            dist = self.get_signed_dist(point[:2])
            dist2 = self.get_signed_dist(point[1:])
            
            try:
                ratio = round(dist/dist2,1)
                self.finger = self.finger << 1
                if ratio > 0.5 :
                    self.finger = self.finger | 1
                label[0] += str(ratio) + ','
            except:
                label[0] += "Division by 0"
        
        frame = cv2.putText(frame, label[0], (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
        #frame = cv2.putText(frame, fingstr, (10,150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
        
        return frame
    
    def get_hand():
        pass
    
    def get_gesture(self):
        if self.hand_result == None:
            return Gest.PALM

        current_gesture = Gest.PALM
        if self.finger in [Gest.LAST3,Gest.LAST4] and self.get_dist([8,4]) < 0.05:
            if self.hand_label == HLabel.MINOR :
                current_gesture = Gest.PINCH_MINOR
            else:
                current_gesture = Gest.PINCH_MAJOR
            #print(Hand_Recog.get_dist([8,4]))
        elif Gest.FIRST2 == self.finger :
            point = [[8,12],[5,9]]
            dist1 = self.get_dist(point[0])
            dist2 = self.get_dist(point[1])
            ratio = dist1/dist2
            #print(ratio)
            if ratio > 1.7:
                #print('V Gesture')
                current_gesture = Gest.V_GEST
            else:
                #print("z : ",Mouse.get_dz([8,12]))
                if self.get_dz([8,12]) < 0.1:
                    #print('2 fingers closed')
                    current_gesture =  Gest.TWO_FINGER_CLOSED
                else:
                    current_gesture =  Gest.MID
            
        else:
            current_gesture =  self.finger
        
        if current_gesture == self.prev_gesture:
            self.frame_count += 1
        else:
            self.frame_count = 0

        self.prev_gesture = current_gesture

        if self.frame_count > 4 :
            self.ori_gesture = current_gesture
        return self.ori_gesture

class Mouse:
    tx_old = 0
    ty_old = 0
    trial = True
    flag = False
    grabflag = False
    pinchstartxcoord = None
    pinchstartycoord = None
    pinchdirectionflag = None
    prevpinchlv = 0
    pinchlv = 0
    framecount = 0
    prev_hand = None
    
    def getpinchylv(hand_result):
        dist = round((Mouse.pinchstartycoord - hand_result.landmark[8].y)*10,1)
        #print("pinch lv ",dist)
        return dist
    def getpinchxlv(hand_result):
        dist = round((hand_result.landmark[8].x - Mouse.pinchstartxcoord)*10,1)
        #print("pinch lv ",dist)
        return dist
    
    def changesystembrightness():
        #print('bright change')
        currentBrightnessLv = sbcontrol.get_brightness()/100.0
        currentBrightnessLv += Mouse.pinchlv/50.0
        if currentBrightnessLv > 1.0:
            currentBrightnessLv = 1.0
        elif currentBrightnessLv < 0.0:
            currentBrightnessLv = 0.0
        
        sbcontrol.fade_brightness(int(100*currentBrightnessLv) , start = sbcontrol.get_brightness())
    
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
    
    def get_position(hand_result):
        point = 9
        position = [hand_result.landmark[point].x ,hand_result.landmark[point].y]
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

    def handle_controls(gesture, hand_result):
        
        x,y = None,None
        if gesture != Gest.PALM :
            x,y = Mouse.get_position(hand_result)
        
        #flag reset
        if gesture != Gest.FIST and Mouse.grabflag:
            Mouse.grabflag = False
            pyautogui.mouseUp(button = "left")
        if gesture != Gest.PINCH_MAJOR and Mouse.pinchstartycoord is not None:
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
        elif gesture == Gest.PINKY:
            print('pinky ksndkskk')
        elif gesture == Gest.PINCH_MINOR:
            print('PINCH MINOR')
        elif gesture == Gest.PINCH_MAJOR:
            if Mouse.pinchstartycoord is None:
                Mouse.pinchstartxcoord = hand_result.landmark[8].x
                Mouse.pinchstartycoord = hand_result.landmark[8].y
                Mouse.pinchlv = 0
                Mouse.prevpinchlv = 0
                Mouse.framecount = 0
                print("pinch INIT")
            else:
                #hold final position for 5 frames to change volume
                if Mouse.framecount == 5:
                    Mouse.framecount = 0
                    Mouse.pinchlv = Mouse.prevpinchlv
                    if Mouse.pinchdirectionflag == True:
                        Mouse.changesystembrightness() #x
                    elif Mouse.pinchdirectionflag == False:
                        Mouse.changesystemvolume() #y
                    
                    print("pinch lv set to ", Mouse.pinchlv)
                lvx =  Mouse.getpinchxlv(hand_result)
                lvy =  Mouse.getpinchylv(hand_result)
                
                if abs(lvy) > abs(lvx) and abs(lvy) > 0.3:
                    #lvy
                    Mouse.pinchdirectionflag = False
                    if abs(Mouse.prevpinchlv - lvy) < 0.3 :
                        Mouse.framecount += 1
                    else:
                        Mouse.prevpinchlv = lvy
                        Mouse.framecount = 0
                elif abs(lvx) > 0.3:
                    #lvx
                    Mouse.pinchdirectionflag = True
                    if abs(Mouse.prevpinchlv - lvx) < 0.3 :
                        Mouse.framecount += 1
                    else:
                        Mouse.prevpinchlv = lvx
                        Mouse.framecount = 0
            
        

class Gest_Ctrl:
    gc_mode = 0
    cap = None
    CAM_HEIGHT = None
    CAM_WIDTH = None
    hr_major = None #right
    hr_minor = None #left
    dom_hand = True # right is dom

    def __init__(self):
        Gest_Ctrl.gc_mode = 1
        Gest_Ctrl.cap = cv2.VideoCapture(0)
        Gest_Ctrl.CAM_HEIGHT = Gest_Ctrl.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        Gest_Ctrl.CAM_WIDTH = Gest_Ctrl.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    
    def calculate_position(self):
        final_x = (Gest_Ctrl.hr_major.landmark[8].x +  Gest_Ctrl.hr_major.landmark[12].x)/2
        final_y = (Gest_Ctrl.hr_major.landmark[8].y +  Gest_Ctrl.hr_major.landmark[12].y)/2
        return [final_x,final_y]
    
    def classify_hands(results):
        left , right = None,None
        try:
            handedness_dict = MessageToDict(results.multi_handedness[0])
            if handedness_dict['classification'][0]['label'] == 'Right':
                right = results.multi_hand_landmarks[0]
            else :
                left = results.multi_hand_landmarks[0]
        except:
            pass

        try:
            handedness_dict = MessageToDict(results.multi_handedness[1])
            if handedness_dict['classification'][0]['label'] == 'Right':
                right = results.multi_hand_landmarks[1]
            else :
                left = results.multi_hand_landmarks[1]
        except:
            pass
        
        if Gest_Ctrl.dom_hand == True:
            Gest_Ctrl.hr_major = right
            Gest_Ctrl.hr_minor = left
        else :
            Gest_Ctrl.hr_major = left
            Gest_Ctrl.hr_minor = right

    def start(self):

        handmajor = Hand_Recog(HLabel.MAJOR)
        handminor = Hand_Recog(HLabel.MINOR)

        with mp_hands.Hands(max_num_hands = 2,min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
            while Gest_Ctrl.cap.isOpened() and Gest_Ctrl.gc_mode:
                success, image = Gest_Ctrl.cap.read()
                if not success:
                    print("Ignoring empty camera frame.")
                    continue
                
                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = hands.process(image)
                
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                if results.multi_hand_landmarks:
                    
                    Gest_Ctrl.classify_hands(results)
                    #pos = self.calculate_position()
                    handmajor.set_hand_result(Gest_Ctrl.hr_major)
                    handminor.set_hand_result(Gest_Ctrl.hr_minor)

                    ##hand
                    image = handmajor.render_finger_state(image)
                    image = handminor.render_finger_state(image)
                    gest_name = handminor.get_gesture()

                    if gest_name == Gest.PINCH_MINOR:
                        Mouse.handle_controls(gest_name, handminor.hand_result)
                    else:
                        gest_name = handmajor.get_gesture()
                        Mouse.handle_controls(gest_name, handmajor.hand_result)
                    #image = Hand_Recog.render_finger_state(image)
                    #gest_name = Hand_Recog.get_gesture()
                    
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


