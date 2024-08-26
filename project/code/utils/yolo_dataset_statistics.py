import os
import glob

def count_images_and_labels(base_dir):
    stats = {}

    for root, dirs, files in os.walk(base_dir):
        for dir_name in dirs:
            if dir_name.isdigit():  # 假设类别文件夹名是数字
                class_id = dir_name
                class_dir = os.path.join(root, dir_name)
                images_dir = os.path.join(class_dir, 'images')
                labels_dir = os.path.join(class_dir, 'labels')
                
                if os.path.exists(images_dir) and os.path.exists(labels_dir):
                    image_count = len(glob.glob(os.path.join(images_dir, '*')))
                    
                    label_count = 0
                    for label_file in glob.glob(os.path.join(labels_dir, '*.txt')):
                        with open(label_file, 'r') as f:
                            label_count += len(f.readlines())
                    
                    # 获取类别文件夹的完整路径
                    class_folder = os.path.relpath(class_dir, base_dir)
                    
                    if class_id not in stats:
                        stats[class_id] = {
                            'image_count': 0,
                            'label_count': 0,
                            'folders': set()
                        }
                    
                    stats[class_id]['image_count'] += image_count
                    stats[class_id]['label_count'] += label_count
                    stats[class_id]['folders'].add(class_folder)

    return stats

def main():
    base_directory = "./output"  # 替换为您的数据集路径
    statistics = count_images_and_labels(base_directory)

    print("Class Statistics:")
    print("-----------------")
    for class_id, data in statistics.items():
        print(f"Class {class_id}:")
        print(f"  Image count: {data['image_count']}")
        print(f"  Label count: {data['label_count']}")
        print(f"  Folders: {', '.join(data['folders'])}")
        print("-----------------")

    total_images = sum(data['image_count'] for data in statistics.values())
    total_labels = sum(data['label_count'] for data in statistics.values())
    print(f"Total Images: {total_images}")
    print(f"Total Labels: {total_labels}")

    # 如果需要，可以将结果保存到文件
    # with open('class_statistics.txt', 'w') as f:
    #     for class_id, data in statistics.items():
    #         f.write(f"Class {class_id}:\n")
    #         f.write(f"  Image count: {data['image_count']}\n")
    #         f.write(f"  Label count: {data['label_count']}\n")
    #         f.write(f"  Folders: {', '.join(data['folders'])}\n")
    #         f.write("-----------------\n")
    #     f.write(f"Total Images: {total_images}\n")
    #     f.write(f"Total Labels: {total_labels}\n")

if __name__ == "__main__":
    main()
