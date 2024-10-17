from ultralytics import YOLO

'''
    v8 与 v10训练文件仅有 'model_config = '差距
    model_config = "yolov8n.yaml" 与 "yolov8n.pt"载入模型完全等效
    
'''
if __name__ == "__main__":
    model_config = "yolov8n.yaml"
    data_config = "v2.yaml"      # 数据集配置文件
    # pretrained_weights = r"D:\PyCharm Community Edition 2024.1.4\PythonPreject\Awesome-Backbones-main\Yolov8\best.pt"
    # 加载模型
    model = YOLO(model_config)  # 可以指定预训练权重，如果使用
    # model.load(pretrained_weights)

    # 训练模型
    model.train(data=data_config, epochs=100, batch=16, imgsz=480, save_dir = 'D:\PyCharm Community Edition 2024.1.4\PythonPreject\Awesome-Backbones-main\Yolov8')

    # 在验证集上评估模型性能
    metrics = model.val(data=data_config)
    # 对本地图像进行预测
    # 确保这里的路径指向你的图像文件
    model.predict(source='text',
                  project='runs_m/detect',
                  name='exp',
                  save=True,)
