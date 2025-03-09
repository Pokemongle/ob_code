# Python Iterators 
an iterator is an object that contains a countable number of values 
contains `__iter__()` and `__next__()`

# Iterator vs Iterable 
Lists, tuples, sets and dictionaries are iterable collections 
They are iterable containers which you can get an iterator from
```python 
# tuple
mytuple = ("apple", "banana", "cherry")  
myit = iter(mytuple)  
  
print(next(myit))  
print(next(myit))  
print(next(myit))

# string
mystr = "banana"  
myit = iter(mystr)  
  
print(next(myit))  
print(next(myit))  
print(next(myit))  
print(next(myit))  
print(next(myit))  
print(next(myit))
```

# Looping Through an Iterator 
`for` loop 

# Create an Iterator 
implement `__iter__()` and `__next()__`
`__iter__()` must return the iterator object itself 
`__next__()` must return the next item in the sequence 
```python 
class MyNumbers:  
  def __iter__(self):  
    self.a = 1  
    return self  
  
  def __next__(self):  
    x = self.a  
    self.a += 1  
    return x  
  
myclass = MyNumbers()  
myiter = iter(myclass)  
  
print(next(myiter))  
print(next(myiter))  
print(next(myiter))  
print(next(myiter))  
print(next(myiter))
```

# Stop Iteration 
`raise StopIteration`