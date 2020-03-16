#camera press 'q' button and then capture  your picture
import cv2

cap = cv2.VideoCapture(0)
count=0
while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("img", img)
    k = cv2.waitKey(30) & 0xFF
    
    if k == ord('q'):
        
        cv2.imwrite("C:/Users/pc1/Desktop/"+str(count)+"id.png",img)
        count=count+1
        
    elif k == 27:
        break
        
cap.release()
cv2.destroyAllWindows()
