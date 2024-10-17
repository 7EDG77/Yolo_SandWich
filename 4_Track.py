from ultralytics import YOLO

'''
  87 177 208.bset.pt 在Y:\\basicAI\\ROItools\\Yolov8\\weights\\文件下
  track()方法比 predict()方法多一个追踪算法
  model.track()返回resilts参数

'''
# Load a model
model = YOLO("Y:\\basicAI\\ROItools\\Yolov8\\weights\\87_weights\\best.pt")  # load a custom model

# Track with the model
# results = model.track(source="E:\Sandwich_Video\\", show=True, device='CPU')
model.predict('E:\\video_t\\0', imgsz=480, save=True)


#    YOLOv8采用2022年提出的跟踪算法BoT-SORT和ByteTrack两种算法实现目标跟踪
#    https://blog.csdn.net/litt1e/article/details/132214220
# model.track(source="E:\\video_t", device='CPU', imgsz=480, show=True, save=True)

# Export the model
model.export(format="onnx")
