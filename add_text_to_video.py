import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #read and print height
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

#cap.set(3, 3000)   #also can be set these height and width that we want to set..arg(CAP_PROP_FRAME_HEIGHT or 3, height that we want)
#cap.set(4, 3000)
#camera always set value according to resolution present there
#print(cap.get(3))
#print(cap.get(3))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # frame is continuous images
        font = cv2.FONT_HERSHEY_COMPLEX
        text = 'Width: ' + str(cap.get(3)) + 'Height: ' + str(cap.get(4))
        datet = str(datetime.datetime.now())

        frame = cv2.putText(frame, datet, (50,50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)   #writing text..arg-frame variable, text, coordi of text start, font, font scale, font color, thickness of letters and digits, linetype
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
