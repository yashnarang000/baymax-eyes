import facetracker as ft

def func(result, output_image, timestamp_ms):
    if result.detections:
        for detection in result.detections:
            print(detection)

tracking = ft.Tracker(0, 'blazeface_sr.tflite', func)

tracking.start(True)