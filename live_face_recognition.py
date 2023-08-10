import faceEncoder as fe
import face_recognition as fr
import pickle
import cv2
import numpy as np

myfaces= fe.get_encodings('myencodings.dat')


def find_faces_in_frame(frame):
    count, encodings, face_dims= fe.encodeFace(frame)

    if count > 0:
        return count, encodings, face_dims

    return 0, None, None



DEFAULT_CAMERA= 0
vid= cv2.VideoCapture(DEFAULT_CAMERA)
turn= True


while True:
    # Grab a single frame of video
    ret, frame = vid.read()

    # Only process every other frame of video to save time
    if turn:
        # Resize frame of video to 1/2 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame
        
        # Find all the faces and face encodings in the current frame of video
        face_locations = fr.face_locations(rgb_small_frame)
        face_encodings = fr.face_encodings(rgb_small_frame, face_locations)
        #print(type(face_encodings))

        face_names = []
        for face_encoding in face_encodings:
            
            # See if the face is a match for the known face(s)
            results = fr.compare_faces(myfaces, face_encoding, 0.1)
            
            match= False
            for result in results:
                if np.count_nonzero(result) / np.size(result) > 0.95:
                    match= True
                    break
            

            face_names.append(name)

    turn = not turn


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/2 size
        s_up= 2
        top *= s_up
        right *= s_up
        bottom *= s_up
        left *= s_up
        if match:
        # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        else:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    
    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

   
vid.release()
cv2.destroyAllWindows()
