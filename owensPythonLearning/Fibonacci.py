def fib(n):
	fibN = []
	a, b, = 1, 1
	for n in range(n):
		a, b = b, a+b
		fibN.append(a)
	return fibN

print(fib(10))
