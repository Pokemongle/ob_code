# Python Variables
## Creating variables
```python
x = 5
y = "John"
print(x)
print(y)

# change variable type
x = 'Sally'
```

## Casting
specify the types of variables
```python
x = str(3)
y = int(3)
z = float(3)
```

## Get the type
`type(VARIABLE)`
```python
x = 5
y = 'John'
print(type(x))
print(type(y))
```

python is lower/upper sensitive
```python
a = 1
# a will not be overwritten
A = 'One'
```

# Variable Names

## Variable Names
- start with a letter or the underscore character `_`
- cannot start with a number
- only contain letters or numbers or underscores (A-z, 0-9, and _)
- case-sensitive
- cannot be Python keywords
```python
# legal names
myvar = "John"  
my_var = "John"  
_my_var = "John"  
myVar = "John"  
MYVAR = "John"  
myvar2 = "John"

# illegal names
2myvar = "John"  
my-var = "John"  
my var = "John"
```

## Multi Words Variable Names
1. Camel Case `myVariableName = 'John'`
2. Pascal Case `MyVariableName = 'John'`
3. Snake Case `my_variable_name = 'John'`


# Assign Multiple values
## Many Values to Multiple Variables
```python
x, y, z = "Orange", "Banana", "Cherry"  
print(x)  
print(y)  
print(z)
```
## One Value to Multiple Variables 
```python
x = y = z = "Orange"  
print(x)  
print(y)  
print(z)
```
## Unpack a Collection
```python
fruits = ["apple", "banana", "cherry"]  
x, y, z = fruits  
print(x)  
print(y)  
print(z)
```

# Output Variables
use `print()`
```python
# print one variable at a time 
x = "Python is awesome"  
print(x)
# print multiple variables at a time
x = "Python"  
y = "is"  
z = "awesome"  
print(x, y, z) # this will add a space between every two variables
# use + to combine multiple variables
x = "Python "  
y = "is "  
z = "awesome"  
print(x + y + z)
x = 5
y = 10
print(x + y)
```


# Global Variables
## Global Variables
***global variables***: variables created outside of a function
```python
x = "awesome"  
  
def myfunc():  
  print("Python is " + x)  
  
myfunc()
```

local variable with the same name of the global variable will be used in the function
```python
x = "awesome"  
  
def myfunc():  
  x = "fantastic"  
  print("Python is " + x)  
  
myfunc()  
  
print("Python is " + x)
```

## The global Keyword
create a global variable in a function, use `global`
```python
def myfunc():  
  global x  
  x = "fantastic"  
  
myfunc()  
  
print("Python is " + x)
```
change the value of a global variable
```python
x = "awesome"  
  
def myfunc():  
  global x  
  x = "fantastic"  
  
myfunc()  
  
print("Python is " + x)
```