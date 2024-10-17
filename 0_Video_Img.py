import cv2
import os
import numpy as np
import random
'''
    # 视频和输出目录的路径
    video_dir = 'E:\\Sandwich_Video' # 视频文件夹
    output_dir = 'E:\\Only_Sandwich_Video2Img' # 转换为图片的文件夹

'''
# 视频和输出目录的路径
video_dir = 'E:\\Sandwich_Video'
output_dir = 'E:\\Only_Sandwich_Video2Img'

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 遍历视频目录中的所有文件
for video_file in os.listdir(video_dir):
    if video_file.endswith(('.mp4', '.avi', '.mov', '.mkv')):
        video_path = os.path.join(video_dir, video_file)
        cap = cv2.VideoCapture(video_path)

        # 获取视频的总帧数
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        num_frames_to_extract = min(10, total_frames)  # 不多于10帧

        # 随机选择帧的索引
        frame_indices = random.sample(range(total_frames), num_frames_to_extract)

        # 按随机顺序抽取帧并保存
        for frame_index in frame_indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)  # 设置到指定帧
            success, image = cap.read()
            if success:
                frame_count = len(frame_indices) - frame_indices[::-1].index(frame_index)  # 计算当前帧的序号
                output_path = os.path.join(output_dir, f"{os.path.splitext(video_file)[0]}_frame_{frame_count}.jpg")
                cv2.imwrite(output_path, image)
                print(f"Saved frame {frame_index} from {video_file} to {output_path}")

        # 释放视频捕获对象
        cap.release()

print("All videos processed.")