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


'''
这个脚本做了以下工作：

    定义了一个 count_multi_class_images 函数，它遍历指定目录下的所有类别文件夹。

    对于每个类别文件夹，它检查 'images' 子文件夹中的所有图片。

    使用 defaultdict(set) 来存储每张图片所属的类别。这样可以自动创建一个空集合，而不需要检查键是否存在。

    遍历完所有类别后，它过滤出包含多个类别的图片。

    返回一个字典，其中键是图片名，值是包含该图片所有类别的集合。

    在 main 函数中，它打印出多类别图片的总数和详细信息。

    还提供了将结果保存到文件的选项（目前被注释掉了）。

使用这个脚本时，您需要：

    将 base_directory 替换为您实际的数据集路径。
    运行脚本。

脚本将输出多类别图片的数量和每张多类别图片的详细信息。如果您想将结果保存到文件，可以取消注释相关代码。

这个脚本的名称可以叫做 multi_class_image_counter.py，因为它主要功能是计数多类别图片。
'''