import numpy as np 
from numpy import random 
import matplotlib.pyplot as plt 
import seaborn as sns 

# ================ random intro
print(f"================ random intro")
## generate a random int
x = random.randint(100) # from 0 to 100
print(x)
## generate a random float
x = random.rand() # random float∈[0, 1)
print(x)
## generate a random array 
x = random.randint(100, size=(2, 3))
print(x)
x = random.rand(2, 3)
print(x)
## generate a random number from an array 
x = np.array([3, 5, 7, 9])
y = random.choice(x, size=(2))
print(y)

# ================= random data distribution 
print(f"================ random data distribution")
x = random.choice([3, 5, 7, 9], p=[0.1,0.3,0.6,0.0], size=(3, 5))
print(x)

# ================= random permutation 
print(f"================ random permutation")
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)
arr = np.array([1,2,3,4,5])
print(random.permutation(arr))

# ================= Seaborn
print(f"================ Seaborn")
arr = np.array([0,1,2,3,4,5])
sns.displot(arr, kind='kde')
plt.show()