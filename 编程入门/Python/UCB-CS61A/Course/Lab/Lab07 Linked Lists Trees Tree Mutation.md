[Lab 07](https://cs61a.vercel.app/lab/lab07/index.html)
挺简单的，就是各种递归的写法
# Q1: WWPD: Linked Lists
被卡住的点主要在于没仔细看 Link 的定义
`Link(first, rest)` 中 `first` 必须传一个值进去没有默认值
`rest` 必须是 ` Link ` 类型
# Q2: Reverse Link
写一个逆转链表，用到 `Link(first, rest)` 来构造就很简单，不需要在原来链表上修改实在是太友好了

# Q3: Label Multiplier
理清楚逻辑之后依旧是内置函数+递归的套路，注意：
	每次递归是否要 `return` 这个递归函数
	以及递归函数只调用一次还是对于每个 sub object 都要调用

# Q4: Store Digits
对 Q 2 中逆转链表的应用

# Q5: Cumulative Mul
和 Q 3 类似，把逻辑理清楚，以及内置函数经典列表存值

---
# Optional Questions
# Q6: Cycles
用列表存储遍历过的值 `O(n)`
[Floyd Algorithm](https://www.bilibili.com/video/BV1qj411w7Vz/?spm_id_from=333.337.search-card.all.click&vd_source=4ab0010a787e254ae5cffb27e35dce8b) `O(1)`


