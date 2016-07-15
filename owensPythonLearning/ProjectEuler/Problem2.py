def evenFibSum(fiboList):
	return sum([num for num in fiboList if num % 2 is 0])

def boundedFib(upper_bound):
	fibs = [1, 1]
	while fibs[len(fibs) - 1] < upper_bound:
		fibs.append(fibs[len(fibs) - 1] + fibs[len(fibs) - 2])

	return fibs

print(evenFibSum(boundedFib(4000000)))
