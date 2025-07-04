create a new array from the original array based on a filter array 
How to generate the filter array?
1. Write a filter array 	
```python
arr = np.array([1, 2, 3, 4, 5])
filter_arr = [False, True, False, True, False]
newarr = arr[filter_arr] # [2, 4]
```
2. Generate a filter array from the original array based on some conditions 
```python 
arr = np.array([1, 2, 3, 4, 5])
filter_arr = []
for elem in arr:
	if elem % 2 == 1:
		filter_arr.append(True)
	else:
		filter_arr.append(False)
newarr = arr[filter_arr] # [1, 3, 5]
```
3. Directly from the original array 
```python 
arr = np.array([1, 2, 3, 4, 5])
filter_arr = arr % 2 == 1
newarr = arr[filter_arr] # [1, 3, 5]
```
