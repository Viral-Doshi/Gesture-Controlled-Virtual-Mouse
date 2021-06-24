import cv2
import mediapipe as mp
import pyautogui
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

#def Find_Gesture():
# Updated

class Gest_Ctrl:
    gc_mode = 0
    cap = None
    def __init__(self):
        Gest_Ctrl.gc_mode = 1
        Gest_Ctrl.cap = cv2.VideoCapture(0)

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
                    # pos = self.calculate_position(results)
                    #self.move_mouse(pos)
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    cv2.imshow('MediaPipe Hands', image)
                if cv2.waitKey(5) & 0xFF == 27:
                    break
        Gest_Ctrl.cap.release()
        cv2.destroyAllWindows()

gc1 = Gest_Ctrl()
gc1.start()