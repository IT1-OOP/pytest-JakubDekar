
import math

def add(a, b):
    return a + b
def add_wrong(a,b):
    return 2*a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def multiply_wrong(a,b):
    return a*b + 1
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def log(a, b):
    if a <= 0:
        raise ValueError("Cannot take log of non-positive number!")
    if b <= 0:
        raise ZeroDivisionError("Cannot take log with non-positive base!")
    if b == 1:
        raise NameError("Cannot take log with base 1!")
    return math.log(a, b)