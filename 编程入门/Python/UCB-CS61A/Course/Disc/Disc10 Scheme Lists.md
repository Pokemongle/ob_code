[Disc10](https://cs61a.vercel.app/disc/disc10/index.html)
Use `python editor` to open scheme editor

---
## Boolean
`0` is not False, `#f` is the only value that is False

---
## Linked list
`nil` in Scheme equals to `Link.empty` in Python

How to construct linked lists?
1. `(cons 1 (cons 2 (cons 3 nil)))`
2. `(list 1 2 3 ...)`
3.  Use quote `'`
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
