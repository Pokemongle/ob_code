# 1. 如何调参
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202503170028333.png)
train loss 太大：
	模型太简单
	优化不好
train loss 小了：
	valid loss 太大：
		过拟合：
			更多的训练数据
			数据增强
			简化模型
		不匹配：

## 防止单一验证集质量太差的方法 ——cross validation
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202503170032824.png)
！不能根据测试集表现的好坏来调参，而是根据验证集的表现调整模型或者调整参数，选择验证集表现最佳的模型用来测试，达到自己满意的测试结果即可，不要追求测试集上结果的绝对完美。

# 2. Optimization Fails
model 复杂且能收敛但是 loss 不够低
停在了 critical points
	local minimum
	local maximum
	***saddle points***

# 3. Batch and Momentum
## Batch size 的影响
每个 batch 训练更新一次模型
batch size越大，需要的显存越大 
batch size 小，更新一个 epoch 的时间长，反之
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202503170106464.png)
小的 batch size 结果可能更好——why？
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202503170109853.png)
每次 batch update 了之后，loss function 都会改变！
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202503170110967.png)
大小 batch size 的比较
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202503170113749.png)

## Momentum
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202503170118565.png)

# 4. Adaptive Learning Rate
梯度大，lr 小，梯度小，lr 大
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202503170127865.png)
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202503170131255.png)
![](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202503170131255.png)

# 5. Loss Function 的影响
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202503170149618.png)
