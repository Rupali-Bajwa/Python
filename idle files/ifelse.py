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
>>> 
