# Bag of Tricks for Image Classification with Convolution Neural Networks

# 20200208
1. (Tricks升级版: Compounding the Performance Improvements of Assembled Techniques in a Convolutional Neural Network)[https://arxiv.org/pdf/2001.06268.pdf],[其tensorflow官方实现]https://github.com/clovaai/assembled-cnn)

2. (Big-little net: An efficient multi-scale feature representation for visual and speech recognition)[https://arxiv.org/abs/1807.03848v2], [其pytorch官方实现](https://github.com/IBM/BigLittleNet)

3. 




## GluonCV:
> [GluonCV](https://github.com/dmlc/gluon-cv)

#### 训练技巧

| 参考文献                                                         | 隶属章节 | Tricks |
| ------------------------------------------------------------ | -------- | -------- |
| [《Bag of Tricks for Image Classification with Convolution Neural Networks》](https://arxiv.org/pdf/1812.01187v2.pdf)   | bag      | ☆☆☆☆☆    |
| [《Understanding the difficulty of training deep feedforward neural networks》](http://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf) | 2.1 Baseline Training Procedure      | Xavier初始化     |
| [《A Method for Solving a Convex Programming Problem with Convergence Rate O(1/K2)》](http://mpawankumar.info/teaching/cdt-big-data/nesterov83.pdf)    | 2.1 Baseline Training Procedure       | Nesterov Accelerated Gradient（NAG）加速优化   |
| [《Don’t decay the learning rate, increase the batch size》](https://book.douban.com/subject/6424904/) | 3.1. Large-batch training      | 保持学习率增加Batch Size 的策略    |
| [《Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour》](https://book.douban.com/subject/19952400/) | 3.1. Large-batch training       | Linear scaling learning rate 等比例增大学习率      |
| [《Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour》](https://book.douban.com/subject/19952400/) | 3.1. Large-batch training       | Learning rate warmup 学习率预热     |
| [《Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour》](https://book.douban.com/subject/19952400/) | 3.1. Large-batch training       | zero γ initialization 将所有残差块中的最后一个BN中的初始化设置成0     |
| [《Highly scalable deep learning training system with mixed-precision: Training imagenet in four minutes》](https://book.douban.com/subject/19952400/) | 3.1. Large-batch training       | No bias decay 无偏置衰减      |
| [《Mixed precision training》](https://book.douban.com/subject/19952400/) | 3.2. Low-precision training      | Low-precision training 低精度训练      |
| [《Training and investigating residual nets.》](http://torch.ch/blog/2016/02/04/resnets.html) | 4.2. ResNet Tweaks     | ResNet-B：大小1x1、步长2的卷积会造成3/4的信息丢失      |
| [《Rethinking the inception architecture for computer vision.》](https://book.douban.com/subject/19952400/) | 4.2. ResNet Tweaks     | ResNet-C：7x7-3x3x3      |
| [《Inspired by ResNet-B》](https://book.douban.com/subject/19952400/) | 4.2. ResNet Tweaks      | ResNet-D： 卷积改为sride=1，同时在前面加上一个2x2，步长2的平均池化     |
| [《SGDR: stochastic gradient de- scent with restarts.》](https://book.douban.com/subject/19952400/) | 5.1. Cosine Learning Rate Decay      | 余弦学习率衰减      |
| [《Rethinking the inception architecture for computer vision.》](https://book.douban.com/subject/19952400/) | 5.2. Label Smoothing     | 一种正则化方法，解决的问题也是为了防止过拟合      |
| [《Distillingtheknowledge in a neural network》](https://book.douban.com/subject/19952400/) | 5.3. Knowledge Distillation      | 将集成模型的泛化能力迁移到小模型。      |
| [《mixup: Beyond empirical risk minimization》](https://book.douban.com/subject/19952400/) | 5.4. Mixup Training      | 混合数据增强的策略     |


#### base model

1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)
He, Kaiming, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. “Deep residual learning for image recognition.” In Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 770-778. 2016.

2(1,2,3,4,5,6,7,8)
He, Kaiming, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. “Identity mappings in deep residual networks.” In European Conference on Computer Vision, pp. 630-645. Springer, Cham, 2016.

3(1,2)
Redmon, Joseph, and Ali Farhadi. “Yolov3: An incremental improvement.” arXiv preprint arXiv:1804.02767 (2018).

4(1,2,3,4,5,6)
Howard, Andrew G., Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang, Tobias Weyand, Marco Andreetto, and Hartwig Adam. “Mobilenets: Efficient convolutional neural networks for mobile vision applications.” arXiv preprint arXiv:1704.04861 (2017).

5(1,2,3,4)
Sandler, Mark, Andrew Howard, Menglong Zhu, Andrey Zhmoginov, and Liang-Chieh Chen. “Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation.” arXiv preprint arXiv:1801.04381 (2018).

6
Krizhevsky, Alex, Ilya Sutskever, and Geoffrey E. Hinton. “Imagenet classification with deep convolutional neural networks.” In Advances in neural information processing systems, pp. 1097-1105. 2012.

7(1,2,3,4)
Huang, Gao, Zhuang Liu, Laurens Van Der Maaten, and Kilian Q. Weinberger. “Densely Connected Convolutional Networks.” In CVPR, vol. 1, no. 2, p. 3. 2017.

8(1,2,3)
Szegedy, Christian, Vincent Vanhoucke, Sergey Ioffe, Jon Shlens, and Zbigniew Wojna. “Rethinking the inception architecture for computer vision.” In Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 2818-2826. 2016.

9(1,2,3,4,5,6,7,8)
Karen Simonyan, Andrew Zisserman. “Very Deep Convolutional Networks for Large-Scale Image Recognition.” arXiv technical report arXiv:1409.1556 (2014).

10(1,2)
Iandola, Forrest N., Song Han, Matthew W. Moskewicz, Khalid Ashraf, William J. Dally, and Kurt Keutzer. “Squeezenet: Alexnet-level accuracy with 50x fewer parameters and< 0.5 mb model size.” arXiv preprint arXiv:1602.07360 (2016).

11(1,2,3)
Zagoruyko, Sergey, and Nikos Komodakis. “Wide residual networks.” arXiv preprint arXiv:1605.07146 (2016).

12(1,2,3,4,5,6,7)
Xie, Saining, Ross Girshick, Piotr Dollár, Zhuowen Tu, and Kaiming He. “Aggregated residual transformations for deep neural networks.” In Computer Vision and Pattern Recognition (CVPR), 2017 IEEE Conference on, pp. 5987-5995. IEEE, 2017.

13(1,2)
Zhang, Hongyi, Moustapha Cisse, Yann N. Dauphin, and David Lopez-Paz. “mixup: Beyond empirical risk minimization.” arXiv preprint arXiv:1710.09412 (2017).

14(1,2,3,4)
Hu, Jie, Li Shen, and Gang Sun. “Squeeze-and-excitation networks.” arXiv preprint arXiv:1709.01507 7 (2017).

15(1,2)
Howard, Andrew, Mark Sandler, Grace Chu, Liang-Chieh Chen, Bo Chen, Mingxing Tan, Weijun Wang et al. “Searching for mobilenetv3.” arXiv preprint arXiv:1905.02244 (2019).

16
Christian Szegedy, Wei Liu, Yangqing Jia, Pierre Sermanet, Scott Reed, Dragomir Anguelov, Dumitru Erhan, Vincent Vanhoucke, Andrew Rabinovich “Going Deeper with Convolutions” arXiv preprint arXiv:1409.4842 (2014).

#### bcd
 
ResNet50_v1_int8 is a quantized model for ResNet50_v1.

ResNet_v1b modifies ResNet_v1 by setting stride at the 3x3 layer for a bottleneck block.

ResNet_v1c modifies ResNet_v1b by replacing the 7x7 conv layer with three 3x3 conv layers.

ResNet_v1d modifies ResNet_v1c by adding an avgpool layer 2x2 with stride 2 downsample feature map on the residual path to preserve more information.


#### se[14]


#### resnext[12]

ResNext50_32x4d

32: cardinality: Number of groups
4: bottleneck_width: Width of bottleneck block

#### mobilev1 - v3


#### bn\gn

#### SqueezeNet

#### DenseNet

#### nasnet