from itertools import count
import cv2
import os
from ultralytics import YOLO

# 加载 YOLOv8 模型
model = YOLO(r'runs\detect\train14\weights\best.pt')

# 定义图片文件夹路径
img_path = r'D:\Workspace\datasets\wgsid\wgsid2\test\images\SVB_20180427_152312131_HDR_rotate.jpg'

results=model.predict(source=img_path)


counter={}
for result in results:
    for box in result.boxes.cpu().numpy():
        cls=int(box.cls[0])
        counter[cls]=counter.get(cls,0)+1

img=cv2.imread(img_path)
for i,(cls,count) in enumerate(counter.items()):
    text=f"{model.names[cls]}:{count}"
    cv2.putText(img,text,(10,10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

cv2.imshow('result',img)
cv2.waitKey(0)
cv2.destroyAllWindows()