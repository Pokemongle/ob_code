# Python Classes/objects
oop: Object-Oriented Language

# Create a Class 
```python 
class MyClass:
	x = 5
```

# Create Object 
```python
p1 = MyClass()  
print(p1.x)
```

# The `__init__()` Function 
```python 
class Person:  
  def __init__(self, name, age):  
    self.name = name  
    self.age = age  
  
p1 = Person("John", 36)  
  
print(p1.name)  
print(p1.age)
```
> Remember the `self`

# The `__str__()` Function 
The `__str__()` function controls what should be returned when the class object is represented as a string.
```python 
class Person:  
  def __init__(self, name, age):  
    self.name = name  
    self.age = age  
  
  def __str__(self):  
    return f"{self.name}({self.age})"  
  
p1 = Person("John", 36)  
  
print(p1)
```

# Object Methods 
```python 
class Person:  
  def __init__(self, name, age):  
    self.name = name  
    self.age = age  
  
  def myfunc(self):  
    print("Hello my name is " + self.name)  
  
p1 = Person("John", 36)  
p1.myfunc()
```

# The self Parameter 
The `self` parameter is a reference to ***the current instance*** of the class, and is used to access variables that belong to the class.

`self` is ***the first parameter*** of the object functions but do not have to be `self`, can be of other name 
```python 
class Person:  
  def __init__(mysillyobject, name, age):  
    mysillyobject.name = name  
    mysillyobject.age = age  
  
  def myfunc(abc):  
    print("Hello my name is " + abc.name)  
  
p1 = Person("John", 36)  
p1.myfunc()
```

