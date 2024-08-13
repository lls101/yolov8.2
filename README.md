报错：

import torchvision.transforms.functional_tensor as F_t
ModuleNotFoundError: No module named ‘torchvision.transforms.functional_tensor’
pytorch版本在1.13及以下没问题，但是安装2.0以上会出现此问题

高版本pytorch的torchvision.transforms._functional_tensor名字改了，在前面加了一个下划线，但是torchvision.transforms.augmentation里面的import没把名字改过来，所以会找不到
手动改成以下内容即可

import torchvision.transforms._functional_tensor as F_t

