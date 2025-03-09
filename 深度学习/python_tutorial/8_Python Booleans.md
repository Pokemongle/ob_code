`bool()` evaluate any value, give `True` or `False` in return
```python
print(bool("Hello"))  
print(bool(15))
```
Most Values are True except empty things `0, None, empty arrays`
```python
bool(False)  
bool(None)  
bool(0)  
bool("")  
bool(())  
bool([])  
bool({})

# empty class
class myclass():  
  def __len__(self):  
    return 0  
  
myobj = myclass()  
print(bool(myobj))

# built-in function that returns boolean values
x = 200  
print(isinstance(x, int))
```