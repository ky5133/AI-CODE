import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

print("Hand Tracking has started.... press 'm' to exit the program")

def detect_gesture(hand_landmarks):
    landmarks=hand_landmarks.landmark
    tip_ids=[4,8,12,16,20]
    pip_ids=[2,6,10,14,18]
    extended_fingers=0

    if abs(landmarks[tip_ids[0]].x-landmarks[pip_ids[0]].x)<0.04:
        extended_fingers+=1

    for i in range(1,5):
        if landmarks[tip_ids[i]].y<landmarks[pip_ids[i]].y:
            extended_fingers+=1

    if extended_fingers>=4:
        return "Open Hand"
    elif extended_fingers<=1:
        return " Closed Fist"
    else:
        return "Partial"

while True:
    ret,frame=cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    frame=cv2.flip(frame,1)
    h, w,_=frame.shape
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=hands.process(rgb_frame)
    gesture="No Hand Detected"

    if results.multi_hand_landmarks and results.multi_handedness:
        
        for  idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
         hand_label=results.multi_handedness[idx].classification[0].label
         gesture=detect_gesture(hand_landmarks)
         mp_draw.draw_landmarks(frame,hand_landmarks,mp_hands.HAND_CONNECTIONS)

         fingertips_ids=[4,8,12,16,20]
         for tip_id in fingertips_ids:
             lm=hand_landmarks.landmark[tip_id]
             x,y=int(lm.x*w),int(lm.y*h)
             cv2.circle(frame,(x,y),10,(0,255,255),cv2.FILLED)
             cv2.putText(frame,f'Gesture: {gesture}',(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

             status_color=(0,255,0) if gesture==("Open Hand","Closed Fist") else (0,0,255)
             cv2.putText(frame,f'Status: {gesture}',(10,70),cv2.FONT_HERSHEY_SIMPLEX,1,status_color,2)
             cv2.imshow("Hand Detection",frame)
             if cv2.waitKey(1) & 0xFF==ord('m'):
                    break
cap.release()
cv2.destroyAllWindows()             




    