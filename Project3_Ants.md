How to traverse the list while do some modification like remove?
1. Traverse reversely
	`for i in range(len(the_list)-1,-1,-1)`
	While the first `-1` refers to the exact index of the list (the element ahead of `the_list[0]`), the second means the stands for the traverse order
2. Iterator `reverse()`

How to check if a subclass instance belongs to a superclass?
`isinstance(obj,superclassc)`