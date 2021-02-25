import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in i]   #to get mouse event present in cv2 library..here EVENT is a keyword
#print(events)
# arg-event that is taken place, x,y coordi whenever we click on image, flag, param..this formate is same everywhere
def click_event(event, x, y, flags, param):  #mouse call back function which is execute when mouse event take place
    if event == cv2.EVENT_LBUTTONDOWN:  #when we click with left mouse button on window
        print(x, " ", y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x)+','+str(y)
        cv2.putText(img, strXY, (x,y), font, 0.5, (255,255,0), 1)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]   #read blue channel and color channel read opposite coordinate
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ',' + str(green)+ ',' +str(red)
        cv2.putText(img, strBGR, (x, y), font, 0.5, (0, 255, 255), 1)
        cv2.imshow('image', img)



#img = np.zeros((512,512,3), np.uint8)  #image create
img = cv2.imread('lena.jpg')   #read image
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)   #way of calling mouse event function..arg- the name of image display, call function

cv2.waitKey(0)
cv2.destroyAllWindows()