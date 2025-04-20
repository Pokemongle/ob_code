# Python Sets 
`myset = {"apple", "banana", "cherry"}`
## Set
unordered unchangeable unindexed 

## Duplicates Not Allowed
```python 
thisset = {"apple", "banana", "cherry", "apple"}  
  
print(thisset)
```

> `True` and `1` are considered the same, `False` and `0` are considered the same 
```python 
thisset = {"apple", "banana", "cherry", True, 1, 2}  
  
print(thisset)
```

## Get the Length of a Set 
`len(myset)`

## Set Items - Data Types 
can be of any data type 

`type(myset)` `<class 'set'>`

# Access Set Items 
## Access Items 
`for x in myset`
`print(x in myset)`
`print(x not in myset)`
> cannot use indexing
## Change Items 
cannot change the value of existing values but can add or remove

# ***Add Set Items***
## Add Items 
`set.add(value)`

## Add Sets 
`set1.update(set2)`

## Add Any Iterable 
`set.update(list)`

# ***Remove Set Items***
`myset.remove(value)`
> If the item to remove does not exist, `remove()` will raise an error.

`myset.discard(value)`
>If the item to remove does not exist, `discard()` will ***NOT*** raise an error.

can also use `pop()`, but will randomly remove an item 

`myset.clear()` empties the set 

`del myset` delete the set object 

# Loop Sets 
## Loop Items 
`for x in myset`

# ***Join Sets*** 
## Join Sets 
There are several ways to join two or more sets in Python.
The `union()` and `update()` methods joins all items from both sets.
The `intersection()` method keeps ONLY the duplicates.
The `difference()` method keeps the items from the first set that are not in the other set(s).
The `symmetric_difference()` method keeps all items EXCEPT the duplicates.
## Union 
取并集 
`set3 = set1.union(set2)` 
`set3 = set1 | set2`

## Join Multiple Sets 
`myset = set1.union(set2, set3, set4)`
`myset = set1 | set2 | set3 |set4`

## Join a Set and a Tuple 
```python 
x = {"a", "b", "c"}  
y = (1, 2, 3)  
  
z = x.union(y)  
print(z)
```
> cannot use `|`

## Update 
`set1.update(set2)`

## Intersection 
取交集
`set3 = set1.intersection(set2)`
`set3 = set1 & set2`
`set1.intersection_update(set2)`

## Difference 
取差集 
`set3 = set1.difference(set2)`
`set3 = set1 - set2`
`set1.difference_update(set2)`

## Symmetric Differences 
取并集-交集（异或）
`set3 = set1.symmetric_difference(set2)`
`set3 = set1 ^ set2`
`set1.symmetric_difference_update(set2)`

# Set Methods
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202503082345400.png)
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202503082345439.png)
