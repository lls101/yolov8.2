from re import split
from tabnanny import verbose
from ultralytics import YOLO, data
if __name__ == '__main__':
    data = r'D:\datasets\test\out\data.yaml'
    model = YOLO(r'runs\train\exp9\weights\best.pt')  # Load model
    rels = model.val(data=data,split='test',project='runs/val',  # 保存训练结果的文件夹
        name='exp')# Display architecture
    print(rels)