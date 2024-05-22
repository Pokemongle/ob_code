# 1.1 Getting Started
## 1.1.1 Programming in Python
## 1.1.2 Installing Python 3
> Better use [Anaconda](https://www.bilibili.com/video/BV1hE411t7RN/?spm_id_from=333.337.search-card.all.click&vd_source=4ab0010a787e254ae5cffb27e35dce8b)
## 1.1.3 Interactive Sessions
Python prompt `>>>`
## 1.1.4 First Example
	from urllib.request import urlopen
- Statements & Expressions
	- expressions: Compute some value `1+2+3`
	- statements: Carry out some action `exit()`
- Functions
	- encapsulate log that manipulates data
```python
	shakespeare = urlopen("http://composingprograms.com/shakespeare.txt")
	words = set(shakespeare.read().decode().split())
```


- Objects
	- data & logic to manipulate data
	- An example of `set`
```python
{w for w in words if len(w)=6 and w[::-1] in words}
// w[::-1] represents for the reverse of w
```

- Interpreters
	- A program that implements such a procedure, evaluating compound expressions