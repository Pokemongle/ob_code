[Lab 08](https://cs61a.vercel.app/lab/lab08/index.html)

# Q1 - repeated
简单的，搞清楚题目在问什么，找迭代器中第 1 个连续出现 k 次的数
算法复杂度：`O(n)`

# Q2 - merge
关键点在于，两个 iterator 都是（非严格）递增的

# Q3 - deep_len
数一个列表中有多少个元素，也就是多少个值，要考虑嵌套列表。
这是递归的写法，已经相对高效。
还有*栈的写法*，待补充

# Q4 - add leaves
树结构给深度为 n 的子节点添加树叶
注意防止给新添加的子叶添加新的子叶陷入无限递归

# Q5 subseqs
Find the all subsets of a set
Use the recursion leap of faith : )
Check if the base case is `return []` or `return [[]]`