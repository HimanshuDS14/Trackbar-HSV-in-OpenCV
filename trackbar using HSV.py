import cv2
import numpy as np


def nothing(x):
    pass

cv2.namedWindow("Tracking color")
cv2.createTrackbar("lower Hue" , "Tracking color" , 0 ,255 , nothing)
cv2.createTrackbar("lower Saturation" , "Tracking color" , 0 ,255 , nothing)
cv2.createTrackbar("lower Value" , "Tracking color" , 0 ,255 , nothing)
cv2.createTrackbar("Upper hue" , "Tracking color" , 255 ,255 , nothing)
cv2.createTrackbar("Upper saturation" , "Tracking color" , 255 ,255 , nothing)
cv2.createTrackbar("Upper Value" , "Tracking color" , 255 ,255 , nothing)



while(1):
    image = cv2.imread("opencv.png")

    hsv = cv2.cvtColor(image ,cv2.COLOR_BGR2HSV)

    lower_h = cv2.getTrackbarPos("lower Hue" , "Tracking color")
    lower_s = cv2.getTrackbarPos("lower Saturation", "Tracking color")
    lower_v = cv2.getTrackbarPos("lower Value", "Tracking color")

    upper_h = cv2.getTrackbarPos("Upper Hue", "Tracking color")
    upper_s = cv2.getTrackbarPos("Upper Saturation", "Tracking color")
    upper_v = cv2.getTrackbarPos("Upper Value", "Tracking color")




    lower_range = np.array([lower_h , lower_s , lower_v] , dtype=np.uint8)
    upper_range = np.array([upper_h,upper_s,upper_v] , dtype=np.uint8)


    mask = cv2.inRange(hsv , lower_range , upper_range)

    res = cv2.bitwise_and(image , image , mask = mask)

    cv2.imshow("image", image)
    cv2.imshow("mask" , mask)
    cv2.imshow("res" , res)


    if cv2.waitKey(1)==13:
        break

cv2.destroyAllWindows()