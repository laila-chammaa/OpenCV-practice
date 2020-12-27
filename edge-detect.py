import cv2 as cv
import numpy

camera = cv.VideoCapture(0)

while True:
    _, frame = camera.read()
    laplacian = cv.Laplacian(frame, cv.CV_64F)
    # converting to int
    laplacian = numpy.uint8(laplacian)
    cv.imshow("Laplacian", laplacian)

    edges = cv.Canny(frame, 110, 110)
    cv.imshow("Canny", edges)

    if cv.waitKey(5) == ord('x'):
        break

camera.release()
cv.destroyAllWindows()
