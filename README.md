# 图片相似度算法

## 1 余弦相似度计算

把图片表示成一个向量，通过计算向量之间的余弦距离来表征两张图片的相似度。

- 当夹角为0°，两个向量同向，相当于相似度最高，余弦值为1。
- 当夹角90°，两个向量垂直，余弦为0。
- 当夹角180°，两个向量反向，余弦为-1。

**用途**

余弦相似度被大量用于对比：如人脸对比、声音对比，来快速判断两个图片或者两段声音的相似度，进而判断是不是来自同一个人。

当一个图像或者声音样本具有n维的特征，我们就可以把他认为是n维向量，两个样本使用余弦相似度比对时，就是对两个n维向量的夹角余弦值，其大小进行衡量。

特别的，当我们拥有一个训练完成的分类神经网络，理论上这个神经网络在最后一层全连接层的输入，就是神经网络提取的特征（因为最后一层全连接层借由这些数据完成了分类任务）。

余弦相似度而非算法，求出余弦相似度后，到底阈值如何界定（值大于多少认为是样本来自同一类），往往需要依次用不同的阈值数值对全部数据集进行测试，挑选效果最好的数值作为阈值
尽管余弦相似度用法类似欧氏距离（欧氏距离也可以用于比对：把n维特征认为是n维空间的一个点，当两个样本对应的点，距离足够近认为认为来自同一类），但余弦相似度并不符合距离定义。
余弦相似度范围[-1,1]包含负值，不便于使用，改进方法有：
- 将余弦相似度用于正空间，对于各个维度均为正的向量，可以保证余弦相似度非负（该空间的夹角被限定在0-90，或者根据公式，内积恒为正）。
- 用1减余弦相似度，此时结果范围为[0,2]，且值越小表示越接近（类似欧氏距离）。

**余弦相似度计算代码**（定义后可以直接调用，a,b为n维的array类数据特征）

```
def simcos(a,b):
    dot = sum(a*b)
    mod_a = sum(a**2)**0.5
    mod_b = sum(b**2)**0.5
    return dot/(mod_a*mod_b)

#用法示例

#向量维度可任意，示例使用2维的数据
a = np.array([0,1]) 
b = np.array([1,0])
print(a.shape,b.shape) #(2,) (2,)
print(simcos(a,b)) #0.0 #两者相似度为0
```