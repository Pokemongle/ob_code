# Q4
```python
>>> nickel = mint.create(Nickel) 
>>>  nickel.year # The mint has not updated its stamp yet 
>>>  2021 
>>>  nickel.worth() # 5 cents + (80 - 50 years) 
>>>  35
```
>How are objects created? - Use the *parentheses*
	`new_object = Object()`

> Can only add string to string
> 	`"Hello " + 1`  >>>Error
> 	`"Hello " + str(1)` >>>"Hello 1"