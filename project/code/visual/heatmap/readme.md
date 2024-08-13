# yolov8_heatmap.py

## 一个参数即可关闭绘制框
## 支持优化热力图效果显示
renormalize=TRUE
## 支持8种热力图方法
(GradCAMPlusPlus, GradCAM, XGradCAM, EigenCAM, HiResCAM, LayerCAM, RandomCAM, EigenGradCAM)
## 支持选择多个层去计算热力图。
## 支持单张图片或者一个文件夹的图片进行绘制

# heatmap 
0	weights	str	用于检测视频的权重文件地址（可以是你训练好的，也可以是官方提供的）
1	cfg	str	你选择的权重对应的yaml配置文件，请注意一定要对应否则会报错和不显示图片
2	device	str	设备的选择可以用GPU也可以用CPU
3	method	str	使用的热力图第三方库的版本，不同的版本效果也不一样。
4	layer	str	想要检测的对应层，比如这里设置的是9那么检测的就是第九层
4	backward_type	str	检测的类别
5	conf_threshold	str	置信度阈值，有的时候你的进度条没有满就是因为没有大于这个阈值的图片了
6	ratio	int	YOLOv8一次产生6300张预测框，选择多少比例的图片绘画热力图。