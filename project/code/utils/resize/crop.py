import os
from PIL import Image

def resize_and_crop_center(input_dir, output_dir, target_size=(2048, 1365)):
    for root, dirs, files in os.walk(input_dir):
        # 构造当前目录对应的输出目录
        relative_path = os.path.relpath(root, input_dir)
        output_path = os.path.join(output_dir, relative_path)
        
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        for filename in files:
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                img_path = os.path.join(root, filename)
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
                output_img_path = os.path.join(output_path, filename)
                img_cropped.save(output_img_path)
                print(f"Cropped and saved {filename} to {output_img_path}")

# 输入和输出根目录
input_root_dir = r'D:\datasets\grape\origin\test'  # 替换为你的根目录
output_root_dir = r'D:\datasets\grape\origin\testnew'  # 替换为你的输出根目录

# 执行缩放和中心裁剪
resize_and_crop_center(input_root_dir, output_root_dir, target_size=(2048, 1365))
