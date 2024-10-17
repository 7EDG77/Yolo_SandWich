import cv2
import os
from ultralytics import YOLO

'''
    对文件夹中的图片进行预测，并将预测结果裁剪出来
input：
    model_path: 模型路径
    imgdir: 图片文件夹路径
    output_dir: 输出文件夹路径    
    
注 results = model.predict(source=image_path, save=False, show=False)
for r in results:
    boxes = r.boxes
    scores = boxes.conf
    labels = boxes.cls
    print(f"Scores: {scores}, Labels: {labels}")
    
        Examples:
            >>> results = model('image.jpg')
            >>> boxes = results[0].boxes
            >>> xyxy = boxes.xyxy
            >>> print(xyxy)
'''
# Load a model
model_path = "D:\\PyCharm Community Edition 2024.1.4\\PythonPreject\\Awesome-Backbones-main\\Yolov8\\runs\\detect\\train208\\weights\\best.pt"
model = YOLO(model_path)  # load a custom model

# Input and output directories
input_dir = 'E:\\in'
output_dir = 'E:\\in_cropped'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process each image in the input directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(input_dir, filename)
        image = cv2.imread(image_path)
        results = model.predict(source=image_path, save=False, show=False)

        # Iterate over each detection result
        for index, r in enumerate(results):
            xyxy = r.boxes.xyxy  # Get detection box coordinates tensor
            xyxy = xyxy.cpu().numpy()  # Move tensor to CPU and convert to numpy array

            # Iterate over each detection box
            for box in xyxy:
                x1, y1, x2, y2 = box
                # Crop the image according to the detection box coordinates
                cropped_image = image[int(y1):int(y2), int(x1):int(x2)]

                # Save the cropped image with a new filename
                base_name = os.path.splitext(filename)[0]
                output_filename = f'{base_name}_{index+1}.jpg'  # Use index+1 to name the cropped images
                output_path = os.path.join(output_dir, output_filename)
                cv2.imwrite(output_path, cropped_image)
                print(f'Cropped image saved as: {output_path}')