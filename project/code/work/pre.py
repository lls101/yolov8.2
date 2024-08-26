from tabnanny import verbose
from ultralytics import YOLO, data
if __name__ == '__main__':
    model = YOLO(r'runs\train\exp30\weights\best.pt')  # Load model
    rels = model.predict(source=r'D:\datasets\autolabel\00\augmented\split_data\test\images',save=True,visualize=False,save_txt=True)# Display architecture