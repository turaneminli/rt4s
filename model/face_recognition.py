import cv2
import threading
from deepface import DeepFace

cap = cv2.VideoCapture(1)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

resident_faces = []  # List of resident face images


def is_resident(frame):
    try:
        for resident_face in resident_faces:
            result = DeepFace.verify(frame, resident_face.copy(
            ), model_name="Facenet", enforce_detection=False)
            if result['verified']:
                return True
    except ValueError as e:
        print("ERROR", str(e))
    return False


def detect_non_resident(frame):
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=8, minSize=(30, 30))
    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]
        print(is_resident(face_img))
        if not is_resident(face_img):
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.putText(frame, "NON-RESIDENT", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        else:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "RESIDENT", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)


def display_frame():
    while True:
        ret, frame = cap.read()

        if ret:
            detect_non_resident(frame)

            # Display the frame
            cv2.imshow("Surveillance", frame)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


# Load resident face images
resident_faces.append(cv2.imread("reference2.jpg"))
resident_faces.append(cv2.imread("reference3.jpg"))
# resident_faces.append(cv2.imread("reference4.jpg"))
resident_faces.append(cv2.imread("friends1.jpg"))
# resident_faces.append(cv2.imread("friends2.jpg"))
# resident_faces.append(cv2.imread("friends3.jpg"))


# Create a new thread to display the frame
display_frame()
