
from pdb import set_trace
"""
Test debugger functionality.
Trace the excution of various arithmetic functions.
Raise exceptions and try debugger's "post-mortem" state.
"""

def add_int(a, b):
    result = a + b
    return result

def substract_int(a, b):
    result = a - b
    return result

def divide_int(a, b):
    result = a / b
    return result

def multiply_int(a, b):
    result = a * b
    return result

def concat_str(str1, str2):
    result = ''
    result = str(str1)
    result += str(str2)
    return result

# Testing


STR1 = "ABC"
STR2 = "DEF"

def test_sum():
    A = 1
    B = 10
    result = add_int(A, B)
    return result

def test_div():
    A = 15
    B = 3
    result = divide_int(A, B)
    return result

def test_multi():
    A = 5
    B = 6
    result = A * B
    return result

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def test_exception_arithmetic():
    # built-in exceptions that are raised for various arithmetic errors
    if n == 1:
        raise OverflowError
    elif n == 2:
        raise ZeroDivisionError
    elif n == 3:
        raise FloatingPointError
    else:
        return 0

set_trace()
# test_sum()
# test_div()
# test_multi()

# factorial(5)
# test_exception()
# def test_exception_arithmetic
