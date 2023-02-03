# Modules

import os
import math, datetime, sys

working_directory = os.getcwd() # using the os module and its build in functionality to run this
print(working_directory)

# modules are simpler to use than libraries and used to import files, modules are used alot in devops


def return_user_id():
    print(os.getpid())

def return_user_name():
    print(os.uname())

print(datetime.date.today()) # use datetime module to get todays date

print((sys.path))

print(math.remainder(1, 5))

# When you are building a program, it's really important to think weather you need to make a class/object or simply a function. You may not even need to make a function yourself, if there is a module that does what you are looking for already.

# Built-in functions

# print
# len()
# type()


