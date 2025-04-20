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
