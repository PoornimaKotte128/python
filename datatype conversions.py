Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

#datatype conversions
int(34)
34
int(345)
345
int(3.6)
3
int(4+8j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(4+8j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int('hi')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int('hi')
ValueError: invalid literal for int() with base 10: 'hi'
int(True)
1
int(False)
0
int(true)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
float(112)
112.0
float(132.5)
132.5
float(8j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(8j)
TypeError: float() argument must be a string or a real number, not 'complex'
float("ioio")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float("ioio")
ValueError: could not convert string to float: 'ioio'
float(True)
1.0
float(False)
0.0
float(true)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    float(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
complex(12)
(12+0j)
complex(2.8)
(2.8+0j)
complex(8j)
8j
complex(9+8j)
(9+8j)
>>> complex(5-7j)
(5-7j)
>>> complex('oiii')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    complex('oiii')
ValueError: complex() arg is a malformed string
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> complex(true)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    complex(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> str(12)
'12'
>>> str(67.9)
'67.9'
>>> str('oi')
'oi'
>>> str(8j)
'8j'
>>> str(True)
'True'
>>> str(False)
'False'
>>> bool(23)
True
>>> bool(3.4)
True
>>> bool(8j)
True
>>> bool('jio')
True
>>> bool(True)
True
>>> bool(False)
False
