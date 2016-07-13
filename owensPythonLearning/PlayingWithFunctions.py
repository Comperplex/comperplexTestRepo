def appendToList(a, L=None):
	if L is None:
		L = []
	L.append(a)
	return L

print(appendToList(1)) #Should print just [1]
print(appendToList(2)) #Should print just [2]
print(appendToList(2, appendToList(1))) #Should print [1, 2]

def keyWordArguments(arg1, arg2='not an essential arg'):
	print('I saw', arg1, 'and', arg2)

keyWordArguments('test') #Prints "I saw test and not an essential arg"
keyWordArguments(arg1 = 'test2') #Prints "I saw test2 and not an essential arg"
#keyWordArguments(arg2 = 'Fail!') #This line would throw an exception: Nothing is assigned to arg1
#keyWordArguments(0, arg1=1) #This line would throw an exception: Duplicate assignment to arg1
keyWordArguments('test', arg2='not a fail') #Prints "I saw test and not a fail"
keyWordArguments('position 1', 'position 2') #Prints "I saw position 1 and position 2"

args = {'arg1': 'dictionaries', 'arg2' : 'stuff'}
keyWordArguments(**args) #Unpacks the dictionary "args" to be used as the function's parameters

def arbitaryKeywordArguments(*arguments, **keywords):
	sorted(keywords.keys(), key=str.lower) #Sorts based on the value the key points to
	for arg in arguments:
		print(arg)

	for kw in keywords:
		print(kw, ':', keywords[kw])

#arguments are thrown into a tuple titled "argument", while keywords are thrown into a dictonary (similar to a Java map?) of key-value pairs

arbitaryKeywordArguments('argument 1',  'argument 2',  keyword1='ZZZZZZZ', keyword2='I\'m a keyword')

def makePowerFunction(n): return lambda x: x ** n #Returns a function that raises a number x to the arbitrary power n declared on definition

square = makePowerFunction(2)
cube = makePowerFunction(3)

print(square(4)) #prints 16
print(cube(4)) #prints 64

pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
pairs.sort(key=lambda pair: pair[0]) #sorts the list pairs by the first element within each tuple within pairs
print(pairs)

def functionWithDoc():
	'''This is documentation.
Do nothing else'''
	pass

print(functionWithDoc.__doc__)
