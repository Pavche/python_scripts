#!/usr/bin/python3
# This script demonstrates string manipulation
# The upper(), lower(), isupper(), and islower() String Methods
# The startswith() and endswith() String Methods
# The join() and split() String Methods

raw_str = r'These are a raw strings. That is Carol\'s cat. That is Kate\'s dog'
print(raw_str)

str1 = 'Hello world!'
str1_up = str1.upper()
str1_low= str1.lower()
print('Normal case:' + str1_low + '\nLower case:' + str1_low +'\nUpper case:' + str1_up)  

print('Please, enter a string.')
str_new = input()

print('Checking if \"' + str_new + '\" or upper case.')
if str_new.isupper():
	print('Yes.')
else:
	print('No.')

print('Checking if \"' + str_new + '\" or lower case.')
if str_new.islower():
	print('Yes.')
else:
	print('No.')

print('Hello world!')
print('Does \'Hello world!\' starts with \'Hello\'?')
'Hello world!'.startswith('Hello')
print('Does \'Hello world!\' ends with \'world!\'?')
'Hello world!'.endswith('Hello')

print('\nJoining strings')
str1=' '.join(['My','name','is','Simon'])
str2='ABC'.join(['My', 'name', 'is', 'Simon'])

# Rainbow colors
str3=', '.join(['The rainbow colors are:','red','orange','yellow','green','blue','indigo','violet'])
print(str1,'\n',str2,'\n',str3)

print('\nAligned text')
print('Hello (right-justify)'.rjust(30,'_'))
print('Hello (right-justify)'.rjust(30,'>'))
print('Hello (left-justify)'.ljust(30, '<'))
