import cv2
import mediapipe as mp
import streamlit as st
import tempfile
import time
import PoseModule as pm
import Hand_Tracking_Module_ as hd
import math

cam = cv2.VideoCapture(0)

st.title("Video Capture")

framePlaceholder = st.empty()


cTime = 0
pTime = 0
detector = pm.poseDetector()
handDetector = hd.handDetector()

stopButton = st.button("Stop")

def bodyPartsName(lm):

    if lm[0][0] == 0:
        cv2.line(frame, (lm[0][1]-5, lm[0][2]+5), (lm[0][1]+100, lm[0][2]+5),(255, 0, 255),2)
        cv2.putText(frame, "Nose", (lm[0][1]+105, lm[0][2]+7),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (255, 0, 255), 1)
    if lm[3][0] == 3:
        cv2.line(frame, (lm[3][1]-5, lm[3][2]+5), (lm[3][1]+100, lm[3][2]+5),(255, 0, 255),2)
        cv2.putText(frame, "Left Eye", (lm[3][1]+100, lm[3][2]+5),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (255, 0, 255), 1)
    if lm[6][0] == 6:
        cv2.line(frame, (lm[6][1]+5, lm[6][2]+5), (lm[6][1]-80, lm[6][2]+5),(255, 0, 255),2)
        cv2.putText(frame, "Right Eye", (lm[6][1]-140, lm[6][2]),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (255, 0, 255), 1)
    if lm[10][0] == 10:
        cv2.line(frame, (lm[10][1]+5, lm[10][2]+5), (lm[10][1]-80, lm[10][2]+5),(255, 0, 255),2)
        cv2.putText(frame, "Lips",  (lm[10][1]-115, lm[10][2]+5),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (255, 0, 255), 1)

while True:

    try:

        Success, frame = cam.read()
        frame = detector.findPose(frame)
        bodayLm = detector.findPosLm(frame)

        frame = handDetector.findHands(frame)
        handLm = handDetector.findPositon(frame)


        # print(lm[0][1])

        bodyPartsName(bodayLm)

        noseDistance = math.sqrt(((handLm[8][1]-bodayLm[0][1])**2)+((handLm[8][2]-bodayLm[0][2])**2))
        print(noseDistance)

        # cTime = time.time()
        # fps = 1/(cTime - pTime)
        # pTime = cTime

        # cv2.putText(frame, str(int(fps)), (20, 70),
        #             cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

        cv2.imshow("Pose Estimation", frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        framePlaceholder.image(frame, channels="RGB")
        
        key = cv2.waitKey(1)

        if key == ord('q') or stopButton:
        # if key == ord('q'):
            cam.release()
            cv2.destroyAllWindows()
            break
    except:
        continue


cam.release()
cv2.destroyAllWindows()