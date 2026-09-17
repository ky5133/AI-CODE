import cv2 ,time,pyautogui
import mediapipe as mp
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

SCROLL_SPEED=300
SCROLL_DELAY=1
CAM_WIDTH,CAM_HEIGHT=640,480

def detect(landmarks,handedness):
    fingers=[]
    tips=[mp_hands.HandLandmark.THUMB_TIP,mp_hands.HandLandmark.INDEX_FINGER_TIP,mp_hands.HandLandmark.MIDDLE_FINGER_TIP,mp_hands.HandLandmark.RING_FINGER_TIP,mp_hands.HandLandmark.PINKY_TIP]
    for tip in tips:
        if landmarks.landmark[tip].y<landmarks.landmark[tip-2].y:
            fingers.append(1)

        thumb_tip_x=landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        thumb_ip=landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    if (handedness=="Right"and thumb_tip_x.x>thumb_ip.x) or (handedness=="Left" and thumb_tip_x.x<thumb_ip.x):
            fingers.append(1)

    return "scroll up" if sum (fingers)==5 else "scroll down" if sum(fingers)==0 else "scroll down"
cap=cv2.VideoCapture(0)
cap.set(3,CAM_WIDTH)
cap.set(4,CAM_HEIGHT)
last_scroll=p_time=0
print("Gesture scroll control started open palm is scroll up and closed palm is scroll down" \
        "Press 'q' to exit")

while cap.isOpened():
     ok,img=cap.read()
     if not ok:
        break
     img=cv2.flip(cv2.cvtColor(img,cv2.COLOR_BGR2RGB),1)
     results=hands.process(img)
     gesture,handedness="none","unknown"

     if results.multi_hand_landmarks and results.multi_handedness:
          for hand,handedness_info in zip(results.multi_hand_landmarks,results.multi_handedness):
               handedness=mp_draw.draw_landmarks(img,hand,mp_hands.HAND_CONNECTIONS)
               gesture=detect(hand,handedness_info.classification[0].label)
               handedness=handedness_info.classification[0].label

               if time.time()-last_scroll>SCROLL_DELAY:
                    if gesture=="scroll up":
                        pyautogui.scroll(SCROLL_SPEED)
                        last_scroll=time.time()
                    elif gesture=="scroll down":
                        pyautogui.scroll(-SCROLL_SPEED)
                        last_scroll=time.time()

     fps=1/(time.time()-p_time) if (time.time()-p_time)>0 else 0
     p_time=time.time()
     cv2.putText(img,f"FPS:{int(fps)},hand:{handedness},Gesture:{gesture})",(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
     cv2.imshow("Gesture Scroll Control",cv2.cvtColor(img,cv2.COLOR_RGB2BGR))
     if cv2.waitKey(1) & 0xFF==ord('q'):
            break


cap.release()
cv2.destroyAllWindows()

