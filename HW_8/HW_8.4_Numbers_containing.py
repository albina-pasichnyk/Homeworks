"""
4. Find all of the numbers from 1-1000 that have a 3 in them
"""

# Defining list variable with elements from range 1 to 1000
numbers_list = list(range(1, 1000))


# Filtering input sequence using comprehension
processed_list = [number for number in range(1, 1000) if '3' in str(number)]


def containing_number(sequence: list) -> list:
    """
    Function for processing and filtering list based on specific condition: contains number 3 in it.
    :param sequence:
    :return:
    """
    result_list = []
    for each in sequence:
        if '3' in str(each):
            result_list.append(each)
    return result_list


if __name__ == "__main__":
    print(containing_number(numbers_list)) # Print list result filtered using function for double-checking.
    print(processed_list) # Print list result filtered using comprehension.
    assert containing_number(numbers_list) == processed_list  # Check that lists filtered by comprehension and function are identical
