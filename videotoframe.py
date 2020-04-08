from cv2 import cv2
 
# Opens the Video file
cap= cv2.VideoCapture(r'C:\Users\Andreas\Desktop\frames_produktion\produktion.mp4')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('produktion_'+str(i)+'.jpg',frame)
    i+=1
 
cap.release()
cv2.destroyAllWindows()