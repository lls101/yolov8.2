import cv2
import os

def compress_images(input_directory, output_directory, quality):
    # 确保质量百分比在0-100之间
    quality = max(0, min(quality, 100))
    
    # 如果输出目录不存在，创建它
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            input_filepath = os.path.join(input_directory, filename)
            output_filepath = os.path.join(output_directory, filename)
            
            # 读取图像
            img = cv2.imread(input_filepath)
            
            if img is not None:
                # 获取文件扩展名
                _, ext = os.path.splitext(filename)
                
                # 根据文件扩展名选择压缩参数
                if ext.lower() in ['.jpg', '.jpeg']:
                    params = [cv2.IMWRITE_JPEG_QUALITY, quality]
                elif ext.lower() == '.png':
                    params = [cv2.IMWRITE_PNG_COMPRESSION, 9]  # PNG使用0-9的压缩级别
                else:
                    params = []  # 对于其他格式，不使用特殊参数
                
                # 压缩并保存图像
                cv2.imwrite(output_filepath, img, params)
                
                print(f'Compressed: {filename}')
            else:
                print(f'Failed to read: {filename}')

# 使用示例
input_directory = './images'  # 替换为你的输入图片目录路径
output_directory = './compress_images'  # 替换为你想保存压缩后图片的目录路径
quality = 50 # 设置压缩质量（0-100）

compress_images(input_directory, output_directory, quality)
