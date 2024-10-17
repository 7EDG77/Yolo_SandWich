from ultralytics import YOLO

'''
    .yaml文件指定数据路径，与网络参数
    无论指定.yaml文件与否，都会载入ultralytics/defult.yaml 
    （defult.yaml文件中能指定网络参数 或 在model.train中也能指定，优先级更高）

    model_config = "yolov8n.yaml" 与 "yolov8n.pt"载入模型完全等效
    
'''
if __name__ == "__main__":
    model_config = "yolov10m.pt"
    data_config = "v2.yaml"  # 数据集配置文件
    # pretrained_weights = r"D:\PyCharm Community Edition 2024.1.4\PythonPreject\Awesome-Backbones-main\Yolov8\best.pt"
    # 加载预训练模型
    model = YOLO(model_config)  # 可以指定预训练权重，如果使用
    # model.load(pretrained_weights)

    # 训练模型
    model.train(data=data_config, epochs=50, batch=16, imgsz=480,
                save_dir='D:\PyCharm Community Edition 2024.1.4\PythonPreject\Awesome-Backbones-main\Yolov8')


