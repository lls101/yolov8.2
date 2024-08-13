from re import split
from tabnanny import verbose
from ultralytics import YOLO, data
if __name__ == '__main__':
    model = YOLO(r'D:\Workspace\YOLO\models\ultralytics\runs\train\exp22\weights\best.pt')  # Load model
    rels = model.val(data=r'D:\Downloads\wsfid\out\data.yaml',split='test',project='runs/val',  # 保存训练结果的文件夹
        name='exp')# Display architecture
    print(rels)