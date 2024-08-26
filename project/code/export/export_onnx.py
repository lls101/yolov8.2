from ultralytics import YOLO
# 加载 YOLOv8 模型
model = YOLO(r'D:\Workspace\models\ultralytics8.2\runs\train\exp27\weights\best.pt')  # Load model
# 导出模型为 ONNX 格式
model.export(format='onnx')
