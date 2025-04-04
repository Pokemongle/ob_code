# Python Dictionary 
key: value pairs 
```python 
thisdict = {  
  "brand": "Ford",  
  "model": "Mustang",  
  "year": 1964  
}
```

ordered (after Python3.6), changeable, no duplicates 

## Dictionary Items 
can be referred to by using the key name 
```python 
thisdict = {  
  "brand": "Ford",  
  "model": "Mustang",  
  "year": 1964  
}  
print(thisdict["brand"])
```

## Dictionary Length 
`len(thisdict)`

# Dictionary Items - Data Types 
can be of any data type 

`type(thisdict)` `<class 'dict'>`

## The `dict()` Constructor 
`thisdict = dict(name = "John", age = 36, country = "Norway")`

# Access Dictionary Items 
## Accessing Items 
`x = thisdict["model"]`
`x = thisdict.get("model")`

## Get Keys 
`x = thisdict.keys()`

## Get Values 
`x = thisdict.values()`

## Get Items 
```python 
x = thisdict.items()
'''The answer will be:
{'google', 'banana', 'microsoft', 'cherry'}
'''
```

## Check if Key Exists 
`if "model" in thisdict:`

# Change Dictionary Items 
## Change Values 
`thisdict["year"] = 2018`

## Update Dictionary 
`dict1.update(dict2)`

# Add Dictionary Items 
## Adding Items 
`thisdict["color"] = "red"`

## Update Dictionary 
`thisdict.update({"color": "red"})`

# Remove Dictionary Items 
## Removing Items 
`thisdict.pop("model")`
`thisdict.popitem()`
`del thisdict["model"]`
`del this dict`
`thisdict.clear()`

# Loop Dictionaries 
## Loop Through a Dictionary 
`for key in thisdict`
`for key in thisdict.keys()`
`for value in thisdict.values()`
`for key, value in thisdict.item()`

# Copy Dictionaries 
## Copy a Dictionary 
`mydict = thisdict.copy()`
`mydict = dict(thisdict)`

# Nested Dictionaries 
## Nested Dictionaries 
```python 
myfamily = {  
  "child1" : {  
    "name" : "Emil",  
    "year" : 2004  
  },  
  "child2" : {  
    "name" : "Tobias",  
    "year" : 2007  
  },  
  "child3" : {  
    "name" : "Linus",  
    "year" : 2011  
  }  
}
```

## Access Items in Nested Dictionaries 
`print(myfamily["child2"]["name"])`

## Loop Through Nested Dictionaries 
```python 
for x, obj in myfamily.items():  
  print(x)  
  
  for y in obj:  
    print(y + ':', obj[y])
```

# Dictionary Methods 
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202503090004065.png)

