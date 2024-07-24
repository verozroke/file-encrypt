import cv2
import os
from datetime import datetime

def capture_face(username):
    if not os.path.exists('faces'):
        os.makedirs('faces')

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{username}_{timestamp}.jpg"

    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            face = frame[y:y+h, x:x+w]
            cv2.imwrite(os.path.join('faces', file_name), face)

        cv2.imshow('img', frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or len(faces) > 0:
            break

    cap.release()
    cv2.destroyAllWindows()
    return file_name
