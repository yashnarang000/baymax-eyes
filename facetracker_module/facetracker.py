import mediapipe as mp
import cv2
import time

# defining some shortcut variables so I don't have to drain my fingers
BaseOptions = mp.tasks.BaseOptions
FaceDetector = mp.tasks.vision.FaceDetector
FaceDetectorOptions = mp.tasks.vision.FaceDetectorOptions
RunningMode = mp.tasks.vision.RunningMode

class Tracker:

    def __init__(self, cam_id, model_asset_path, operation):

        self.cam_id = cam_id
        self.model_asset_path = model_asset_path
        self.operation = operation

        self.options = FaceDetectorOptions(
            base_options = BaseOptions(model_asset_path=self.model_asset_path),
            running_mode = RunningMode.LIVE_STREAM,
            result_callback = self.operation
        )

    def start(self, looping_condition):

        cam = cv2.VideoCapture(self.cam_id)

        with FaceDetector.create_from_options(self.options) as detector:

            while looping_condition:
                success, frame = cam.read()
                frame = cv2.flip(frame, 1)

                frame = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
                
                detector.detect_async(frame, int(time.time()*1000))