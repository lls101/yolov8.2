import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def resize_and_crop_center(input_dir, output_dir, target_size=(2048, 1365)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(input_dir, filename)
            img = Image.open(img_path)
            
            img_width, img_height = img.size
            
            # 计算缩放比例，确保图像至少大于目标大小
            scale = max(target_size[0] / img_width, target_size[1] / img_height)
            new_size = (int(img_width * scale), int(img_height * scale))
            img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
            
            # 更新大小
            img_width, img_height = img_resized.size

            # 中心裁剪位置
            left = (img_width - target_size[0]) / 2
            top = (img_height - target_size[1]) / 2
            right = (img_width + target_size[0]) / 2
            bottom = (img_height + target_size[1]) / 2
            
            img_cropped = img_resized.crop((left, top, right, bottom))
            
            # 保存裁剪后的图像
            img_cropped.save(os.path.join(output_dir, filename))
            print(f"Cropped and saved {filename} to {output_dir}")
            
            # 可视化裁剪过程
            fig, ax = plt.subplots(1, 3, figsize=(18, 6))
            
            # 原始图片
            ax[0].imshow(np.array(img))
            ax[0].set_title(f"Original Image\n{img.size[0]}x{img.size[1]}")
            
            # 缩放后的图片
            ax[1].imshow(np.array(img_resized))
            ax[1].set_title(f"Resized Image\n{img_resized.size[0]}x{img_resized.size[1]}")
            ax[1].add_patch(plt.Rectangle((left, top), target_size[0], target_size[1], edgecolor='r', facecolor='none', lw=2))
            
            # 裁剪后的图片
            ax[2].imshow(np.array(img_cropped))
            ax[2].set_title(f"Cropped Image\n{target_size[0]}x{target_size[1]}")
            
            for a in ax:
                a.axis('off')
            
            plt.tight_layout()
            plt.show()

# 输入和输出目录
input_dir = r'D:\Workspace\datasets\test\in\tt'  # 替换为你的图片目录
output_dir = r'D:\Workspace\datasets\test\out'  # 替换为你的输出目录

# 执行缩放和中心裁剪并可视化
resize_and_crop_center(input_dir, output_dir, target_size=(2048, 1365))
