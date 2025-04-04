# Python Numbers
- int
- float
- complex
> What about scientific numbers type? - float
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202502260236977.png)

# Type Conversion
`int() float() complex()`
> float to int will cut off
```python
x = 1    # int  
y = 2.8  # float  
z = 1j   # complex  
  
#convert from int to float:  
a = float(x)  
  
#convert from float to int:  
b = int(y)  
  
#convert from int to complex:  
c = complex(x)  
  
print(a)  
print(b)  
print(c)  
  
print(type(a))  
print(type(b))  
print(type(c))
```

# Random Number
`import random`
```python
import random  
# will create a random integer number between [1, 9]
print(random.randrange(1, 10))
```
