import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in i]   #to get mouse event present in cv2 library..here EVENT is a keyword
#print(events)
# arg-event that is taken place, x,y coordi whenever we click on image, flag, param..this formate is same everywhere
def click_event(event, x, y, flags, param):  #mouse call back function which is execute when mouse event take place
    if event == cv2.EVENT_LBUTTONDOWN:   #when we click with left mouse button on window
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        #cv2.circle(img, (x, y), 3, (0, 0, 255), -1)   #arg- image variable, center, radius, color, thickness
        mycolorImage = np.zeros((512, 512, 3), np.uint8)
        mycolorImage[:] = [blue, green, red]
        cv2.imshow('color', mycolorImage)

        '''cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append((x,y))   #append mouse click coordi
        if len(points) >=2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)   #join lines..arg-, last click, socond last click, colorof line, thickness of line
        cv2.imshow('image', img)'''


img = np.zeros((512,512,3), np.uint8)  #image create
#img = cv2.imread('lena.jpg')   #read image
cv2.imshow('image', img)
#points = []   #making list for saving coordinate when mouse click
cv2.setMouseCallback('image', click_event)   #way of calling callback function mouse_event function..arg- the name of image display, call function

cv2.waitKey(0)
cv2.destroyAllWindows()