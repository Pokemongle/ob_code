Lists Methods:
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202503082258087.png)

# Python Lists

# Python Lists 
`mylist = ["apple", "banana", "cherry"]`
## List 
store multiple items in a single variable
created by square brackets

see other python collections (arrays): tuple, set, dictionary, list

## List Items 
ordered, changeable, duplicate values allowed
list items are indexed

## List Length 
`len(mylist)`

## List Items - Data Types 
list items can be of any data type

## List type
`<class 'list'>`

## Access Items
`[0] [1] [-1] [-4] [2:5] [-4:-1]`

## Check if Item Exists
`if item in mylist`

# Change List Items
## Change Item Value 
access item -> assign value
`mylist[0] = 'first'`
## ***Change a Range of Item Values***
`mylist[1:3] = ['apple', 'watermelon']`
- insert more than you access, will insert
- insert less than you access, will remove original items and then insert the new one
- In short, 1. remove the original item 2. insert the new one



# Add List Items
## Append Items
`mylist.append('apple')` will add to the end of the list
## Insert Items
`mylist.insert(2, 'apple')`

## Extend List 
`mylist.extend(another_list)` will concatenate to the end 
> another_list can be any iterable items

# Remove List Items 
## Remove Specified item
`mylist.remove("apple")`

## Remove Specified Index 
`mylist.pop(index)`
`mylist.pop(item)`
`mylist.pop()`
`del mylist[0]`
`del mylist`

## Clear the List 
`mylist.clear()`

# Loop Lists 
## Loop Through a List 
`for x in mylist`
## Loop Through the Index Numbers 
`for i in range(len(mylist))`

## Using a While Loop 
`while i < len(mylist)`

## Looping Using List Comprehension 
`[print(x) for x in this list]`

# List Comprehension
## List Comprehension 
create a new list based on the values of an existing list
`new_list = [x for x in mylist if 'a' in x]`

## Sort Lists 
## Sort List Alphanumerically
`mylist = ["orange", "mango", "kiwi", "pineapple", "banana"]`
or
`mylist = [100, 50, 65, 82, 23]`
`mylist.sort()`

## Sort Descending
`mylist.sort(reverse = True)`

## Customize Sort Function 
```python 
def myfunc(n):  
  return abs(n - 50)  
  
thislist = [100, 50, 65, 82, 23]  
thislist.sort(key = myfunc)  
print(thislist)
```

## Case Insensitive Sort
```python 
thislist = ["banana", "Orange", "Kiwi", "cherry"]  
thislist.sort()  
print(thislist)

## key insensitive
thislist.sort(key = str.lower)
```

## Reverse Order 
`mylist.reverse()`

# Copy Lists 
cannot use `list1=list2`, because they point to the same object 

## Use the copy () method 
`list2 = list1.copy()`

## Use the list () method 
`list2 = list(list1)`

## Use the slide Operator 
`list2 = list1[:]`

# Join Lists 
## Join Two Lists 
`list3 = list1 + list2`
use for loop and .append/.extend:
```python 
for x in list2:
	list1.append(x)

list1 = list1.extend(list2)
```

