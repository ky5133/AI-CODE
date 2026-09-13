import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc


Hands = mp.solutions.hands
hands = Hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
drawing = mp.solutions.drawing_utils
TH, IX = Hands.HandLandmark.THUMB_TIP, Hands.HandLandmark.INDEX_FINGER_TIP


try:
    dev = AudioUtilities.GetDefaultOutputDevice() if hasattr(AudioUtilities, "GetDefaultOutputDevice") else AudioUtilities.GetSpeakers()
    volctl = dev.EndpointVolume.QueryInterface(IAudioEndpointVolume)
    minv, maxv = volctl.GetVolumeRange()[:2]
except Exception as e:
    print(f"Error initializing audio device: {e}")
    minv, maxv = -65.25, 0.0


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()


WIN = "Hand Gesture Control"
cv2.namedWindow(WIN, cv2.WINDOW_NORMAL)


while True:
    ok, img = cap.read()
    if not ok:
        break
        
    img = cv2.flip(img, 1)
    h, w = img.shape[:2]
    res = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    
    if res.multi_hand_landmarks and res.multi_handedness:
        for i, hand in enumerate(res.multi_hand_landmarks):
            label = res.multi_handedness[i].classification[0].label
            drawing.draw_landmarks(img, hand, Hands.HAND_CONNECTIONS)
            lm = hand.landmark
            tp = (int(lm[TH].x * w), int(lm[TH].y * h))
            ip = (int(lm[IX].x * w), int(lm[IX].y * h))
            
            cv2.circle(img, tp, 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, ip, 10, (0, 255, 0), cv2.FILLED)
            cv2.line(img, tp, ip, (255, 0, 0), 3)
            dist = np.linalg.norm(np.array(tp) - np.array(ip))

            if label == "Left":
                
                v = np.interp(dist, [30, 300], [0.0, 1.0])
                try:
                    volctl.SetMasterVolumeLevelScalar(v, None)
                except Exception as e:
                    print(f"Error setting volume: {e}")
                
                bar = int(np.interp(dist, [30, 300], [400, 150]))
                pct = int(np.interp(dist, [30, 300], [0, 100]))
                cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
                cv2.rectangle(img, (50, bar), (85, 400), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f"{pct}%", (40, 430), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

            elif label == "Right":
                b = np.interp(dist, [30, 300], [0, 100])
                try:
                    sbc.set_brightness(int(b))
                except Exception as e:
                    print(f"Error setting brightness: {e}")
                
                bar = int(np.interp(dist, [30, 300], [400, 150]))
                pct = int(np.interp(dist, [30, 300], [0, 100]))
                cv2.rectangle(img, (w - 85, 150), (w - 50, 400), (255, 0, 0), 3)
                cv2.rectangle(img, (w - 85, bar), (w - 50, 400), (255, 0, 0), cv2.FILLED)
                cv2.putText(img, f"{pct}%", (w - 120, 430), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

   
    cv2.imshow(WIN, img)

  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    try:
        if cv2.getWindowProperty(WIN, cv2.WND_PROP_VISIBLE) < 1:
            break
    except cv2.error:
        break


cap.release()
cv2.destroyAllWindows()
