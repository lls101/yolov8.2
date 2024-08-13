import os
import sys

'''

    此脚本会直接重命名文件，请在使用前备份重要文件。
    脚本会保留原始文件的扩展名。
    文件会按照字母顺序排序后进行重命名，以确保一致性。
    如果文件夹中已存在与新命名模式相同的文件名，可能会导致错误。在实际使用中，你可能需要添加额外的逻辑来处理这种情况。
    在命令行中运行脚本，提供文件夹路径和新文件名前缀作为参数：
    python rename_files.py /path/to/folder new_prefix_
'''
def rename_files(folder_path, prefix):
    # 确保文件夹路径存在
    if not os.path.isdir(folder_path):
        print(f"错误: 文件夹 '{folder_path}' 不存在")
        return

    # 获取文件夹中的所有文件
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # 对文件进行排序，以确保重命名的顺序
    files.sort()

    # 重命名文件
    for index, filename in enumerate(files, start=1):
        # 获取文件扩展名
        file_extension = os.path.splitext(filename)[1]
        
        # 创建新的文件名
        new_filename = f"{prefix}{index}{file_extension}"
        
        # 构建完整的文件路径
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        
        # 重命名文件
        os.rename(old_file, new_file)
        print(f"已重命名: {filename} -> {new_filename}")

    print(f"重命名完成。共处理 {len(files)} 个文件。")

if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) != 3:
        print("使用方法: python script.py <folder_path> <prefix>")
        sys.exit(1)

    folder_path = sys.argv[1]
    prefix = sys.argv[2]

    rename_files(folder_path, prefix)
