细节见 readme.ipynb文件 或 官方文档 https://docs.ultralytics.com/zh/guides/#guides

需求文件都存放在 Y:\basicAI\ROItools\Yolov8 目录下文件
模型下载路径: /mnt/90_sdb/sda_backup/sda/hhy/Yolov8/wights/208_weights

    pip install -r requirements.txt
    
## 1 数据集准备
### - Yolov8/ img9k_all        		数据集
### - Yolov8/ 0_Video_Img.py        		将视频抽帧为图片
### - Yolov8/ 1_split_train_val.py   	 	将XML文件随机划分
### - Yolov8/ 2_voc_label.py      	 	将VOC数据集格式转换成YOLO格式


## 2 配置文件解释  
.yaml文件指定数据路径与网络参数  

无论指定.yaml文件与否，都会载入ultralytics/defult.yaml  

（defult.yaml文件中能指定网络参数 或 在model.train中也能指定，优先级更高）

### - Wights                        		训练过程中较好.pt和.onnx文件
### - V1.yaml                       		增加CA层Yolov8训练文件
### - V2.yaml				        Yolov8源训练文件


## 3 train   
v8 与 v10训练文件仅有 'model_config = xx'差距  
  
model_config = "yolov8n.yaml" 与 "yolov8n.pt"载入模型完全等效  

详情请参见 https://docs.ultralytics.com/zh/modes/train/
    
### - Yolov8/ 3_YOLO10.py       		v10模型训练文件
### - Yolov8/ 3_YOLOV8n.py		        v8模型训练文件


## 4 test  

详情请参见 https://docs.ultralytics.com/zh/modes/predict/
### - Yolov8/ 4_Track.py           		目标检测检测文件
### - Yolov8/ 4_corpped.py           		快速裁剪图片
### - Yolov8/ 5_Auto.py		 	使用预训练模型权重对图像集进行识别后自动标注（增加数据集使用）

## 5 模型转换  

详情请参见 https://docs.ultralytics.com/zh/modes/export/
### - Yolov8/ 6_prune.py			剪枝、约束训练
### - Yolov8/ 7_onnx.py       	 	onnx转换
### - Yolov8/ 7_openvino.py        		openvino转换
### - Yolov8/ 7_openvino_test.py    		openvino测试





