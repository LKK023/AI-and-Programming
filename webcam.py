import cv2
import numpy as np
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    success, img3 = capture.read()
    imgCanny = cv2.Canny(img3, 100,100)
    kernel  = np.ones((5,5), np.uint8)
    imgDilation = cv2.dilate(imgCanny,kernel,iterations=3)

    cv2.imshow("webcam", img3)
    cv2.imshow("imgCanny", imgCanny)
    cv2.imshow("imgDilate", imgDilation)

    if cv2.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
