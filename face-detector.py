import cv2

#loading the free open source xml file by Opencv which is already trained on a lot of frontal faces (haarcascade algorithm)
face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choosing an image to detect face
# img = cv2.imread('me.jpg')

# getting input from webcam
webcam = cv2.VideoCapture(0)      ## use cv2.VideoCapture(0) for webcam and cv2.imread('image file') for images

# Iterate forver through the frames
while True:
    #read the current frame
    successful_frame_read, frame = webcam.read()

    #converting the image into black&white (grayscale)
    bw_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detecting the face
    face_coordinates = face_data.detectMultiScale(bw_img)

    # drawing rectangle ariound the faces
    # (x, y, w, h) = face_coordinates[0]
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Rupesh's Face detector app", frame)
    key = cv2.waitKey(1)

    #End the program if Q is pressed
    if key==81 or key==113:
        break

#Release the video capture object
webcam.release()


'''
#detecting the face
face_coordinates = face_data.detectMultiScale(bw_img)

# drawing rectangle ariound the faces

# (x, y, w, h) = face_coordinates[0]
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

#showing the image
cv2.imshow("Rupesh's Face detector app", img)
#to keep the image on screen until we press any key
cv2.waitKey()


print("Completed")
'''