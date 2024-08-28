from tabnanny import verbose
from ultralytics import YOLO, data
if __name__ == '__main__':
    model = YOLO(r'runs\train\exp\weights\best.pt')  # Load model
    rels = model.predict(source=r'D:\dataset\temp\temp\test\images',save=True,visualize=False,save_txt=True)# Display architecture