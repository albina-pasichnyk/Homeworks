"""
5. Implement your own all function
"""


def custom_all(args):
    """
    Function custom_all returns True if bool(x) is True for all values x in the iterable.
    In case if no argument is passed, function returns True.
    :param args: list, tuple, set
    :return: True or False
    """
    for element in args:
        if not element:
            return False
    return True


if __name__ == "__main__":
    assert custom_all([True, True, True]) == True  # Check if all values of a list are True, among similar ones
    assert custom_all([True, False, True]) == False  # Check if all values of a list are True, among different ones
    assert custom_all(('QA', 'Dev', 'AQA')) == True  # Check if all values of a tuple are True, among similar ones
    assert custom_all(('SM', 'PO', '')) == False  # Check if all values of a tuple are True, among different ones
    assert custom_all({1, 7, 6}) == True  # Check if all values of a set are True, among all True
    assert custom_all({None, 8, -4}) == False  # Check if all values of a set are True, among True and False
