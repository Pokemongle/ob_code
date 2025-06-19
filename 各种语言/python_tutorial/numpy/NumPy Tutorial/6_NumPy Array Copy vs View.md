copy 复制原 array，有自己的数据
view 不复制原 array，没有自己的数据
感觉 view 类似于指针，而 copy 是复制了一个对象
```python
arr = np.array([1,2,3,4,5])
x = arr.copy()
y = arr.view()
arr[0]=42
print(x) # [1,2,3,4,5]
print(y) # [42,2,3,4,5]

# change values in view?
y[0]=100
print(arr) # [100,2,3,4,5]
```

# check if array owns its data
`print(x.base) # None`
`print(y.base) # same value as array`