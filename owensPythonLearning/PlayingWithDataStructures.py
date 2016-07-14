from collections import deque

a = list(range(10))
print(a)

a.append(11)
print(a)

a.extend(a)
print(a)
print(a.count(2))
a.reverse()
print(a)

queue = deque(a) #Make a deque from 'a'
print(queue.popleft())
print(queue)

def isEven(x): return x % 2 is 0

print(list(filter(isEven, range(20)))) #get the values from range(20) that satisfy isEven
print(list(map(isEven, range(20)))) #Map isEven to the list range and print the list of return values

def squares(n):
	return [x ** 2 for x in range(n)] #Uses a "list comprehension" to define a list of squares.
	#This would also work here: return map(lambda x: x **2, range(n))

print(squares(5)) #print the first five square numbers

def oddFilter(L): #Manually filters out odd numbers. Of course, the filter method would work better here, but I wanted to do it with a list comprehension
	return [x for x in L if not isEven(x)]

print(oddFilter(list(range(10)))) #Prints all odd numbers between 1 and 10 (inclusive)

matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

print(matrix, len(matrix))
print(matrix[2])

def transpose(M):
	return [[row[i] for row in M] for i in range(len(M))] #Nested list comprehensions transposing a matrix. Inner nest corresponds to the value of each COLUMN in the output matrix.
	#Apparently zip(*matrix) would work here as well. zip() is basically THE function for transposition. Just remember the * to unpack the matrix into arguments for zip()
print(transpose(matrix))

b = list(range(10))
del b[2:5] #delete elements 2, 3, and 4 from b. Does NOT delete element 5
print(b)
del b
#print(b, a) would error because del b completely deletes the reference to b. b becomes undefined
