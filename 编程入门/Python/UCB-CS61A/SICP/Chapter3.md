[Lab 10](https://cs61a.vercel.app/lab/lab10/index.html)
[3.2](https://composingprograms.netlify.app/3/2)
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
; 1. define a value
(define pi 3.14)
(* pi 2)
6.28

; define a function
(define (square x) (* x x))
(square 2)
4

; 2. define a nested function
;; example1 - one body
(define (average x y) (/ (+ x y) 2))
;; example2 - nested body
(define (abs x) 
  (if (< x 0) 
  (- x)
  x))
;; example3 - many bodies
(define (sqrt x)
  (define (good-enough? guess)
    (< (abs (- (square guess) x)) 0.001))
  (define (improve guess)
    (average guess (/ x guess)))
  (define (sqrt-iter guess)
    (if (good-enough? guess)
        guess
        (sqrt-iter (improve guess))))
  (sqrt-iter 1.0))
(sqrt 9)
3.00009155413138
; 3. lambda function
((lambda (x y z) (+ x y (square z))) 1 2 3)
```
---
## 3.2.3 Compound values
```Scheme
; 1. Pairs
;; example 1
(define x (cons 1 2))
x
(1 . 2)
(car x)
1
(cdr x)
2
;; example 2
(define x (cons 1
(cons 2
      (cons 3
            (cons 4 nil)))))
x
(1 2 3 4)
	; equals to list
(list 1 2 3 4)
(1 2 3 4)
```
