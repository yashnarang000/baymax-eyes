import cv2
import mediapipe as mp
from time import time

model_path = 'blazeface_sr.tflite'
canvas_path = 'black.png'

BaseOptions = mp.tasks.BaseOptions
FaceDetector = mp.tasks.vision.FaceDetector
FaceDetectorOptions = mp.tasks.vision.FaceDetectorOptions
RunningMode = mp.tasks.vision.RunningMode

canvas = cv2.imread(canvas_path)

def drawADot(result, output_image, timestamp_ms):
    global canvas

    if result.detections:
        for detection in result.detections:
            boundingBox = detection.bounding_box
            x, y = boundingBox.origin_x, boundingBox.origin_y

            cv2.circle(canvas, (x, y), 5, (255, 255, 255), -1)


options = FaceDetectorOptions(
    base_options = BaseOptions(model_asset_path = model_path),
    running_mode = RunningMode.LIVE_STREAM,
    result_callback=drawADot
)

camera = cv2.VideoCapture(0)

with FaceDetector.create_from_options(options) as detector:
    while True:
        success, frame = camera.read()
        frame = cv2.flip(frame, 1)
        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame) 
        
        detector.detect_async(image, int(time()*1000))

        cv2.imshow("Canvas", canvas)
        cv2.waitKey(1)