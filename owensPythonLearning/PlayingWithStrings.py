print("""\
This is a test
of multiple line printing
in python""" )

print(3 * 'un' + 'ium')

word = 'pythonz'
for i in range(len(word)):
	print(word[:i + 1])

def wordContainsZ(wordToCheck):
	for j in range(len(wordToCheck)):
		if wordToCheck[j] is 'Z' or wordToCheck[j] is 'z':
			print('The word', wordToCheck, 'contains a z or Z')
			break
	else:
		print('The word', wordToCheck, 'does not contain a z or Z')

def betterWordContainsZ(wordToCheck):
	if 'Z' in word or 'z' in word:
		print('The word', wordToCheck, 'contains a z or Z')
	else:
		print('The word', wordToCheck, 'does not contain a z or Z')

wordContainsZ(word)
betterWordContainsZ(word)
