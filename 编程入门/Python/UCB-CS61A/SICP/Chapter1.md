simple : )

---
a new discovery:  `-1 - -1`
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202409270030436.png) 

---
Function definition:
```Python
def <name>(<formal parameters>):
    return <return expression>
```
	domain range intent
---
Function name and parameter name in Python
	`name_of function`
	`name_of_parameter`

How to write [docstring](https://peps.python.org/pep-0257/)

Default argument value
```Python
def pressure(v, t, n=6.022e23):
        """Compute the pressure in pascals of an ideal gas.

        v -- volume of gas, in cubic meters
        t -- absolute temperature in degrees kelvin
        n -- particles of gas
        """
        k = 1.38e-23  # Boltzmann's constant
        return n * k * t / v
```

Doc Test
`python -m doctest <python_source_file>`

Higher Functions
	Pass function to function
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202409280006847.png)

Boolean
`True and not False or not True and False` equals to
`(True and (not False)) or ((not True) and False)`

Lambda Functions
```Python
lambda x : x * x
put x into lambda will return x * x
```

`*args` stands for all the arguments sent to function f
```Python
def printed(f):
	def print_and_return(*args):
		result = f(*args)
		print('Result:', result)
		return result
	return print_and_return
```

This operator `/` will result in a float number