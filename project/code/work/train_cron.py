from ultralytics import YOLO
import csv
import os

def train_and_save_results(model_name, data_path, results_file):
    # 加载模型
    if model_name.startswith('yolov8'):
        model = YOLO(f'{model_name}.yaml')
    else:
        model = YOLO(f'{model_name}.pt')  # For YOLOv5 and YOLOv7, use pre-trained weights

    # 获取模型信息
    num_layers = sum(1 for _ in model.model.parameters())
    num_params = sum(p.numel() for p in model.model.parameters())
    num_gradients = sum(p.numel() for p in model.model.parameters() if p.requires_grad)
    
    # 尝试获取 GFLOPs，如果失败则设为 'N/A'
    try:
        info = model.info(verbose=False)
        gflops = info['GFLOPs'] if isinstance(info, dict) and 'GFLOPs' in info else 'N/A'
    except:
        gflops = 'N/A'

    # 训练模型
    results = model.train(
        data=data_path,
        epochs=500,
        batch=12,
        imgsz=640,
        workers=4,
        optimizer='SGD',
        lr0=0.01,
        momentum=0.937,
        patience=50,
        weight_decay=0.0005,
        save_period=50,
        plots=True,
        verbose=True,
        project='runs/train',
        name=f'exp_{model_name}'
    )

    # 保存结果
    metrics = results.results_dict
    file_exists = os.path.isfile(results_file)
    with open(results_file, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:  # 如果文件不存在，写入表头
            writer.writerow(['Model', 'Layers', 'Parameters', 'Gradients', 'GFLOPs', 'mAP50', 'mAP50-95'])
        writer.writerow([
            model_name, 
            num_layers, 
            num_params, 
            num_gradients, 
            gflops,
            metrics['metrics/mAP50(B)'], 
            metrics['metrics/mAP50-95(B)']
        ])

if __name__ == '__main__':
    data_path = r'D:\datasets\temp\aug_test\out\data.yaml'
    results_file = r'D:\datasets\wgsid\output\model_comparison_results.csv'

    # 确保结果文件存在
    os.makedirs(os.path.dirname(results_file), exist_ok=True)

    # 训练不同的模型
    # models = [ 'yolov8s-MobileNetV3','yolov8s-VanillaNet-BiFPN','yolov8s-Vanillanet','yolov8s-EfficientViT2','yolov8s-GhostNetV2','yolov8s-LSKA','yolov8-SwinTransformer','yolov8s',
    #         'yolov8s-FasterNet','yolov8s-LSKNet']
    #models = [ 'yolov8s-AKConv','yolov8s-AFPNHead3','yolov8s-C2f-AKConv','yolov8s-C2f-DSConv','yolov8s-DSConvHead','yolov8s-ghost-p2','yolov8s-ShuffleNetV2','yolov8s-v9TwoBackbone']
    #models = ['yolov8s-SPDConv']
    #models = ['yolov8s-DynamicConv','yolov8s-C2f-GhostModuleDynamicConv','yolov8s-SPDConv']
    #models = ['yolov8s-C2f-FasterBlock','yolov8s-C2f-RFAConv','yolov8s-DySample']
    # models = ['yolov8s-SAHead','yolov8s-SAConv','yolov8s-CCFM-ADown','yolov8s-CSPHet','yolov8s-CSPPC','yolov8s-C2f-DualConv','yolov8s-MSBlock']
    #models = ['yolov8-MobileNetV4','yolov8-CCFM-ADown','yolov8-C2f-ScConv','yolov8s-C2f-ScConv']
    models = ['yolov8s-CCFM-ADown']
    for model_name in models:
        train_and_save_results(model_name, data_path, results_file)

    print(f"All training completed. Results saved in {results_file}")


