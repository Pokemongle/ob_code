import numpy as np 
print(f'=============NumPy intro')
# arr = np.array([1, 2, 3, 4, 5])
arr = np.array((1,2,3,4,5))
print(arr)
print(arr.ndim)
print(np.__version__)

# dimensions in numpy 
print(f"=============Dimensions in NumPy")
## 0-d or scalar
arr = np.array(42)
print(arr)
## check dim of the array
print(arr.ndim)
## create array with dim 
arr = np.array([1,2,3,4], ndmin=5)
print(arr)
print(arr.ndim)

# Access elements in ndarray 
print(f"=============Access in NumPy")
arr = np.array([1,2,3,4])
print(arr[0])
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr[0, 1])

# Slicing 
print(f"=============Slicing")
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])
print(arr[4:])
print(arr[-3:-1])
print(arr[::2])
## 2-d slicing 
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr[1,1:3])
print(arr[0:2,1:3])

# Data Types 
## check the data type of an ndarray
print(f"=========numpy data types")
arr = np.array([1,2,3,4])
print(arr.dtype)
arr = np.array(['apple', 'banana', 'carrot'])
print(arr.dtype)
## create an array with dtype and even size
arr = np.array([1,2,3],dtype='S')
print(arr)
print(arr.dtype)
print(arr[0]+arr[1])
arr = np.array([1,2,3,4],dtype='i4')
print(arr)
print(arr.dtype)
## data type convert error 
### this will cause an ValueError
# arr = np.array(['a','2','3'], dtype='i')
## convert array data type 
arr = np.array([1.1,2.1,3.1])
newarr = arr.astype('i')
# newarr = arr.astype(bool)
# newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

# Copy and View in NumPy
print(f"======= Copy vs View")
arr = np.array([1,2,3,4,5])
x = arr.copy()
y = arr.view()
arr[0]=42
print(arr)
print(x)
print(y)
## make changes in the view?
y[0]=32
print(y)
print(arr)
## check if array owns its data
print(x.base)
print(y.base)

# Array shape
print(f"=========== array shape")
arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)
arr = np.array([1,2,3],ndmin=5)
print(arr.shape)

# Reshape
print(f"========Reshape")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr.shape)
print(arr)
newarr = arr.reshape(4,3)
print(newarr.shape)
print(newarr)
newarr = arr.reshape(2,3,2)
print(newarr.shape)
print(newarr)
## reshape into any shape?
#newarr = arr.reshape(3,3) # this will cause an Value Error
## returns copy or view?
print(newarr.base) # a view 
## unknown dimension
newarr = arr.reshape(2,2,-1)
print(newarr.shape)
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr.shape)

# Iterating 
print(f"=============Iterating")
## for loop
### 1-d arr
arr = np.array([1,2,3])
for i in arr:
    print(i)
### 2-d arr
arr = np.array([[1,2,3],[4,5,6]])
for i in arr:
    print(i)
for i in arr:
    for j in i:
        print(j)

## nditer()
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr): # no need for nested for loop
    print(x)
### iterate through the array as a string 
arr = np.array([1,2,3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)
### iterate with step size
arr = np.array([[1,2,3,4],[5,6,7,8]])
for x in np.nditer(arr[:,::2]):
    print(x)
### enumerate 
arr = np.array([[1, 2, 3], [4, 5, 6]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)

# numpy array join
print(f"=============== Join")
## ======== concatenate
## join 2 1-D array 
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1, arr2))
print(arr)
## join 2 2-D array along an axis
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)
## ========= stack
### stack along axis
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=0)
print(arr)
### stack along rows 
arr = np.hstack((arr1, arr2))
print(arr)
### stack along columns 
arr = np.vstack((arr1, arr2))
print(arr)
### stack along depth 
arr = np.dstack((arr1, arr2))
print(arr)
print(arr1.shape)
print(arr2.shape)
print(arr.shape)

# =========== splitting
print(f"=============== Splitting")
## 1-D array
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr) # a list
newarr = np.array_split(arr, 4) # self-adjust
print(newarr)
## 2-D array
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print(newarr)
newarr = np.array_split(arr, 3, axis=1)
print(newarr)
newarr = np.vsplit(arr, 3)
print(newarr)

# ============== searching 
## search for conditions
print(f"=============== Searching")
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x) # a tuple of index
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 1)
print(x)
## searchsort
arr = np.array([5, 6, 7, 8])
x = np.searchsorted(arr, 7)
print(x)
x = np.searchsorted(arr, 7, side='right')
print(x)
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)

# ============== Sorting 
print(f"=============== Sorting")
arr = np.array([3, 2, 0, 1])
print(np.sort(arr)) # returns a copy of the sorted array
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))
arr = np.array([True, False, True])
print(np.sort(arr))
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

# ============== Filter Array 
print(f"=============== Filter")
## create a newarr based on filter array
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)
print('------------')
## create newarr based on some conditions
arr = np.array([41, 42, 43, 44])
filter_arr = []
for elem in arr:
    if elem > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr[filter_arr]    
print(filter_arr)
print(newarr)
print('------------')
## create newarr directly from the original array 
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(newarr)
print('------------')