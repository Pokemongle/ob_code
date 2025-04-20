# Python Functions 
## Creating a Function 
`def`

## Calling a Function 
```python 
def my_function():  
  print("Hello from a function")  
  
my_function()
```

## Arguments 
```python 
def my_function(**fname**):  
  print(fname + " Refsnes")  
  
my_function(**"Emil"**)  
my_function(**"Tobias"**)  
my_function(**"Linus"**)
```

## Number of Arguments 
must match 

## Arbitrary Arguments, \*args
```python 
def my_function(*kids):  
  print("The youngest child is " + kids[2])  
  
my_function("Emil", "Tobias", "Linus")
```

## Keyword Arguments (kwargs)
`key=value` use this to pass args 
```python 
def my_function(child3, child2, child1):  
  print("The youngest child is " + child3)  
  
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
```

## Arbitrary Keyword Arguments, \*\*kwargs
```python 
def my_function(**kid):  
  print("His last name is " + kid["lname"])  
  
my_function(fname = "Tobias", lname = "Refsnes")
```

## Default Parameter Value 
```python 
def my_function(**country = "Norway"**):  
  print("I am from " + country)  
  
my_function("Sweden")  
my_function("India")  
my_function()  
my_function("Brazil")
```

## Passing a List as an Argument 
```python 
def my_function(food):  
  for x in food:  
    print(x)  
  
fruits = ["apple", "banana", "cherry"]  
  
my_function(fruits)
```

## Return Values 
```python 
def my_function(x):  
  **return 5 * x  
**  
print(my_function(3))  
print(my_function(5))  
print(my_function(9))
```

## The pass Statement 
```python 
def myfunction():  
  pass
```

## Positional-Only Arguments 
```python 
def my_function(x, /):  
  print(x)  
  
my_function(3)
```

## Keyword-Only Arguments 
```python 
def my_function(*, x):  
  print(x)  
  
my_function(x = 3)
```

## Combine Positional-Only and Keyword-Only 
```python 
def my_function(a, b, /, *, c, d):  
  print(a + b + c + d)  
  
my_function(5, 6, c = 7, d = 8)
```

## Recursion 
pass