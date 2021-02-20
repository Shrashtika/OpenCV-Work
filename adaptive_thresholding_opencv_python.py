import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png', 0)

# adaptive threshold is not global for all region but for small region, different value for diff. region of the same image
_,th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)  #here 127 is global value which is same for all the pixel value
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)  #arg- source, max value (non zero) assigned to pixel for which condition is satisfied, adaptive method, threshold type, blocksize(size of neighbourhood area, value of c(constant)
# ADAPTIVE_THRESH_MEAN_C ::threshold value is mean of neighbourhood area

th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
# ADAPTIVE_THRESH_GAUSSIAN_C::threshold value is WEIGHTAGE mean of neighbourhood area

cv.imshow('image', img)
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)

cv.waitKey(0)
cv.destroyAllWindows()