import cv2
import mediapipe as mp

model_path = 'blazeface_sr.tflite'
canvas_path = 'black.png'

BaseOptions = mp.tasks.BaseOptions
FaceDetector = mp.tasks.vision.FaceDetector
FaceDetectorOptions = mp.tasks.vision.FaceDetectorOptions
RunningMode = mp.tasks.vision.RunningMode

def drawADot(result, output_image, timestamp_ms):
    if result.detections:
        for detection in result.detections:
            boundingBox = detection.bounding_box
            locationData = boundingBox.origin_x, boundingBox.origin_y, boundingBox.width, boundingBox.height

            canvas = cv2.imread(canvas_path)
            cv2.circle(canvas, (locationData[0], locationData[1]), 10, (255, 255, 255))

    cv2.imshow("Live", canvas)
    cv2.waitKey(timestamp_ms)

options = FaceDetectorOptions(
    base_options = BaseOptions(model_asset_path = model_path),
    running_mode = RunningMode.LIVE_STREAM,
    result_callback=drawADot
)

camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()
    frame = cv2.flip(frame, 1)
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)

    # help(FaceDetector.create_from_options)

    with FaceDetector.create_from_options(options) as detector:
        detector.detect_async(image, 1)