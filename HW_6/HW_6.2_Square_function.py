"""
2. Write a function square that takes 1 argument, the side of the square, and returns 3 values (using a tuple):
the perimeter of the square, the area of the square, and the diagonal of the square.
"""

import math

def square_function(square_side: int) -> int or float:
    perimeter = 4 * square_side
    area = square_side ** 2
    diagonal = math.sqrt(2) * square_side
    return perimeter, area, diagonal

# print(square_function(5))
