# 如何调参
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

# 防止单一验证集质量太差的方法 ——cross validation
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202503170032824.png)
！不能根据测试集表现的好坏来调参，而是根据验证集的表现调整模型或者调整参数，选择验证集表现最佳的模型用来测试，达到自己满意的测试结果即可，不要追求测试集上结果的绝对完美。