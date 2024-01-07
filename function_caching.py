# import functools

# @functools.lru_cache(maxsize=None)
# def fibo(n):
#     if n<2:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)

# fibo_input=eval(input("Enter number to find the fibonaci series: "))
# print(f"Finovancci series of {fibo_input}is {fibo(fibo_input)}")

#This is the concept of memoization where we store the result of values given and 
#when the same value is to be operated, rather than re-computing it gets the value from the cache
from functools import lru_cache
import time

@lru_cache(maxsize=None)
def mul(n):
    time.sleep(3)
    return n*n

print(f"Multiply of 2 is {mul(2)}")
print(f"Multiply of 2 is {mul(3)}")
print(f"Multiply of 2 is {mul(4)}")
print(f"Multiply of 2 is {mul(5)}")

print(f"Multiply of 2 is {mul(2)}")
print(f"Multiply of 2 is {mul(3)}")
print(f"Multiply of 2 is {mul(4)}")
print(f"Multiply of 2 is {mul(5)}")