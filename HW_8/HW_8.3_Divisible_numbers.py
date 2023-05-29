"""
3. Find all of the numbers from 1-1000 that are divisible by 7
"""

# Defining list variable with elements from range 1 to 1000
numbers_list = list(range(1, 1000))

# Filtering input sequence using comprehension
processed_list = [number for number in range(1, 1000) if number % 7 == 0]


def divisible_number(sequence: list) -> list:
    """
    Function for processing and filtering list based on specific condition: divisible by 7
    """
    result_list = []
    for each in sequence:
        if each % 7 == 0:
            result_list.append(each)
    return result_list


if __name__ == "__main__":
    print(processed_list)  # Print list result filtered using comprehension.
    print(divisible_number(numbers_list))  # Print list result filtered using function for double-checking.
    assert divisible_number(numbers_list) == processed_list  # Check that lists filtered by comprehension and function are identical
