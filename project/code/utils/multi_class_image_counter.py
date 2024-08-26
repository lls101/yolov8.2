import os
from collections import defaultdict

def count_multi_class_images(base_dir):
    # 使用defaultdict，这样我们不需要检查键是否存在
    image_classes = defaultdict(set)

    # 遍历基础目录下的所有子目录
    for class_id in os.listdir(base_dir):
        class_dir = os.path.join(base_dir, class_id)
        if os.path.isdir(class_dir):
            images_dir = os.path.join(class_dir, 'images')
            if os.path.exists(images_dir):
                # 遍历images目录中的所有图片
                for image_name in os.listdir(images_dir):
                    # 将类别ID添加到该图片的set中
                    image_classes[image_name].add(class_id)

    # 过滤出包含多个类别的图片
    multi_class_images = {img: classes for img, classes in image_classes.items() if len(classes) > 1}

    return multi_class_images

def main():
    base_directory = "./output"  # 替换为您的数据集路径
    multi_class_images = count_multi_class_images(base_directory)

    # 打印结果
    print(f"Total number of multi-class images: {len(multi_class_images)}")
    for image, classes in multi_class_images.items():
        print(f"{image}: {classes}")

    # 如果需要，可以将结果保存到文件
    # with open('multi_class_images.txt', 'w') as f:
    #     for image, classes in multi_class_images.items():
    #         f.write(f"{image}: {classes}\n")

if __name__ == "__main__":
    main()
