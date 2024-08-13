from ultralytics import YOLO
# 加载 YOLOv8 模型
model = YOLO(r'yolov8n.pt')  # Load model
# 导出模型为 ONNX 格式
model.export(format='onnx')
