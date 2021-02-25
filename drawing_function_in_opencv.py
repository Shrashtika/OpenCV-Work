import numpy as np
import cv2

#img = cv2.imread('lena.jpg', 1) #image read
img = np.zeros((512, 512, 3), np.uint8)   #create image of black color arg-(height, width, 3(represent there are 3 channels))shape, datatype, order

#img = cv2.line(img, (0, 0), (255, 255), (67, 168, 128), 5) #draw line on image
# arg-image variable, starting coordinate, ending coordi, in which color line draw(blue green red),thickness
#for other color (rgb color picker)(67, 168, 128) in reverse order

#img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 5) #to draw arrowed line

img = cv2.rectangle(img, (384, 0), (510,128), (0, 0, 255), -1)   #to draw rectangle- arg--image variable, top left corner, bottom right corner, ,
#if we use -1 instead of thickness then whole rect filled with color
#img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1) #draw circle..arg-image variable, coordinate of centre, radius, ,

font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'OpenCv', (10,500), font, 4, (255, 255, 255), 10, cv2.LINE_AA)  #add text..arg-, text, start coordi of text, font, fontsize, font color, thickness of letters or digits, line type
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
