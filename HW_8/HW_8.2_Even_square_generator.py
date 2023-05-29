"""
2. Create a function that can return the squares of even elements for the range 0 to 1000000000 inclusive. The
solution should work and not freeze your computer.
"""


def even_square_generator():
    """
    Generator that return one by one square of even numbers from 0 to 1000000000 inclusively
    :return: int value
    """
    number_list = range(0, 1000000001)  # stop arg incremented by 1, since it's not included by build-in function
    counter = 0
    while counter < len(number_list):
        yield number_list[counter] * number_list[counter]
        counter += 2


def even_square_function() -> list:
    """
    Simple function that generates list of square of even numbers from 0 to 1000000000 inclusively
    :return: processed list of values
    """
    number_list = list(range(0, 1000000001))  # stop arg incremented by 1, since it's not included by build-in function
    result = []
    for each in number_list:
        if each % 2 == 0:
            result.append(each * each)
    return result


if __name__ == "__main__":
    # Check performance for generator function usage
    generator_result = even_square_generator()
    for each in generator_result:
        print(each)

    # Check performance for simple function usage
    # simple_result = simple_function()
    # for each in simple_result:
    #     print(each)
