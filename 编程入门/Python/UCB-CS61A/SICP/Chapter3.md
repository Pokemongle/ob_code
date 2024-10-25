# 3.2 Basic Scheme
## 3.2.1 expressions
- suffix notation
	`scm> (* 2 2)` `4`
- if expression
	`if <predicate> <consequent> <alternative>`
- compare
	`scm> (>= 4 2)` `#t`
	`(and <e1> ... <en>)` 
	`(or <e1>... <en>)`
	`(not <e>)`
---
## 3.2.2 Definitions
```Scheme
# define a value
(define pi 3.14)
(* pi 2)
6.28

# define a function
(define (square x) (* x x))
(square 2)
4
```