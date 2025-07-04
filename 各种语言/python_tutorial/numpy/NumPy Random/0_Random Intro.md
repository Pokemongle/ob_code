package 
	`from numpy import random`

generate a random int 
	`x = random.randint(100) # from 0 to 100 x ∈[0,100], x∈Z`
generate a random float
	`x = random.rand() x∈[0, 1)`
	`x = random.rand(2, 3)`
generate a random array 
	`x = random.randint(100, size=(2, 3))`
generate random from an array 
	`x = np.array([1, 3, 5, 7, 9])`
	`y = random.choice(x, size=(2))`

summary 
`from numpy import random`
`random.randint(100, size=(2, 3))`
`random.rand(SIZE)`
`random.choice(arr, size=(2, 3))`

