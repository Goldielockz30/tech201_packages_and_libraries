# API

Application Programming Interface

How software can communicate with one another
The API is the translator between the Client and the Server

get means request the date, which is the main use of the API

### The API formats the returned data in JSON
```python
import requests
import json


post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

print(post_codes_req) # <Response [200]>

print(post_codes_req.status_code) # 200

print(post_codes_req.headers) # http headers returned
print(post_codes_req.content) # raw content
print(post_codes_req.json) # json content
print(type(post_codes_req.json())) # <class 'dict'>


# If I want specific details
# I'ts important to look at API documentation when sending something over, to get the rules right

json_body = json.dumps({"postcodes": ["PR8 5DB", "M45 6GN", "EX165BL"]})
headers = {"Content-Type": "application/json"}


# this is the data we want to send
post_multi_red = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body) # we don't need the end code because we are asking for specific things from the API,


print(post_multi_red.json())
```

```python


__init__    # this will be the first things to happen when we use this package
```



```python
class Fizzbuzz:

    def __init__(self, start_of_range, end_of_range):
        self.fizzrange = range(start_of_range, end_of_range + 1)
        self.fizzbuzz_list = []
        self._fizzbuzz_iterator()

    def _divisible_by(self, num1, num2):
        if num1 % num2 == 0:
            return True
        else:
            return False

    def _fizzbuzz_iterator(self):

        for num in self.fizzrange:
            if self._divisible_by(num, 15):
                self.fizzbuzz_list.append("fizzbuzz")
            elif self._divisible_by(num, 5):
                self.fizzbuzz_list.append("buzz")
            elif self._divisible_by(num, 3):
                self.fizzbuzz_list.append("fizz")
            else:
                self.fizzbuzz_list.append(num)


```

```python
# envoke the fizzbuzz solution from fizzbuzz.py

from app.fizzbuzz import Fizzbuzz

one_to_100 = Fizzbuzz(1, 100)  # capitalisation is important when it comes to classes

print(one_to_100.fizzbuzz_list)
```

```python

# Background to application/package

# Sample info in this file:

# Version = "1.0"

# description="Python app"

# author="Luke Fairbrass"

# url="https://www.python.org"

from setuptools import setup # we want to import tools related to setup

setup(name="app")
```
