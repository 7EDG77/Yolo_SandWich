from ultralytics import YOLO

# 设置视频文件夹路径
video_folder = "E:\\video_t"

model = YOLO("D:/PyCharm Community Edition 2024.1.4/PythonPreject/Awesome-Backbones-main/Yolov8/runs/detect/train206/weights/best_openvino_model/")

# half
model.predict(video_folder, imgsz=480, save=True, show=True, device='CPU')

