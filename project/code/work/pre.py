from tabnanny import verbose
from ultralytics import YOLO, data
if __name__ == '__main__':
    model = YOLO(r'runs\detect\train24\weights\best.pt')  # Load model
    rels = model.predict(source=r'D:\Workspace\datasets\wgsid\wgsid0\test\images',save=True,visualize=True,save_txt=True)# Display architecture