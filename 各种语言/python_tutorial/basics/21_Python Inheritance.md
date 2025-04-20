# Create a Parent Class 
```python 
class Person:  
  def __init__(self, fname, lname):  
    self.firstname = fname  
    self.lastname = lname  
  
  def printname(self):  
    print(self.firstname, self.lastname)  
  
#Use the Person class to create an object, and then execute the printname method:  
  
x = Person("John", "Doe")  
x.printname()
```

# Create a Child Class 
```python 
class Student(Person):  
  pass

# override __init__()
class Student(Person):  
  def __init__(self, fname, lname):  
    #add properties etc.

# keep the inheritance 
class Student(Person):  
  def __init__(self, fname, lname):  
    Person.__init__(self, fname, lname)

# easier way to keep the inheritance 
class Student(Person):  
  def __init__(self, fname, lname):  
    super().__init__(fname, lname)
```

# Add Properties 
after `super().__init__()`
```python 
  def __init__(self, fname, lname):  
    super().__init__(fname, lname)  
    self.graduationyear = 2019
```
