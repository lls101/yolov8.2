import torch

# 测试GPU是否可用，如果可以，打印CUDA设备数量和设备名称
if torch.cuda.is_available():
    print(f"Available CUDA devices: {torch.cuda.device_count()}")
    for i in range(torch.cuda.device_count()):
        print(f"CUDA device {i}: {torch.cuda.get_device_name(i)}")
else:
    print("No CUDA devices available.")
