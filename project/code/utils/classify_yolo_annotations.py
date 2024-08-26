import os
import shutil

def process_yolo_annotations(source_dir, destination_base):
    # 确保目标基础目录存在
    if not os.path.exists(destination_base):
        os.makedirs(destination_base)

    # 遍历源目录中的所有文件
    for filename in os.listdir(source_dir):
        if filename.endswith('.txt'):  # 假设标注文件是.txt格式
            file_path = os.path.join(source_dir, filename)
            image_filename = os.path.splitext(filename)[0] + '.jpg'  # 假设图片是.jpg格式
            image_path = os.path.join(source_dir, image_filename)

            # 如果对应的图片文件不存在，跳过这个标注文件
            if not os.path.exists(image_path):
                print(f"Warning: Image file {image_filename} not found for annotation {filename}")
                continue

            # 读取标注文件
            with open(file_path, 'r') as f:
                lines = f.readlines()

            # 处理每一行标注
            for line in lines:
                parts = line.strip().split()
                if parts:
                    class_id = parts[0]
                    # 创建目标目录结构
                    dest_dir = os.path.join(destination_base, class_id)
                    dest_images_dir = os.path.join(dest_dir, 'images')
                    dest_labels_dir = os.path.join(dest_dir, 'labels')
                    
                    # 创建目录（如果不存在）
                    os.makedirs(dest_images_dir, exist_ok=True)
                    os.makedirs(dest_labels_dir, exist_ok=True)

                    # 复制标注文件到labels子文件夹
                    shutil.copy2(file_path, dest_labels_dir)

                    # 复制图片文件到images子文件夹
                    shutil.copy2(image_path, dest_images_dir)

                    print(f"Copied {filename} to {os.path.join(class_id, 'labels')} and {image_filename} to {os.path.join(class_id, 'images')}")

# 使用示例
source_directory = "./images"
destination_base_directory = "./output"

process_yolo_annotations(source_directory, destination_base_directory)
