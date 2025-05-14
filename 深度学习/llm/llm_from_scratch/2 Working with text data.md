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

# 2.3&2.4  tokenized text → token IDs
1. 首先把 split 处理好的 text 列表转换为 sorted set，即 vocab
2. 创建一个 tokenizer 类
	1. 创建 encode 函数，即 str to int，输入一段 text 返回对应的 IDs
		流程 `split->strip`
	2. 创建 decode 函数，即 int to str，输入一段 id 返回对应的 text
		流程：
			用 `" "` join token 列表
			去除特殊符号之前的空格，用到 re 的捕获组和 `re.sub` 函数
	3. 补充完善
		special tokens
		`<endoftext>` 可以拼接2个 text，注意前后加空格
		`<unk>` 可以替代 vocab 里没出现的未知字符
		extend 到初始的 vocab 中

# 2.5 Byte pair Encoding
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202505141624154.png)
如图所示，不按照预定的词汇分割，而是几个 char 的组合，这样就不需要 `<|unk|>` 这种特殊字符

# 2.6 Data sampling with a sliding window
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202505141724000.png)
llm 基于上文预测下一个单词，看不到之后的单词

# 2.7 Creating token embeddings
`torch.nn.Embedding(vocab_size, output_dim)`
词典映射到 embedding 空间，选定 embedding 的 dimension 

# 2.8 Encoding word positions 
给 `torch.nn.Embeddings` 输入 `torch.arange(context_length)` 就会获得随机的 pos_embeddings
