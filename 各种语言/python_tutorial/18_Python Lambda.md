a lambda function is a ***small anonymous*** function 
# Syntax 
`lambda arguments : expression`
```python 
# single argument
x = lambda a : a + 10  
print(x(5))

# multiple arguments 
x = lambda a, b : a * b  
print(x(5, 6))

x = lambda a, b, c : a + b + c  
print(x(5, 6, 2))
```

# Why Use Lambda Functions?
use it within another function 
```python 
# example1
def myfunc(n):  
  return lambda a : a * n
  
# example2
def myfunc(n):  
  return lambda a : a * n  
  
mydoubler = myfunc(2)  
  
print(mydoubler(11))
```

