import cv2 as cv

video = cv.VideoCapture(0)
#video = cv.VideoCapture('people.mp4')

subtractor = cv.createBackgroundSubtractorMOG2(100, 40)

while True:
    ret, frame = video.read()
    if ret:
        mask = subtractor.apply(frame)
        cv.imshow('Mask', mask)

        if cv.waitKey(5) == ord('x'):
            break
    else:
        video = cv.VideoCapture('people.mp4')

cv.destroyAllWindows()
video.release()
