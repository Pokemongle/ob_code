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