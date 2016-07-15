import math
from collections import Counter

def bruteForceSolution(topValue):
	ans = 1
	while(not all(v is 0 for v in [ans % x for x in range(1, topValue + 1) if x is not ans])):
		ans += 1
	return ans

def isPrime(number):
	if number % 2 is 0:
		return number is 2
	else:
		return all(v is not 0 for v in [number % x for x in range(3, math.ceil(number / 2) + 1)])

def bruteForcePrimeFactorization(topValue):
	#Generate list of primes up to topValue / 2
	#Divide topValue by each prime until unsuccessful and append the appropriate number of primes to the list of primes
	primes = [x for x in range(1, topValue + 1) if isPrime(x)]
	factors = [num for num in primes if topValue % num is 0]

	for prime in factors[1:]: #skip index 1, since anything can be divided by 1 infinitely
			topValue /= prime

			while int(topValue) % prime is 0 and topValue >= prime:
				topValue /= prime
				factors.append(prime)

	return factors

def product(listToProd):
    p = 1
    for i in listToProd:
        p *= i
    return p

def actualSolution(topValue):
	exhaustivePrimes = []
	for i in range(topValue):
		exhaustivePrimes = Counter(exhaustivePrimes) | Counter(bruteForcePrimeFactorization(i))

	return product(list(exhaustivePrimes.elements()))

print(actualSolution(20))
#print(all(v is True for v in [product(bruteForcePrimeFactorization(a)) == a for a in range(1, 1000)]))
