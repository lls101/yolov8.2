from sympy import false
from ultralytics import RTDETR


'''
不建议使用下面的写法，注意batch大小
'''
# # Load a model
# model = RTDETR("ultralytics/cfg/models/rt-detr/rtdetr-resnet50.yaml")  # build a new model from scratch

# # Use the model
# model.train(data=r"coco128.yaml", epochs=100,workers=0,batch=12)  # train the model


if __name__ == '__main__':
    model = RTDETR('ultralytics\cfg\models\improve\yolov8_rtdetr.yaml')
    model.train(data='coco128.yaml',
                imgsz=640,
                epochs=200,
                batch=12,
                workers=0,
                device=0,
                optimizer='SGD', # 这里可以使用两个优化器SGD 和AdamW其它的可能会导致模型无法收敛
                )