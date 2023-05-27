"""
1. Create a decorator that prints to the console the name of the function that was called. The function should work
as intended. For example, create a pair of functions for the arithmetic operations of summation and multiplication.
When calling these functions, the result of the operation must be returned and the name of the function that was
called must be displayed in the console with the result. Small hint (__name__)
"""


def function_name_decorator(function):
    def wrapper(*args):
        func_name = function.__name__
        return f'{func_name}\n{function(*args)}'
    return wrapper

@function_name_decorator
def summation(*args: int or float) -> int or float:
    if len(args) == 0:
        return 'No arguments were passed to function'
    else:
        return sum(args)

@function_name_decorator
def multiplication(*args: int or float) -> int or float:
    if len(args) == 0:
        return 'No arguments were passed to function'
    else:
        result = 1
        for each in args:
            result *= each
    return result


if __name__ == "__main__":
    print(multiplication(12, 5))
    print(summation(12, 5))
