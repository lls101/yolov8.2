from tabnanny import verbose
from ultralytics import YOLO, data
if __name__ == '__main__':
    # data = r'D:/Workspace/YOLO/models/ultralytics/datasets/car/car.yaml'
    # model = YOLO('yolov8n.pt')  # Load model
    # model.train(data=data,epochs=100,batch=16,plots=True,verbose=True)
    # data = r'D:\Workspace\datasets\wgsid\wgsid0\data.yaml'
    data = r'coco128.yaml'
    
    model = YOLO('ultralytics\cfg\models\improve\yolov8test.yaml')  # Load model
    model.train(
        data=data,
        epochs=100,  # 训练200轮
        batch=12,  # 每批次12张图片
        imgsz=640,  # 输入图像尺寸
        workers=4,  # 多进程数量
        optimizer='SGD',  # 优化器设置为SGD
        lr0=0.01,  # 初始学习率
        momentum=0.937,  # 动量
        weight_decay=0.0005,  # 权重衰减
        save_period=10,  # 每10轮保存一次权重
        plots=True,  # 绘制训练过程图表
        verbose=True, # 显示详细信息
        project='runs/train',  # 保存训练结果的文件夹
        name='exp',  # 保存训练结果的文件夹
    )  # Train model

