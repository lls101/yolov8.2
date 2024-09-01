import torch
from torchsummary import summary
from thop import profile

# 加载模型
model = torch.load(r'runs\train\exp41\weights\best.pt', map_location=torch.device('cpu'))['model'].float()

# 打印模型结构和参数数量
print(model)
total_params = sum(p.numel() for p in model.parameters())
print(f"Total parameters: {total_params}")

# 计算层数
def count_layers(model):
    return sum(1 for _ in model.modules())

num_layers = count_layers(model)
print(f"Number of layers: {num_layers}")

# 计算 GFLOPs
input = torch.randn(1, 3, 640, 640)  # 假设输入尺寸为 640x640
macs, params = profile(model, inputs=(input, ))
gflops = macs / (1000**3)
print(f"GFLOPs: {gflops:.1f}")

# 检查是否有梯度
gradients = sum(1 for p in model.parameters() if p.requires_grad)
print(f"Parameters with gradients: {gradients}")
