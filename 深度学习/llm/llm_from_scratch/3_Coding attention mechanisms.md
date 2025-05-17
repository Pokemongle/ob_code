# 3.1 The problem with modeling long sequences
rnn 无法同时考虑所有的 token，只能最后一个 hidden_state 储存所有的 token 状态
self_attention 的底层原理是 dot product 可以计算两个 vector 之间的相似度
# 3.3 固定 weights 产生 context_vec
计算 attention 的步骤：
输入4个 token，以第2个为例
token2对所有的 token（包括自己）分别进行点乘，得到维度为4的 atten_weights 注意力权重，然后每个 token embedding 分别乘以对应的 atten_weight，再把乘了权重的 token embedding 相加获得一个新的 context_vec向量，维度和每个 token 相同
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202505180304754.png)

# 3.4 trainable weights-self attention
