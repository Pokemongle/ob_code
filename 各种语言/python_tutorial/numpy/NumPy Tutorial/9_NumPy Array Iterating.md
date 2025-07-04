use `np.nditer`
	`nd` stands for n-dim
```python 
import numpy as np
arr = np.array([[1,2,3,4], [5,6,7,8]])
for x in np.nditer(arr): # no need for nested for loop
	print(x)

# iterate with defined dtype
for x in np.nditer(arr, flags=['buffered'], op_dtypes='S'): # op means operands
	print(x)

# iterate with step 
for x in np.nditer(arr[:,::2]):
	print(x) # 1 3 5 7
```
	
use `np.ndenumerate`
```python 
import numpy as np
arr = np.array([[1,2,3,4], [5,6,7,8]])
for idx, x in np.ndenumerate(arr):
	print(idx, x)
```
output:
```python 
(0, 0) 1
(0, 1) 2
(0, 2) 3
(1, 0) 4
(1, 1) 5
(1, 2) 6
```