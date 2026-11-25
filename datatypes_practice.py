Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatypes
>>> type(2)
<class 'int'>
>>> type(2.5)
<class 'float'>
>>> type(10.0)
<class 'float'>
>>> type(56)
<class 'int'>
>>> type(6.9)
<class 'float'>
>>> type(8j)
<class 'complex'>
>>> type(8i)
SyntaxError: invalid decimal literal
>>> type(0+4j)
<class 'complex'>
>>> type(0j+9)
<class 'complex'>
>>> type('hi')
<class 'str'>
>>> type("tyu")
<class 'str'>
>>> type('''ui''')
<class 'str'>
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> type(true)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> type(false)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    type(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
