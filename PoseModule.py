import cv2
import mediapipe as mp
import time

class poseDetector():

    def __init__(self, mode = False, modelComp = 1, smoothLm = True,
                 enalbeSeg = False, smoothSeg = True, detectionCon = 0.5,
                 trackCon = 0.5):
        self.mode = mode
        self.modelComp = modelComp
        self.smoothLm = smoothLm
        self.enalbeSeg = enalbeSeg
        self.smoothSeg = smoothSeg
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.modelComp, self.smoothLm,
                                     self.enalbeSeg, self.smoothSeg,
                                     self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findPose(self, frame):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        # print(results.pose_landmarks)

        # if self.results.pose_landmarks:
        #     self.mpDraw.draw_landmarks(frame, self.results.pose_landmarks,
        #                                self.mpPose.POSE_CONNECTIONS)
        return frame

    def findPosLm(self, frame):

        poseLm = []

        for id, lm in enumerate(self.results.pose_landmarks.landmark):
            h, w, c = frame.shape
            # print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            poseLm.append([id, cx, cy])
            # cv2.circle(frame, (cx, cy), 4, (255, 0, 255), cv2.FILLED)


        return poseLm



def main():
    pTime = 0
    cam = cv2.VideoCapture("pose2.mp4")
    detector = poseDetector()
    while True:
        Success, frame = cam.read()
        frame = detector.findPose(frame)
        poselm = detector.findPosLm(frame)
        print(poselm)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(frame, str(int(fps)), (20, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

        cv2.imshow("Pose Estimation Module", frame)
        key = cv2.waitKey(1)

        if key == 81 or key == 113:
            break

if __name__ == "__main__":
    main()
