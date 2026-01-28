import cv2

print(cv2.__version__)

img1 = cv2.imread('Resources/BlackPink.png')

print(img1.shape)

img1 = cv2.resize(img1,(int(img1.shape[1]/1.5),int(img1.shape[0]/1.5)))

img1 = cv2.cvtColor(img1,cv2.COLOR_RGB2YCrCb)

cv2.imshow("Frame",img1)

cv2.waitKey(0)


capture = cv2.VideoCapture("Resources/dog.mp4")

while True:
    success, img2 = capture.read()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2YCrCb)
    cv2.imshow("img",img2)

    if cv2.waitKey(20) & 0xff == ord('e'):
        break

capture.release()
cv2.destroyAllWindows()