这段代码的主要作用是将VOC（Visual Object Classes）格式的数据集转换为YOLO（You Only Look Once）格式的数据集。具体来说，它将XML格式的标注文件转换为YOLO所需的TXT格式。

主要功能：
1. 读取VOC格式的XML标注文件
2. 解析XML文件中的对象边界框信息
3. 将边界框坐标从VOC格式（xmin, ymin, xmax, ymax）转换为YOLO格式（中心x, 中心y, 宽度, 高度），并进行归一化
4. 生成YOLO格式的TXT标注文件
5. 可选择是否复制图像文件到新的目录

使用教程：

1. 确保你有以下目录：
   - 包含原始图像的目录
   - 包含VOC格式XML标注文件的目录
   - 用于保存YOLO格式TXT文件的目录
   - （可选）用于保存复制图像的目录

2. 在代码的最后，设置正确的参数：

```python
if __name__ == '__main__':
    VOC2Yolo(
        class_num={'71': 0, '73': 1, '75': 2, '77': 3, '79': 4},  # 类别映射字典
        voc_img_path=r'path/to/your/image/directory',  # 原始图像目录
        voc_xml_path=r'path/to/your/xml/directory',    # XML标注文件目录
        yolo_txt_save_path=r'path/to/save/txt/files',  # 保存YOLO格式TXT文件的目录
        yolo_img_save_path=r'path/to/save/images'      # （可选）保存复制图像的目录
    )
```

3. 调整 `class_num` 字典以匹配你的数据集类别。键是VOC标签，值是对应的YOLO类别索引。

4. 运行脚本：
   ```
   python script_name.py
   ```

5. 脚本执行后，它将：
   - 读取每个XML文件
   - 转换标注信息为YOLO格式
   - 在指定目录中创建对应的TXT文件
   - 如果指定了 `yolo_img_save_path`，还会复制图像文件

6. 转换过程中，脚本会显示处理进度。

注意事项：
1. 确保你有足够的磁盘空间来存储生成的文件。
2. 这个脚本假设图像文件是 .jpg 格式。如果你的文件格式不同，需要修改代码。
3. 如果XML文件中没有图像尺寸信息，脚本会尝试读取图像文件来获取尺寸。
4. 如果遇到类别标签不在 `class_num` 字典中的情况，脚本会跳过该标注并打印警告。
5. 确保你的环境中安装了所需的库：`lxml`和`opencv-python`（cv2）。

这个工具对于需要将VOC格式数据集转换为YOLO格式的研究人员和开发者非常有用，特别是在准备目标检测任务的训练数据时。