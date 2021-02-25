import cv2
img = cv2.imread('lena.jpg', 0)   #read image ..arg- file name, in which color
#0 gray 1 colour image -1 including alpha channel

print(img)   #image pixels

cv2.imshow('image', img)   #dispay image for millisec... arg- image name,variable in which image read

#cv2.waitKey(5000) & 0xFF  #waitkey may taking input from user
#if arguement 5000 that is for 5 seconds photo display which is delay time

k = cv2.waitKey(0) & 0xFF   #waitkey taking input from user and here delay is none
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()