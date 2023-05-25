"""
4. Implement your own implementation of function max and min (* additional argument amount of result, if you pass 2,
function should return 2 max values from the list)
"""


def custom_min(*args) -> int or float or str:
    """
    Function custom_min returns the smallest value among arguments.
    In case of single argument is passed, the function returns argument itself
    In case in no argument is passed, the function returns None.
    :param args: int, float, list, str
    :return: min value
    """
    if len(args) == 0:
        return None
    elif len(args) == 1 and type(args[0]) is list:
        my_list = args[0]
        min_value = my_list[0]
        for each_element in my_list:
            if each_element < min_value:
                min_value = each_element
        return min_value
    else:
        min_value = args[0]
        for each_arg in args:
            if each_arg < min_value:
                min_value = each_arg
        return min_value


def custom_max(*args) -> int or float or str:
    """
    Function custom_max returns the biggest value among arguments.
    In case of single argument is passed, the function returns argument itself
    In case in no argument is passed, the function returns None.
    :param args: int, float, list, str
    :return: max value
    """
    if len(args) == 0:
        return None
    elif len(args) == 1 and type(args[0]) is list:
        my_list = args[0]
        max_value = my_list[0]
        for each_element in my_list:
            if each_element > max_value:
                max_value = each_element
        return max_value
    else:
        max_value = args[0]
        for each_arg in args:
            if each_arg > max_value:
                max_value = each_arg
        return max_value


if __name__ == "__main__":
    # Tests for Min
    assert custom_min(6, 2, 4, 1) == 1  # Check for min among separate int values
    assert custom_min(-4, -3, 4) == -4  # Check for min among negative separate int values
    assert custom_min(6, 3.4, 99, 34.6) == 3.4  # Check for min among separate int and float values
    assert custom_min(7) == 7  # Check for min if only one argument is pass to function
    assert custom_min([7, 5, 12, 9]) == 5  # Check for min if single list is pass as argument
    assert custom_min([2, 3, 7], [2, 3, 5]) == [2, 3, 5]  # Check for min if several lists are pass as arguments
    assert custom_min('n', 'a', 'p') == 'a'  # Check for min among separate srt values
    assert custom_min() is None  # Check for min if no argument is pass to function
    # Tests for Max
    assert custom_max(6, 2, 9, 1) == 9  # Check for max among separate int values
    assert custom_max(-4, -3, -7) == -3  # Check for max among negative separate int values
    assert custom_max(6, 3.4, 99.3, 34.6) == 99.3  # Check for max among separate int and float values
    assert custom_max(7) == 7  # Check for max if only one argument is pass to function
    assert custom_max([7, 5, 12, 9]) == 12  # Check for max if single list is pass as argument
    assert custom_max([2, 3, 7], [2, 3, 5]) == [2, 3, 7]  # Check for max if several lists are pass as arguments
    assert custom_max('n', 'a', 'p') == 'p'  # Check for max among separate srt values
    assert custom_max() is None  # Check for max if no argument is pass to function
