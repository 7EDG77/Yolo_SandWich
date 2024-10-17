from ultralytics import YOLO

model = YOLO("D:\PyCharm Community Edition 2024.1.4\\PythonPreject\\Awesome-Backbones-main\\Yolov8\\runs\\detect\\train208\\weights\\best.pt")  # load a custom model


# Export the model
# model.export(format="openvino", imgsz=480, half=True)  # creates 'yolov8n_openvino_model/'
model.export(format="onnx", imgsz=480, half=True)  # creates 'yolov8n.onnx'

