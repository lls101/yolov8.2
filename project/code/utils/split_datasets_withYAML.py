import os
import random
import shutil
import yaml
from tqdm import tqdm

def copy_files(src_dir, dst_dir, filenames, extension):
    os.makedirs(dst_dir, exist_ok=True)
    missing_files = 0
    for filename in tqdm(filenames, desc=f"Copying to {os.path.basename(dst_dir)}"):
        src_path = os.path.join(src_dir, filename + extension)
        dst_path = os.path.join(dst_dir, filename + extension)
        
        if os.path.exists(src_path):
            shutil.copy(src_path, dst_path)
        else:
            print(f"Warning: File not found for {filename}")
            missing_files += 1

    return missing_files

def split_and_copy_dataset(image_dir, label_dir, output_dir, train_ratio=0.7, valid_ratio=0.15, test_ratio=0.15, class_names=None):
    image_filenames = [os.path.splitext(f)[0] for f in os.listdir(image_dir)]
    random.shuffle(image_filenames)

    total_count = len(image_filenames)
    train_count = int(total_count * train_ratio)
    valid_count = int(total_count * valid_ratio)
    test_count = total_count - train_count - valid_count

    train_image_dir = os.path.join(output_dir, 'train', 'images')
    train_label_dir = os.path.join(output_dir, 'train', 'labels')
    valid_image_dir = os.path.join(output_dir, 'valid', 'images')
    valid_label_dir = os.path.join(output_dir, 'valid', 'labels')
    test_image_dir = os.path.join(output_dir, 'test', 'images')
    test_label_dir = os.path.join(output_dir, 'test', 'labels')

    print("Copying train files...")
    train_missing_files = copy_files(image_dir, train_image_dir, image_filenames[:train_count], '.jpg')
    train_missing_files += copy_files(label_dir, train_label_dir, image_filenames[:train_count], '.txt')

    print("Copying validation files...")
    valid_missing_files = copy_files(image_dir, valid_image_dir, image_filenames[train_count:train_count + valid_count], '.jpg')
    valid_missing_files += copy_files(label_dir, valid_label_dir, image_filenames[train_count:train_count + valid_count], '.txt')

    print("Copying test files...")
    test_missing_files = copy_files(image_dir, test_image_dir, image_filenames[train_count + valid_count:], '.jpg')
    test_missing_files += copy_files(label_dir, test_label_dir, image_filenames[train_count + valid_count:], '.txt')

    print(f"Train dataset count: {train_count}, Missing files: {train_missing_files}")
    print(f"Validation dataset count: {valid_count}, Missing files: {valid_missing_files}")
    print(f"Test dataset count: {test_count}, Missing files: {test_missing_files}")

    # Generate data.yaml file
    data_yaml = {
        'path': os.path.abspath(output_dir),
        'train': os.path.join('train', 'images'),
        'val': os.path.join('valid', 'images'),
        'test': os.path.join('test', 'images'),
        'names': class_names if class_names else []
    }

    with open(os.path.join(output_dir, 'data.yaml'), 'w') as f:
        yaml.dump(data_yaml, f, default_flow_style=False)

    print(f"Generated data.yaml file in {output_dir}")

# 使用例子
image_dir = r'./test_output/images'
label_dir = r'./test_output/labels'
output_dir = r'./temp1'

# 定义类别名称
class_names = ['55']

split_and_copy_dataset(image_dir, label_dir, output_dir, class_names=class_names)
