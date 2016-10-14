Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> with open('num.txt') as f:
	w, h = [int(x) for x in next (f).split()]
	array = []
	for lin in f:
		array.append([int(x) for x in line.split()])

		
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    with open('num.txt') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'num.txt'
>>> with open('num.txt') as f:
	w, h = [int(x) for x in next (f).split()]
	array = []
	for lin in f:
		array.append([int(x) for x in line.split()])
average = 0
SyntaxError: invalid syntax
>>> int average = 0
SyntaxError: invalid syntax
>>> average = int 0
SyntaxError: invalid syntax
>>> average = 0
>>> sum = 0
>>> for n in numbers:
	sum = sum + n
	average = sum / len(n)
print 'The average of the numbers is: ', average
SyntaxError: Missing parentheses in call to 'print'
>>> print ('The average of the numbers is: ', average)
The average of the numbers is:  0
>>> 
