# yolov4_mask_detect
基于yolov4的口罩检测，采用darknet yolov4，dartnet部分的使用和编译请参考：
https://github.com/AlexeyAB/darknet
这里把dada目录和cfg共享出来
数据集参考的以下项目
https://github.com/xiaomujiang/Object_Dete_Masking
图片比较少，易于上手，也可以使用其他开源项目数据集

#python数据转换文件说明
generatetxt.py 用来生产训练和验证清单txt
voc_label.py用来进行voc数据集到yolo数据集的转换，这里我把转化的结果和图片放到同一个目录label里
#运行指令
训练指令
darknet.exe detector train data/mask/mask.data cfg/yolov4-mask.cfg yolov4.conv.137
摄像头指令
darknet.exe detector demo data/mask/mask.data cfg/yolov4-mask.cfg backup/yolov4-mask_last.weights -c 0 -thresh 0.75
这里的-thresh 0.75是最低得分阈值
图片测试指令
darknet.exe detector test data/mask/mask.data cfg/yolov4-mask.cfg backup/yolov4-mask_last.weights 
#关于重复检测
yolov4重复检测问题通过把yolov4-mask.cfg中nms_kind=greedynms改成nms_kind=diounms来进行优化，也就是在重叠面积过滤基础上又加上了中心点距离过滤。
