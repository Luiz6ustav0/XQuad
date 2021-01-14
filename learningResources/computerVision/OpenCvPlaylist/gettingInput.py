# Learning to read videos, display and save them

import cv2

# Can also be used to read from files
cap = cv2.VideoCapture(0); 

cap.set(3, 1920)
cap.set(4, 1080)
# Writing to a file 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()

    if ret:    
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        print((height, width))

        out.write(frame)

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if ret:
            cv2.imshow('Frame', gray_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
