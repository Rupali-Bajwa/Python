Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def is_prime(n):
	for i in range(2,n)
	
SyntaxError: invalid syntax
>>> def is_prime(n):
	for i in range(2,n):
		if n%i==0:
			return False
	return True
