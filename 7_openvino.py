import os
import cv2
import time

from ultralytics import YOLO


from ultralytics import YOLO

model = YOLO("D:\PyCharm Community Edition 2024.1.4\\PythonPreject\\Awesome-Backbones-main\\Yolov8\\runs\\detect\\train206\\weights\\best.pt")  # load a custom model


# Export the model
model.export(format="openvino", imgsz=480, half=True)  # creates 'yolov8n_openvino_model/'

# Load the exported OpenVINO model
# ov_model = YOLO("D:/PyCharm Community Edition 2024.1.4/PythonPreject/Awesome-Backbones-main/Yolov8/runs/detect/train87/weights/best_openvino_model/")
# Run inference
# results = ov_model(video_folder)
