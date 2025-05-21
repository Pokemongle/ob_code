# 3.1 The problem with modeling long sequences
rnn 无法同时考虑所有的 token，只能最后一个 hidden_state 储存所有的 token 状态
self_attention 的底层原理是 dot product 可以计算两个 vector 之间的相似度
# 3.3 simplified self-attention
计算 attention 的步骤：
输入4个 token，以第2个为例
token2对所有的 token（包括自己）分别进行点乘，得到维度为4的 atten_weights 注意力权重，然后每个 token embedding 分别乘以对应的 atten_weight，再把乘了权重的 token embedding 相加获得一个新的 context_vec向量，维度和每个 token 相同
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202505180304754.png)

# 3.4 trainable weights-self attention
创建继承 `nn.Module` 的注意力机制计算 module
`__init__(self, d_in, d_out, qkv_bias=False)`
- `d_in` 是 token 的维度
- `d_out` 是 context_vec 和 W_qkv 的维度
- 先 `super().__init__()`
- 返回 `context_vec`

# 3.5 Hiding future words with causal Attention
mask 的构建
1. 提取矩阵对角线上方的元素为1，其余为0
	`torch.triu(torch.ones(context_length, context_length), diagonal=1)`
2. 根据构造的矩阵对 attn_scores 矩阵进行填充
	`attn_scores = attn_scores.masked_fill(self.mask.bool()[: num_tokens, : num_tokens], -torch.inf) `
	这样可以便捷地使用 softmax 函数
	