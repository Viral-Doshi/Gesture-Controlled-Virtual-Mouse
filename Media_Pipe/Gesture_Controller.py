import cv2
import mediapipe as mp
import pyautogui
import math
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


class Hand_Recog:
    def render_vector(frame, hand_results):
        points = [[8,0],[12,0]]
        for point in points:
            s_cord = (int(hand_results.landmark[point[0]].x * Gest_Ctrl.CAM_WIDTH), int(hand_results.landmark[point[0]].y * Gest_Ctrl.CAM_HEIGHT))
            e_cord = (int(hand_results.landmark[point[1]].x * Gest_Ctrl.CAM_WIDTH), int(hand_results.landmark[point[1]].y * Gest_Ctrl.CAM_HEIGHT))
            frame = cv2.line(frame, s_cord, e_cord, (0,255,150), 9)
        return frame
    def render_finger_state(frame, hand_results):
        points = [[8,6,5],[12,10,9]]
        label = ["angle : ", "dist_ratio :"]
        for point in points:
            p1 = np.array([hand_results.landmark[point[0]].x,hand_results.landmark[point[0]].y])
            p2 = np.array([hand_results.landmark[point[1]].x,hand_results.landmark[point[1]].y])
            p3 = np.array([hand_results.landmark[point[2]].x,hand_results.landmark[point[2]].y])
            radian = np.arctan2(p3[1]-p2[1],p3[0]-p2[0]) - np.arctan2(p1[1]-p2[1],p1[0]-p2[0])
            angle = np.abs(radian*180.0/np.pi)
            if angle > 180.0:
                angle = 360.0-angle

            dist = (hand_results.landmark[point[0]].x - hand_results.landmark[point[2]].x)**2
            dist += (hand_results.landmark[point[0]].y - hand_results.landmark[point[2]].y)**2
            #dist += (hand_results.landmark[point[0]].z - hand_results.landmark[point[2]].z)**2
            dist = math.sqrt(dist)
            dist2 = (hand_results.landmark[point[2]].x - hand_results.landmark[0].x)**2
            dist2 += (hand_results.landmark[point[2]].y - hand_results.landmark[0].y)**2
            #dist2 += (hand_results.landmark[point[2]].z - hand_results.landmark[0].z)**2
            dist2 = math.sqrt(dist2)

            label[0] += str(round(angle,1)) + '  --  '
            label[1] += str(round(dist/dist2,1)) + '  --  '
        frame = cv2.putText(frame, label[0], (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, label[1], (10,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
        return frame




#def Find_Gesture():
# Updated

class Gest_Ctrl:
    gc_mode = 0
    cap = None
    CAM_HEIGHT = None
    CAM_WIDTH = None
    def __init__(self):
        Gest_Ctrl.gc_mode = 1
        Gest_Ctrl.cap = cv2.VideoCapture(0)
        Gest_Ctrl.CAM_HEIGHT = Gest_Ctrl.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        Gest_Ctrl.CAM_WIDTH = Gest_Ctrl.cap.get(cv2.CAP_PROP_FRAME_WIDTH)

    def move_mouse(self,position):        
        (sx,sy)=pyautogui.size()
        (mx_old,my_old) = pyautogui.position()
        tx = position[0]
        ty = position[1]           
        pyautogui.moveTo(int(sx*tx), int(sy*ty), duration = 0.1)


    def calculate_position(self,results):
        final_x = (results.multi_hand_landmarks[0].landmark[8].x +  results.multi_hand_landmarks[0].landmark[12].x)/2
        final_y = (results.multi_hand_landmarks[0].landmark[8].y +  results.multi_hand_landmarks[0].landmark[12].y)/2
        return [final_x,final_y]


    def ShowLocation(self, results):
        try:
            print(results.multi_hand_landmarks[0].landmark[12].z)
        except:
            print('Hi')


    def start(self):
        with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
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
                    #pos = self.calculate_position(results)
                    #self.move_mouse(pos)
                    ##hand
                    image = Hand_Recog.render_finger_state(image, results.multi_hand_landmarks[0])
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                cv2.imshow('MediaPipe Hands', image)
                if cv2.waitKey(5) & 0xFF == 13:
                    break
        Gest_Ctrl.cap.release()
        cv2.destroyAllWindows()

gc1 = Gest_Ctrl()
gc1.start()
