from tabnanny import verbose
from ultralytics import YOLO, data
import ultralytics
if __name__ == '__main__':
    # data = r'D:/Workspace/YOLO/models/ultralytics/datasets/car/car.yaml'
    # model = YOLO('yolov8n.pt')  # Load model
    # model.train(data=data,epochs=100,batch=16,plots=True,verbose=True)
    # data = r'D:\Workspace\datasets\wgsid\wgsid0\data.yaml'
    #data = r'D:\datasets\wgsid\out\data.yaml'
    #data = r'D:\datasets\autolabel\89\augmented_data\out\data.yaml'
    #data = r'D:\datasets\all\out\data.yaml'
    data=r'D:\dataset\temp\temp\data.yaml'
    model = YOLO('yolov8n.yaml')  # Load model
    model.train(
        data=data,
        epochs=500,  # 训练200轮
        batch=12,  # 每批次12张图片
        imgsz=640,  # 输入图像尺寸
        workers=4,  # 多进程数量
        optimizer='SGD',  # 优化器设置为SGDv 
        lr0=0.01,  # 初始学习率
        momentum=0.937,  # 动量``
        patience=10,  # 提前停止训练
        weight_decay=0.0005,  # 权重衰减
        save_period=50,  # 每10轮保存一次权重
        plots=True,  # 绘制训练过程图表
        verbose=True, # 显示详细信息
        project='runs/train',  # 保存训练结果的文件夹
        name='exp',  # 保存训练结果的文件夹
    )  #
