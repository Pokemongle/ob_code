[Disc10](https://cs61a.vercel.app/disc/disc10/index.html)
Use `python editor` to open scheme editor

---
## Boolean
`0` is not False, `#f` is the only value that is False

---
## Linked list
`nil` in Scheme equals to `Link.empty` in Python

How to construct linked lists?
1. `(list 1 2 3 ...)`
2.  Use quote `'`
3. `(cons 1 (cons 2 (cons 3 nil)))`
- 3 ways to accomplish this graph:
	![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202410260951429.png)
```Scheme
; Use list
(define with-list
    (list
        (list 'a 'b)
        'c 'd (list 'e)
    )
)
(draw with-list)
```
`(list <value1> <next list>)`
Use `'a` to represent a

```Scheme
; Use quote
(define with-quote
    '(
        (a b)
        c d (e)
    )

)
(draw with-quote)
```
Use `'()` to represent `(list)`
Do not have to use `'` before un-num values

```Scheme
; Use cons
(define with-cons
    (cons
        (cons 'a (cons 'b nil))
        (cons 'c (cons 'd (cons (cons 'e nil) nil)))
    )
)
(draw with-cons)
```
`(cons <value> <next list>)` is similar to `List` in Python

---
## Quotation
 ```Scheme
scm> (quote (1 x 3))
scm> `(1 × 3) ;equals to the former expression
``` 
---
## Equivalent comparison
1.  `=`: compare numbers or cause Error
```Scheme
(define a 1)
(= 1 1); #t
(= a 1); #t
(= 'a 1); Error
```
2. `eq?`: check if the same objects
```Scheme
(define a 1)
(eq? a a); #t
(eq? 1 1); #f, be like Obj(), in diff cache
```
3. `equal:` check if all elems are the same
```Scheme
(define a (list 1 2 3))
(define b (cons 1 (cons 2 (cons 3 nil))))
(equal? a b); #t diff objs but the same elems
```

---
## Tail Recursion
```Scheme
; not tail recursion
(define (factorial n)
	(if (= n 0)
	    1
	    (* n (factorial (- n 1)))))
; tail recursion
(define (tail-factorial n)
(define (helper n acc)
  (if (= n 0)
      acc
      (helper (- n 1) (* n acc)))); recursion with no other calculation
(helper n 1))
```
tail recursion do not create new stacks
- In the former condition:
	- n=3
	- n=2
	- n=1
	- n=0
- In the latter condition:
	- helper

---
## Filter
`(filter <condition> <list>)`
In condition, return which condition is `True`
```Scheme
(define (remove item lst)
    (define (condition num)
        (not (= item num)) ; num != item
    )
    (filter condition lst)
)
(remove 2 (list 1 2 3))
```
