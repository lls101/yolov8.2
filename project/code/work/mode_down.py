from tabnanny import verbose
from ultralytics import YOLO, data

model = YOLO('yolov10s.yaml')  # Load model
print(model)  # Display architecture


