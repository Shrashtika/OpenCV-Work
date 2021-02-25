#read display save video via camera
import cv2


cap = cv2.VideoCapture(0)   #capture livestream from camera(0,-1)...for read the video from file give file name in argument
#if more than camera then 1(2nd camera) ,2 like argument

#for saving videos ...video writer class
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')   #either(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))    #arguement-video saving file, fourcc code, no of frame, size
#fourcc appear when you dont hav etheright codec installed to play AVI file.

#videos properties:::video open or not
print(cap.isOpened())     #used to know videofile exist or not...camera device present or not
while(cap.isOpened()):
#while (True) :    #in order to capture frame continuously
    ret, frame = cap.read ()   #if frame available then ret(T, F) and and frame stored in frame variable
    if(ret == True):
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  #WIDTH AND HEIGHT OF THE FRAME
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)  #to write video and saved in BGR format...frame is frame captured variable

        gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   #to convert in gray color...source is frame and convert from blue green red to gray
        cv2.imshow('frame', gray)      #cv2.imshow('frame', frame)   #arguement-name of window and frame variable

        if cv2.waitKey(1) & 0xFF == ord('q'):   #for 64bit machine 0xFF is mask...waitkey used for user input
            break
    else:
        break

cap.release()    #to release resources
out.release()
cv2.destroyAllWindows()

'''#videos properties:::video open or not
print(cap.isOpened())     #used to know videofile exist or not...camera device present or not
while(cap.isOpened()):'''
