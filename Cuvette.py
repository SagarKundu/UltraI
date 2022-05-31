import cv2
video=cv2.VideoCapture("C:/Users/sagar/Downloads/car_test.mp4")
while True:
    status, frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    cv2.imshow('Gray Video',gray)
    key=cv2.waitKey(0)
    if key==ord('q'):
        break
video.release()
cv2.destroyWindows()
