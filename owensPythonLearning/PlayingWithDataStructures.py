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

a[1] = 200 #Lists are MUTABLE ('think of this as mutatable'); they can be changed after creation
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

#TUPLES:
t = 5, 2, 'hi'
print(t)
print(*t) #Unpacking the tuple, prints '5 2 hi' instead of '(5, 2, 'hi')'
var1, var2, var3 = t
print(var1, var2, var3) #'Sequence unpacking' - multiple variable assignments in one! Yay!
#t[0] = 3 #THIS DOES NOT WORK! TUPLES ARE IMMUTABLE

#SETS:
letters = ['a', 'b', 'a', 'c', 'c', 'e']
letterSet = set(letters)
print(letterSet)

hasLetters = 'd' in letterSet, 'a' in letterSet #sets have quick ways of checking membership
print(hasLetters)

del a
a = {x for x in 'abracadabra' if x not in 'abc'} #Set comprehensions work exactly like list comprehensions do
print(a)

#DICTIONARIES (Basically key-value pairs)
robots = {'2175-2013' : 'Trap', '2175-2014' : 'Atlas', '2175-2015' : 'Melman', '2175-2016' : 'Night Fury'}
print(robots['2175-2014'])
robots.pop('2175-2015') #It was a bad year. We don't want it in our dictionary...
print(robots.keys())

dictComp = {x: x + 5 for x in range(5)} #Dictionaries have comprehensions too
print(dictComp)
