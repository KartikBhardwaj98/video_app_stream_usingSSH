import cv2
cap=cv2.VideoCapture(0)
while True:
    ret, photo= cap.read()
    cv2.imshow("hi",photo)
    if cv2.waitKey()== 13:
        break
cv2.destroyAllWindows()
