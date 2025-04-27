![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202504271451708.png)

# 2.1 Understanding word embeddings

**embedding**: convert data into a vector format

# 2.2 Tokenizing text
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202504271456513.png)

1. read the txt file
```python
with open("the_text.txt", "r", encoding="utf-8") as f:
	raw_text = f.read()
	print(len(raw_text))
```
2. split the txt on whitespace characters 
```python
result = re.split(r'(\s)',raw_text)
```
> r' (\s)' will keep the whitespace characters as tokens
> r '\s' will eliminate the whitespace characters 

