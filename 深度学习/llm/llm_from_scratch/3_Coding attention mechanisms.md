# 3.1 The problem with modeling long sequences
rnn 无法同时考虑所有的 token，只能最后一个 hidden_state 储存所有的 token 状态
self_attention 的底层原理是 dot product 可以计算两个 vector 之间的