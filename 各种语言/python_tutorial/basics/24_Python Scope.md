A variable is only available from inside the region it is created. This is called **scope**.
# Local Scope 
A variable created inside a function belongs to the _local scope_ of that function, and can only be used inside that function.
```python 
def myfunc():  
  x = 300  
  print(x)  
  
myfunc()

# function inside function 
def myfunc():  
  x = 300  
  def myinnerfunc():  
    print(x)  
  myinnerfunc()  
  
myfunc()
```

# Global Scope
A variable created in the main body of the Python code is a global variable and belongs to the global scope.
```python 
x = 300  
  
def myfunc():  
  print(x)  
  
myfunc()  
  
print(x)
```

# Global Keyword 
```python 
def myfunc():  
  global x  
  x = 300  
  
myfunc()  
  
print(x)
```

# Nonlocal Keyword 
The `nonlocal` keyword is used to work with variables inside nested functions.

The `nonlocal` keyword makes the variable belong to the outer function.
```python 
def myfunc1():  
  x = "Jane"  
  def myfunc2():  
    nonlocal x  
    x = "hello"  
  myfunc2()  
  return x  
  
print(myfunc1())
```