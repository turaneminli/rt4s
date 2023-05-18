from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import cv2
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)

# Load YOLOv2 model
net = cv2.dnn.readNetFromDarknet('yolov2.cfg', 'yolov2.weights')
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]


def detect_objects(frame):
    # Resize frame for YOLOv2 model
    resized_frame = cv2.resize(frame, (416, 416))
    blob = cv2.dnn.blobFromImage(
        resized_frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    # Pass frame through YOLOv2 model
    net.setInput(blob)
    outs = net.forward(output_layers)

    height, width, _ = frame.shape

    class_ids = []
    confidences = []
    boxes = []

    # Process the outputs and filter for objects with high confidence
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

    # Draw bounding boxes and labels on the frame
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(class_ids[i])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, label, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame


@socketio.on('connect')
def handle_connect():
    print('A client has connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('A client has disconnected')


@socketio.on('request_detection')
def handle_detection():
    # Open webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read frame from webcam
        ret, frame = cap.read()

        # Perform object detection on frame
        detected_frame = detect_objects(frame)

        # Convert frame to JPEG format for streaming
        ret, jpeg = cv2.imencode('.jpg', detected_frame)
        frame_data = jpeg.tobytes()

        # Send frame data via socket event
        emit('detection_frame', frame_data, broadcast=True)

        # Check for client disconnect event
        if not socketio.server.eio.connected_clients:
            break

    # Release webcam and resources
    cap.release()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, debug=True)
