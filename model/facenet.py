import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.models import load_model
import cv2
import numpy as np


def detect_faces(image):
    # Load the pre-trained Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    return faces


# Load the FaceNet model
model = tf.keras.models.load_model('facenet_keras_weights.h5', compile=False)


def preprocess_image(image, target_size=(160, 160)):
    # Convert the BGR image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Resize the image to the target size
    image = cv2.resize(image, target_size)

    # Convert the image to an array and preprocess it
    image = img_to_array(image)
    image = preprocess_input(image)

    # Expand the dimensions to match the model input requirements
    image = np.expand_dims(image, axis=0)

    return image


# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam feed
    ret, frame = cap.read()

    # Detect faces in the frame
    faces = detect_faces(frame)

    # Iterate over detected faces
    for (x, y, w, h) in faces:
        # Preprocess the face image
        face = frame[y:y+h, x:x+w]
        face = preprocess_image(face)

        # Apply face recognition using FaceNet
        embeddings = model.predict(face)[0]

        # TODO: Add your face recognition logic here

        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Webcam Face Recognition', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
