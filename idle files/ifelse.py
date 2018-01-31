Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=int(input("Enter the number"))
Enter the number34
>>> if x<40
SyntaxError: invalid syntax
>>> if x<0:
	x=0
	print("Negative number")
	elif x==0:
		
SyntaxError: invalid syntax
>>> if x<0:
	x=0
	print("Negative number")
elif x==0:
	print("Number is zero")
elif x==1:
	print("Number is single")
else:
	print("More then one")

	
More then one
>>> words=['dog','cow','tiger']
>>> for w in words:
	print(w,len(w))

	
dog 3
cow 3
tiger 5
>>> for i in [1:10]:
	
SyntaxError: invalid syntax
>>> for i in :10:
	
SyntaxError: invalid syntax
>>> for i in 10:
	print (i)

	
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    for i in 10:
TypeError: 'int' object is not iterable
>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> fori in range(-10,-100,-30):
	
SyntaxError: invalid syntax
>>> for i in range(-10,-100,-20):
	print(i)

	
-10
-30
-50
-70
-90
>>> 
KeyboardInterrupt
>>> a = ['pallvi,'has','a','cute','face']
     
SyntaxError: invalid syntax
>>> a = ['pallvi','has','a','cute','face']
>>> for i in range(len(a))
SyntaxError: invalid syntax
>>> a = ['pallvi','has','a','cute','face']
>>> for i in range(len(a)):
	
SyntaxError: multiple statements found while compiling a single statement
>>> a = ['pallvi','has','a','cute','face']
>>> for i in range(len(a)):
	
SyntaxError: multiple statements found while compiling a single statement
>>> a = ['pallvi','has','a','cute','face']
>>> for i in range(len(a)):
	print(i,a[i])

	
0 pallvi
1 has
2 a
3 cute
4 face
>>> list[range(10)]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    list[range(10)]
TypeError: 'type' object is not subscriptable
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list=[1,3,4,5,6,3,3,2,4,90]
>>> if list[0]
SyntaxError: invalid syntax
>>> list=[0,3,4,5,6,3,3,2,4,90]
>>> range(10)
range(0, 10)
>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> name="My name is Rupali"
>>> for i in name:
	print (i)

	
M
y
 
n
a
m
e
 
i
s
 
R
u
p
a
l
i
>>> for n in range(10):
	if n==6:
		break
	print(n, end-',')

	
Traceback (most recent call last):
  File "<pyshell#58>", line 4, in <module>
    print(n, end-',')
NameError: name 'end' is not defined
>>> for n in range(10):
	if n==6:
		break
	print(n,end-1)

	
Traceback (most recent call last):
  File "<pyshell#64>", line 4, in <module>
    print(n,end-1)
NameError: name 'end' is not defined
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('banana')
2
>>> fruits.index('apple')
1
>>> fruits.index('banana',3)
3
>>> fruits.index('banana',4)
6
>>> fruits.reverse()
>>> friuts
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    friuts
NameError: name 'friuts' is not defined
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grapes')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grapes']
>>> fruits.sort
<built-in method sort of list object at 0x0227A850>
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grapes', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grapes', 'kiwi', 'orange']
>>> 
