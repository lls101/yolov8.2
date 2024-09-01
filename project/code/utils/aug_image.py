import albumentations as A
import cv2
import numpy as np
import os
from glob import glob
from tqdm import tqdm

def validate_and_clip_bbox(bbox, image_filename, bbox_index):
    """验证并裁剪边界框坐标，同时记录任何异常情况"""
    clipped_bbox = []
    for i, coord in enumerate(bbox):
        if coord < 0 or coord > 1:
            print(f"警告: 文件 {image_filename} 中的第 {bbox_index + 1} 个边界框坐标超出范围: {coord}")
            coord = max(0, min(1, coord))
        clipped_bbox.append(coord)
    return clipped_bbox

def apply_augmentation(image, bboxes, class_labels, augmentation, image_filename):
    """应用单一增强操作"""
    # 验证并裁剪边界框坐标
    clipped_bboxes = [validate_and_clip_bbox(bbox, image_filename, i) for i, bbox in enumerate(bboxes)]
    
    aug_pipeline = A.Compose([augmentation], bbox_params=A.BboxParams(format='yolo', label_fields=['class_labels']))
    augmented = aug_pipeline(image=image, bboxes=clipped_bboxes, class_labels=class_labels)
    return augmented['image'], augmented['bboxes'], augmented['class_labels']

def augment_and_save(image_path, label_path, output_image_dir, output_label_dir, augmentations):
    """对图像进行增强并保存原图和单一增强版本"""
    # 读取图像和标注
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    image_filename = os.path.basename(image_path)
    
    with open(label_path, 'r') as f:
        yolo_annotations = [line.strip().split() for line in f]
    
    # 转换YOLO标注为Albumentations所需的格式
    bboxes = [[float(x) for x in ann[1:]] for ann in yolo_annotations]
    class_labels = [int(ann[0]) for ann in yolo_annotations]
    
    # 保存原始图像
    original_image_path = os.path.join(output_image_dir, f"{os.path.splitext(image_filename)[0]}_original.jpg")
    cv2.imwrite(original_image_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    
    # 保存原始标注（使用验证并裁剪后的边界框）
    label_filename = os.path.splitext(os.path.basename(label_path))[0]
    original_label_path = os.path.join(output_label_dir, f"{label_filename}_original.txt")
    with open(original_label_path, 'w') as f:
        for i, (bbox, class_label) in enumerate(zip(bboxes, class_labels)):
            clipped_bbox = validate_and_clip_bbox(bbox, image_filename, i)
            f.write(f"{class_label} {' '.join(map(str, clipped_bbox))}\n")
    
    # 应用并保存每个单一增强版本
    for aug_name, augmentation in augmentations.items():
        augmented_image, augmented_bboxes, augmented_class_labels = apply_augmentation(image, bboxes, class_labels, augmentation, image_filename)
        
        # 保存增强后的图像
        aug_image_path = os.path.join(output_image_dir, f"{os.path.splitext(image_filename)[0]}_{aug_name}.jpg")
        cv2.imwrite(aug_image_path, cv2.cvtColor(augmented_image, cv2.COLOR_RGB2BGR))
        
        # 保存增强后的标注
        aug_label_path = os.path.join(output_label_dir, f"{label_filename}_{aug_name}.txt")
        with open(aug_label_path, 'w') as f:
            for bbox, class_label in zip(augmented_bboxes, augmented_class_labels):
                f.write(f"{class_label} {' '.join(map(str, bbox))}\n")

def main(input_image_dir, input_label_dir, output_dir):
    """主函数"""
    # 创建输出目录
    output_image_dir = os.path.join(output_dir, 'images')
    output_label_dir = os.path.join(output_dir, 'labels')
    os.makedirs(output_image_dir, exist_ok=True)
    os.makedirs(output_label_dir, exist_ok=True)
    
    # 定义所有单一增强操作
    augmentations = {
        'vflip': A.VerticalFlip(p=1),
        'hflip': A.HorizontalFlip(p=1),
        # 'Shift': A.ShiftScaleRotate(shift_limit=0.2, scale_limit=0, rotate_limit=0, p=1),
        'Shift': A.ShiftScaleRotate(shift_limit=0.2, scale_limit=0, rotate_limit=0,border_mode=cv2.BORDER_CONSTANT,value=(0, 0, 0),  p=1),
        'SafeRote':  A.SafeRotate(limit=(-90, -90), border_mode=cv2.BORDER_CONSTANT,value=(0, 0, 0),p=1),
        # 'Rote':  A.SafeRotate(limit=(-90, -90), border_mode=cv2.BORDER_CONSTANT,value=(0, 0, 0),p=1),
        'Crop': A.BBoxSafeRandomCrop(erosion_rate=0.2, p=1),
        #'Contrast': A.RandomBrightnessContrast(brightness_limit=(-0, 0), contrast_limit=(0.3, 0.3), brightness_by_max=True,  p=1.0,)
        #'Brightness': A.RandomBrightnessContrast(brightness_limit=(-0, 0), contrast_limit=(-0.2, -0.2), brightness_by_max=True,  p=1.0,)
        #'GaussNoise ': A.GaussNoise(var_limit=(10.0, 50.0), p=1.0),
        'compose': A.Compose([A.VerticalFlip(p=1),A.ShiftScaleRotate(shift_limit=0.2, scale_limit=0, rotate_limit=0,border_mode=cv2.BORDER_CONSTANT,value=(0, 0, 0),  p=1)],p=1)
    }
    
    # 获取所有图像文件
    image_paths = glob(os.path.join(input_image_dir, '*.jpg')) + glob(os.path.join(input_image_dir, '*.png'))
    
    # 使用tqdm创建进度条
    for image_path in tqdm(image_paths, desc="Processing images", unit="image"):
        image_filename = os.path.basename(image_path)
        label_filename = os.path.splitext(image_filename)[0] + '.txt'
        label_path = os.path.join(input_label_dir, label_filename)
        
        if os.path.exists(label_path):
            try:
                augment_and_save(image_path, label_path, output_image_dir, output_label_dir, augmentations)
            except Exception as e:
                print(f"\n错误: 处理文件 {image_filename} 时出错: {str(e)}")
        else:
            print(f"\n警告: 未找到对应的标注文件 {label_path}")
if __name__ == "__main__":
    input_image_dir = "./out/train/images"
    input_label_dir = "./out/train/labels"
    output_dir = "./out/train_aug"
    main(input_image_dir, input_label_dir, output_dir)









