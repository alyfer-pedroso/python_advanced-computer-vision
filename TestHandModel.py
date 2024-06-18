import cv2
import time
import HandTrackingModule as htm

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = htm.handDetector()

    while True: 
        success, img = cap.read()
        img = detector.findHands(img, draw=True)
        lmList = detector.findPosition(img, draw=False)
        if len(lmList) != 0:
            print(lmList[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, "FPS: "+str(round(fps)), (5, 25), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()