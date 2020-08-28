import cv2
import datetime

# Can also be used to read from files
cap = cv2.VideoCapture(0); 

cap.set(3, 1920)
cap.set(4, 1080)

# Writing to a file 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (1280, 720))

while cap.isOpened():
    ret, frame = cap.read()

    if ret:    
        height = cap.get(3)
        width = cap.get(4)

        # Putting text in the frame
        text = (height, width)
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, "{} {}".format(datet, text), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)

        out.write(frame)

        if ret:
            cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
