![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202504271451708.png)

# 2.1 Understanding word embeddings

**embedding**: convert data into a vector format

# 2.2 Tokenizing text
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202504271456513.png)

## Input text → tokenized text
1. 首先 
	`with open(file_path, "r", encoding="utf-8") as f`
	`raw_text = f.read()`
	给它整个读进来
2. 然后用 `re.split` 和特殊的 pattern 切分，注意保留特殊字符
3. 最后用 `.strip()` 按情况去掉空白

## tokenized text → token IDs
