from ultralytics import YOLO
model = YOLO('ultralytics/cfg/models/v8/yolov8test.yaml')
model.train(data="coco128.yaml", cfg="ultralytics/cfg/default.yaml", epochs=100,workers=0,batch=12)