# tech201_packages_and_libraries
tech201_packages_and_libraries

# Modules
```python
import os
import math, datetime, sys

working_directory = os.getcwd() # using the os module and its build in functionality to run this
print(working_directory)
```
### modules are simpler to use than libraries and used to import files, modules are used alot in devops

```python
def return_user_id():
    print(os.getpid())

def return_user_name():
    print(os.uname())

print(datetime.date.today()) # use datetime module to get todays date

print((sys.path))

print(math.remainder(1, 5))
```
When you are building a program, it's really important to think weather you need to make a class/object or simply a function. You may not even need to make a function yourself, if there is a module that does what you are looking for already.

# Built-in functions

- print
- len()
- type()


```python


from modules import *

return_user_id()

return_user_name()
```

or we could use
```

# import modules

# modules.return_user_id()
```

# Python Libraries
```
we can import methods and functions
python has loads of libraries, we can import any of them if we know what we want
because its opensource, free
I'ts been around for a long time
I'ts a simple language,
I'ts built into the language

# import random     # to import the library random
# print(random.random())
```
```python
from random import random          # if we don't want the entire library


import math

print(random())     # we don't need to mention where, random because we call it from above


num_float = 23.66

print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)
```
# pip and packages

pip is Pythons package manager and installer  

### import requests
```python


request_bbc = requests.get("https://www.google.co.uk")

print(request_bbc.status_code)
print(request_bbc.content)
```

















