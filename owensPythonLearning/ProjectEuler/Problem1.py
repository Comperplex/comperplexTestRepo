def sum_multiples(factors, upper_bound):
	return sum([num for num in range(1, upper_bound) if 0 in [num % factor for factor in factors]])

print(sum_multiples([3 , 5], 1000))
