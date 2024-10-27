# Q1: Is Tail Call
**Tail Context**
1. the second **or** third operand in an `if` expression
2. any of the non-predicate sub-expressions in a `cond` expression (i.e. the second expression of each clause)
3. the last operand in an `and` or an `or` expression
4. the last operand in a `begin` expression's body
5. the last operand in a `let` expression's body

# Q2: Sum
This is easy tail call

# Q3: Reverse
This is easy, but check `(if (null? l))` not `(if (null? (car l)))`