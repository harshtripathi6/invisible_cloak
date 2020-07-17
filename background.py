import cv2
cap = cv2.VideoCapture(0)                       #capturing from webcam

while cap.isOpened():
    ret, back = cap.read()                      #this is what the webcam is reading. ret is basically a bool variable used for testing truth

    if ret:
        cv2.imshow("image",back)
        if cv2.waitKey(5) == ord('q'):

            cv2.imwrite('image.jpg',back)       #this is saving the image
            break

cap.release()
cv2.destroyAllWindows()