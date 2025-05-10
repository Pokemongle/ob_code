[系统的RegEx学习](https://deerchao.cn/tutorials/regex/regex.htm#)



1. import the regular expression package
	`import re`
2. prepare a txt
	`txt = "The rain in Spain."`
3. functions 
- `findall`: returns a list containing all matches
	`x = re.findall("<RULES>", txt)`

the RULES 
`[]`: a set of Characters, ASCII
	`[a-m]`
`\`: signals a  special sequence
	`\d`
	![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202504201624784.png)
> a "raw string" is a str where the `\` in it is considered literal instead of escape characters 

`\w` equals to `[A-Za-z0-9_]`

`.`: any character except `\n`
	`he..o`
`^`: start with
	`^hello`
`$`: ends with
	`planet$`
`*`: zero or more occurrences
	`he.*o`
`+`: one or more
	`he.+o`
`?`: zero or one
	`he.?o`
`{}`: exactly the specified number of occurrences 
	`he.{2}o`
`|`: either or
	`falls|stays`

# 1. 正则表达式的7个境界
## level1-固定的字符串
```python
import re
txt = "The rain in Spain"
x = re.findall(r"ai", txt)
print(x)
```
## level2-某一类字符
```python 
text = "Height: 161 Weight: 121, ID: 123456, Password: 8207"
# find single number
print(re.findall(r"\d", text))
# find number in the specified range
print(re.findall(r"[1-5]", text))
# find specified number
print(re.findall(r"[123]", text))
```

## level3-重复某一类字符
```python
text = "Height: 161 Weight: 121, ID: 123456, Password: 8207"
# ?: 0 or 1
print(re.findall(r"\d?", text))
# +: 1 or more
print(re.findall(r"\d+", text))
# {<NUMBER>}: NUMBER characters
print(re.findall(r"\d{3}", text))
print(re.findall(r"\d{1,5}", text)) #####
# *: 0 or more
print(re.findall(r"\d*", text))
```

## level4-组合 level2-3
```python
text = "phone number: 0521-12354235 phone number2: 852-78302942"
print(re.findall(r"\d{3,4}-\d{1,10}", text))
```

## level5-多种情况
```python
text = ("phone number: 0521-12354235 phone number2: 852-78302942 phone number3: 15270169033")
print(re.findall(r"\d{3,4}-\d{1,10}|\d{8,12}", text))
```
匹配座机或者手机号码

## level6-特殊位置

## level7-内部约束

# 2. 写正则表达式的步骤
`0571-88776655-9527`
- 确定模式包含几个子模式
	3个，用 `-` 连接
- 各个部分的字符分类是什么
	`\d`
- 各个子模式如何重复
- 是否有外部位置限制
- 是否有内部制约关系

# 3. RegEx的语法规则
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202504271548898.png)

![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202504271548925.png)

![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202504271550216.png)

![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202504271552253.png)

![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202504271557311.png)

![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202504271557141.png)

![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202504271558087.png)

# 4. Python re module
## 查找
- search，只返回一个
```python
text = "abc, Abc, ABC"
m = re.search(r"abc", text)
print(dir(m))
print(m.group())

text = "David's phone number is 13588033064, another one is 19083956724, she's favorite numbers are 01234567891, her home number is 0571-70169033"
m = re.search(r"(\d{4})-(\d{8})", text)
print(m.groups())
```
- match，只返回一个，从头开始匹配
- findall，返回字符串
- 返回 Match 迭代器
## 替换
- sub
- subn 返回替换后的 str 和替换次数
## 分割
- split
