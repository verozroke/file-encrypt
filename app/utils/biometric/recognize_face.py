import face_recognition
import cv2
import os

def recognize_face(username):
    known_faces = []
    known_files = []

    for filename in os.listdir('faces'):
        if filename.startswith(username) and filename.endswith(".jpg"):
            face = face_recognition.load_image_file(os.path.join('faces', filename))
            encoding = face_recognition.face_encodings(face)[0]
            known_faces.append(encoding)
            known_files.append(filename)

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_faces, face_encoding)
            if True in matches:
                cap.release()
                cv2.destroyAllWindows()
                return True
        cv2.imshow('img', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return False
