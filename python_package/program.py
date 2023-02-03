# envoke the fizzbuzz solution from fizzbuzz.py

from app.fizzbuzz import Fizzbuzz

one_to_100 = Fizzbuzz(1, 100)  # capitalisation is important when it comes to classes

print(one_to_100.fizzbuzz_list)