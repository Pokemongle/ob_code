# Shell Scripting

## keypoints
* perform a series of commands
* make use of *control flow expressions* like conditionals or loops
## differences
* optimized for performing shell-related tasks
	* creating command pipelines `touch` `echo >`
	* saving results into files `>`
	* reading from standard input `<`
* **bash** scripting is the most common 

## variables

* assign variables
	* `foo=bar` is correct
	* `foo = bar` is wrong, because this seems like calling the command `foo` with arguments `bar` and `=`
		* in bash, the **space character** will perform *argument splitting*
* access the variable
	`$foo`
	![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308211819584.png)

## delimiters

Strings in bash can be defined with `'` and `"`, but they are not equivalent
* Strings delimited with `'` are literal strings, and can not substitute variable values
* whereas `"` delimited strings will 
	![](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308211820668.png)

## control flow techniques
`if`, `case`, `while`, `for`

### function
