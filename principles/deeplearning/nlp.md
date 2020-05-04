## nlp
### Embedding
将每一个词 映射为数组
one hot 
希望通过无标注数据，判断词汇相似性
使用现有已经有的embedding -腾讯词向量
预训练语言模型

### 马尔可夫过程和隐马尔可夫过程HMM
每一位置只与前一步有关 ht 与 ht-1有关
h(hidden,股票的开关是否连续震荡，nlp中的语义) + x ->y


但是要看整个句子的语义更客观，所以隐马尔可夫并不是太准确

### RNN、LSTM
rnn
x enbedding 字向量词向量的嵌入
yt = softmax(weight+b)
ht = Activation(wt-1+wx+bh)

lstm
ft Ct It Ot 
Ct
ht
sigmoid 作为门控的机制

语句可长可短，padding token

### google cloud platform



### 文本分类


### Bert