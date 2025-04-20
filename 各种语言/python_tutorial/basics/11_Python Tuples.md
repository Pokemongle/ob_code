# Python Tuples 

ordered and unchangeable
tuple is created using round brackets 
## Tuple 
`thistuple = ("apple", "banana", "cherry")`

## Tuple Length 
`len(mytuple)`

## Create Tuple With One Item 
need a comma
```python 
thistuple = ("apple",)  
print(type(thistuple))  
  
#NOT a tuple  
thistuple = ("apple")  
print(type(thistuple))
```

## Tuple Items - Data Types 
Tuple items can be of any data type 

`type(mytuple)`
`<class 'tuple'>`

# Access Tuple Items
## Access Tuple Items 
use index `mytuple[0]`

## Negative Indexing 
`mytuple[-1]`

## Range of Indexes 
`mytuple[2:5]`
`mytuple[:4]`
`mytuple[2:]`

## Range of Negative Indexes 
`mytuple[-4:-1]`

## Check if Item Exists 
`if item in mytuple`

# Update Tuples 
## Change Tuple Values 
***tuple → list → tuple***
`mylist = list(mytuple)`
`mytuple = tuple(mylist)` 
```python 
x = ("apple", "banana", "cherry")  
y = list(x)  
y[1] = "kiwi"  
x = tuple(y)  
  
print(x)
```

## Add Items 
```python 
# 1. Convert the tuple into a list
thistuple = ("apple", "banana", "cherry")  
y = list(thistuple)  
y.append("orange")  
thistuple = tuple(y)
# 2. Add tuple to a tuple 
Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")  
y = ("orange",)  # Rememeber the comma
thistuple += y  
  
print(thistuple)
```

## Remove Items 
```python 
thistuple = ("apple", "banana", "cherry")  
y = list(thistuple)  
y.remove("apple")  
thistuple = tuple(y)
```
delete the tuple completely
`del thistuple`

# Unpack Tuples 
## Unpacking a Tuple 
using values from a tuple 
```python 
fruits = ("apple", "banana", "cherry")  
  
(green, yellow, red) = fruits  
# number of variables must match the length of the tuple
print(green)  
print(yellow)  
print(red)
```

what if number of variables < number of values?
```python 
# Example1 - asterisk at the end
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")  
# red will be a list
(green, yellow, *red) = fruits  
  
print(green)  
print(yellow)  
print(red)
'''The answer will be:
apple
banana
['cherry', 'strawberry', 'raspberry']
'''

# Example2 - asterisk in the middle 
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")  
  
(green, *tropic, red) = fruits  
  
print(green)  
print(tropic)  
print(red)
''' The answer will be:
apple
['mango', 'papaya', 'pineapple']
cherry
'''
```

# Loop Tuples 
## Loop Through a Tuple 
use for loop 
`for x in mytuple`

## Loop Through the Index Numbers 
`for i in range(len(mytuple))`

## Using a While Loop 
`while i < len(mytuple)`

# Join Two Tuples 
## Join Two Tuples 
`tuple1 + tuple2 

## Multiple Tuples 
`tuple2 = tuple1 * 2` 
> list can also be multiplied

# Tuple Methods 
`mytuple.count(value)`
`mytuple.index(value)`