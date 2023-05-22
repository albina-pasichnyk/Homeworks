"""
6. Create a function that accepts N parameters of type int. Calculate the sum of these parameters and return it.
"""

def calculate_sum(*number: int) -> int:
    return sum(number)

#print(calculate_sum(1, 9, 6, -4))
