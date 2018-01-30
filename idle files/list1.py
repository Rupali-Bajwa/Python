Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> CAP=['MCA','MCA2']
>>> CAP
['MCA', 'MCA2']
>>> CAP[1]
'MCA2'
>>> CAP[0]
'MCA'
>>> sd=['Rupali',25,'female']
>>> sd
['Rupali', 25, 'female']
>>> sd[1]=30
>>> sd
['Rupali', 30, 'female']
>>> sd.append('MCA(hons.)')
>>> sd
['Rupali', 30, 'female', 'MCA(hons.)']
>>> sd[-1]
'MCA(hons.)'
>>> sd
['Rupali', 30, 'female', 'MCA(hons.)']
>>> sd[-1]='Bajwa'
>>> sd
['Rupali', 30, 'female', 'Bajwa']
>>> sd[1]='Bajwa'
>>> sd
['Rupali', 'Bajwa', 'female', 'Bajwa']
>>> new[['a','s','e','f'],[2,3,4,5]]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    new[['a','s','e','f'],[2,3,4,5]]
NameError: name 'new' is not defined
>>> new=[['a','s','e','f'],[2,3,4,5]]
>>> new
[['a', 's', 'e', 'f'], [2, 3, 4, 5]]
