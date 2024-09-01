from tabnanny import verbose
from ultralytics import YOLO, data
if __name__ == '__main__':
    model = YOLO(r'runs\train\exp_yolov8s-CCFM-ADown6\weights\best.pt')  # Load model
    rels = model.predict(source=r'D:\datasets\grape\origin\花蕾分离期',save=True,visualize=False,save_txt=True)# Display architecture