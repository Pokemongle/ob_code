# Python Strings
## Strings
`'string'` or `"string"`
## Quotes Inside Quotes
```python
print("It's alright")  
print("He is called 'Johnny'")  
print('He is called "Johnny"')
```

## Assign String to a Variable 
`a = 'Hello'`

## Multiline Strings
```python
a = """Lorem ipsum dolor sit amet,  
consectetur adipiscing elit,  
sed do eiusmod tempor incididunt  
ut labore et dolore magna aliqua."""  
print(a)
```

## Strings are Arrays
```python
a = "Hello, World!"  
print(a[1])
```

## Looping Through a string
```python
for x in "banana":  
  print(x)
```

## String length
```python
a = "Hello, World!"  
print(len(a))
```

## Check String 
`in`  check if certain phrase or character is present in a string 
`not in` not in a string
```python
txt = "The best things in life are free!"  
print("free" in txt)
print("free" not in txt)
```

# Slicing Strings
## Slicing
```python
b = "Hello, World!"  
print(b[2:5]) # b[5] is not included
print(b[:5]) # slicing from the start
print(b[2:]) # slicing to the end
print(b[-5:-2]) # negative indexing, b[-2] is not included
```

# Modify Strings
```python
# upper case
a = "Hello, World!"  
print(a.upper())

# lower case
a = "Hello, World!"  
print(a.lower())

# remove Whitespace from the beginning or the end
a = " Hello, World! "  
print(a.strip()) # returns "Hello, World!"

# replace letters
a = "Hello, World!"  
print(a.replace("H", "J"))

# split strings
a = "Hello, World!"  
print(a.split(",")) # returns ['Hello', ' World!']
```

# String Concatenation
```python
# use +
a = "Hello"  
b = "World"  
c = a + b  
print(c)
```

# Format - Strings
```python
# F-Strings
age = 36  
txt = f"My name is John, I am {age}"  
print(txt)

# Modifiers
price = 59  
txt = f"The price is {price:.2f} dollars"  
print(txt)
```

# Escape Characters
`\`  insert character that are illegal in a string
```python
txt = "We are the so-called \"Vikings\" from the north."
```
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202502260421775.png)

# String Methods 
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202502260425438.png)
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202502260425416.png)
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202502260426751.png)

