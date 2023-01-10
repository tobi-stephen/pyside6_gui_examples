import cv2 as cv
import sys
import numpy

def main():
    cap = cv.VideoCapture(0)

    while True:
        ret, img = cap.read()
        if not ret:
            break

        cv.imshow('img', img)
        if cv.waitKey(1) & 0xFF == 27:
            break

    cv.destroyAllWindows()



if __name__=='__main__':
    main()