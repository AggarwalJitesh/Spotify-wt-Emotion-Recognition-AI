from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import numpy as np
import cv2
import dlib

cap = cv2.VideoCapture(0)

class_labels = ['Angry','Happy','Neutral','Sad']

classifier =load_model(r'C:\Users\kaifh\Desktop\Emotion detector\Emotion_detector.h5')
clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(4,3))
hog_face_detector = dlib.get_frontal_face_detector()
dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def rect_to_bb(rect):
    # take a bounding predicted by dlib and convert it  to the format (x, y, w, h) as we would normally do with OpenCV
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    return x, y, w, h


while True:
    _, frame = cap.read()
    gray = clahe.apply(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))

    faces = hog_face_detector(gray)
    rects = hog_face_detector(gray, 1)
    for rect in rects:
        (x, y, w, h) = rect_to_bb(rect)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)
        
        if np.sum([roi_gray])!=0:
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi,axis=0)
            
            preds = classifier.predict(roi)[0]
            label=class_labels[preds.argmax()]
            label_position = (x,y)
            cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
        else:
            cv2.putText(frame,'No Face Found',(20,60),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)

    for face in faces:
        face_landmarks = dlib_facelandmark(gray, face)

        for n in range(0,68):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            cv2.circle(frame, (x, y), 1, (0, 255, 0), 1)

    cv2.imshow("Face Landmarks", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()