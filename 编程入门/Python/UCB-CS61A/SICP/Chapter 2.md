- [datatype](http://getpython3.com/diveintopython3/native-datatypes.html) 
	- `isinstance(data, datatype)`
	- `type(data)`
	- Boolean: can do calculation. View `True` as `1` and `False` as `0`

	- Python takes apart int and float data by the *decimal point*
	- `float(data), int(data)`
		![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202410031405083.png)
		
- List
	- Creating a list
		`a_list = [1,2,3]`, values separated with comas in square brackets
		
		`[x for <statement>]` 
			e.g. `[x for x in odds]`
			`[x for x in odds if 25 % x == 0]`
	- Copy a list
		`new_list = list(old_list)` 
	- Slicing
		`a_list[A:B:C]`
		
	- Add item
		`append(element)`
		`extend([a list of elements])`
		`insert(index, element)`
		
	- Search for item 
		`count(item)`
		`in <list>`
		`index(item)
		`
	- Delete item
		`del <list>[index]`
		`pop()`
		`pop(index)`
		
- Tuple
	- Just like list, immutable
	- `tuple(<list>)` `list(<tuple>)`
	- `(False)` is different from `(False, )`
		- Think of `if ()`
---
- Iteration
	- for
		`for i in <sequence>`
		`for x, y in <sequence>`
		`for _ in <sequence>`
---
- [String](http://getpython3.com/diveintopython3/strings.html)
	- Create string
		- `str()`
		- `str1 + str2`
		- 'sth'. join (list)
	- format  
		- `print("{0:.1f}{1}".format(size, suffix))`
		- `'1000{0[0]} = 1{0[1]}'.format(si_suffixes)`
	- Split string
		- `s.splitlines()`
		- `s.lower()`
		- `a_list = s.split(<sth>)`