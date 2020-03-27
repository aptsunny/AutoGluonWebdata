# Nas 网络结构搜索

# Outline

## EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks
> [paper](https://arxiv.org/pdf/1905.11946.pdf)

> [官方实现](https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet)

EfficientNet-B0, Its main building block is mobile inverted bottleneck MBConv

[MnasNet: Platform-aware neural architecture search for mobile](https://www.zhihu.com/question/287988785/answer/469932620)

[Mobilenetv2: Inverted residuals and linear bottlenecks](https://www.zhihu.com/question/265709710/answer/298245276)

to which we also add squeeze-and-excitation optimization

[Squeeze-and-excitation net- works](https://zhuanlan.zhihu.com/p/47494490)

EfficientNet-B0 are α = 1.2, β = 1.1, γ=1.15, under constraint of α·β2·γ2 = 1.92027 ≈2

Our method solves this issue by only doing search once on the small baseline network (step 1), and then use the same scaling coefficients for all other models (step 2)

> /Users/ysunmzn/Library/Caches/PyCharm2018.3/remote_sources/-632611853/-1141404460/autogluon/nas/efficientnet.py


## ProxyLessNAS: Direct Neural Architecture Search On Target Task And Hardware
> [官方实现](https://github.com/MIT-HAN-LAB/ProxylessNAS)


> to be continue

### outline
|                                                          | 要点总结 | 具体实现 |
| ------------------------------------------------------------ | -------- | -------- |
|  propose   | proxyless: proxy tasks restricts the block diversity and harms performance      | ☆☆☆☆☆    |
|  method   | path-level binarization （using the binary gates and only one path of activation is active in memory）     | ☆☆☆☆☆    |
|  Highlight  | training procedure (When training weight parameters, we first freeze the architecture parameters and stochastically sample binary gates according to Eq. (2) for each batch of input data. Then the weight parameters of active paths are updated via standard gradient descent on the training set (Figure 2 left). When training architecture parameters, the weight parameters are frozen, then we reset the binary gates and update the architecture parameters on the validation set (Figure 2 right). These two update steps are performed in an alternative manner. Once the train- ing of architecture parameters is finished, we can then derive the compact architecture by pruning redundant paths. In this work, we simply choose the path with the highest path weight.)       | ☆☆☆☆☆    |
|  method   | gradient-based approach (the architecture parameters are not directly involved in the computation graph)      | ☆☆☆☆☆    |
|  Highlight   | [BinaryConnect:Training deep neural networks with binary weights during propagations: ](https://github.com/MatthieuCourbariaux/BinaryConnect) architecture parameters can be approximately estimated using ∂L/∂gi in replace of ∂L/∂pi      | ☆☆☆☆☆    |
|  contribute   | t****he architecture parameters would also require roughly N times GPU memory compared to training a compact model. (we consider factorizing the task of choosing one path out of N candidates into multiple binary selection tasks.)      | ☆☆☆☆☆    |
|  contribute   | latency is non-differentiable. (We incorporate the expected latency of the network into the normal loss function by multiplying a scaling factor λ2(> 0) which controls the trade-off between accuracy and latency.)      | ☆☆☆☆☆    |
|  method   | REINFORCE-BASED APPROACH:we can utilize REINFORCE to train binarized weights as well. Consider a network that has binarized parameters α    | ☆☆☆☆☆    |


### contribute
这个工作能够减少200倍的GPU hours的原因在于通过先验极大地减小了网络结构的搜索空间

将 NAS 制定为一个路径级修剪过程，直接训练一个包含所有候选路径的过参数化网络。在训练期间，明确地引入结构参数以学习哪些路径是冗余的，而在训练结束时修剪这些冗余路径以获得紧凑的优化结构。通过这种方式，只需要在结构搜索期间训练单个网络而无需任何元控制器，从而减少搜索花费的 GPU 小时数

1.将搜索成本从40000 GPU hours降低到200 GPU hours；

2.搜索过程的内存消耗与普通紧凑模型在一个量级

3.将模型的latency作为优化目标之一

4.直接在目标数据集上优化，不需要使用代理数据集(CIFAR-10)+transfer

### result

On ImageNet, our model achieves 3.1% better top-1 accuracy than MobileNetV2, while being 1.2× faster with measured GPU latency

### insight
1. GPU prefers shallow and wide model with early pooling;

2. CPU prefers deep and narrow model with late pooling. 

3. Pooling layers prefer large and wide kernel. 

4. Early layers prefer small kernel.

5. Late layers prefer large kernel

> Large kernel > small kernel 的原因主要是采用 MBConv (depthwise + separable) 计算量为 HxWxC_in (k^2 + C_out)，两个 3x3 在计算量上就比 5x5 要大了。

> downsample （降采样时），NAS 往往会让 channel 更多（expansion ratio），以更好的保留信息。


## Dynamic Mini-batch SGD for Elastic Distributed Training: Learning in the Limbo of Resources

Different tasks may receive varying numbers of machines at different time, a setting we call elastic distributed training.

AsyncSGD, however, converges radically differently from synchronous mini-batch SGD [49, 36, 52]. It is also difficult for async- SGD to match the model accuracy trained with synchronized mini-batch SGD with similar computation budget [5, 2].


|                                                          | 要点总结 | 具体实现 |
| ------------------------------------------------------------ | -------- | -------- |
|  propose   | we focus on extending synchronized mini- batch SGD with momentum into the dynamic training envi- ronment. We aim to minimize the convergence difference when the training environment is constantly changing. There are two straightforward approaches to extend synchronized SGD with momentum.      | ☆☆☆☆☆    |
|  method   | One approach is to fix the mini-batch size but reassign mini-batches across machines when the number of machines changes.     | ☆☆☆☆☆    |
|  method   | The other approach fixes the mini-batch size per machine, and updates the total mini- batch size linearly with the number of machines, while lin- early changing the learning rate at the same time    | ☆☆☆☆☆    |
|  Highlight  | Dynamic Mini-batch Stochastic Gradient Descent (Dy- namic SGD) that smoothly adjusts the learning rate to stabilize the variance changes. | ☆☆☆☆☆  |

