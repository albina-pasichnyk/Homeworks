"""
3. Implement your own implementation of the function map
Note: tasks 2-3 must have the following signature def function_name(callback, sequence). Add annotations yourself.
Functions must be able to work with integers, floats, and strings as elements of sequences.
"""


def custom_map(callback, sequence):
    """
    Function custom_map is used to return a list of results after applying a given function to each item of an iterable
    :param callback: function with specific rule to be applied
    returns True only for those elements that have to be in filtered result
    :param sequence: list, set, tuple with allowed int, float, str values
    :return: object with int, float, str values
    """
    result = []
    for each_element in sequence:
        result.append(callback(each_element))
    return result


def callback_f(number):
    return number + 100


if __name__ == "__main__":
    # Filtering List
    assert list(custom_map(lambda text: text.lower(), ['Some', 'TEST', 'Text', 'valueS'])) == ['some', 'test', 'text',
                                                                                               'values']  # Check for mapping for str values of the list
    assert list(custom_map(callback_f, [10, 20, 30])) == [110, 120, 130]  # Check mapping for int values of the list
    assert list(custom_map(callback_f, [6.4, 4.1, 12.5, 10.0])) == [106.4, 104.1, 112.5,
                                                                    110.0]  # Check mapping for float values of the list
    # # Filtering Set
    assert set(custom_map(lambda text: text.lower(), {'Some', 'TEST', 'Text', 'valueS'})) == {'some', 'test', 'text',
                                                                                              'values'}  # Check for mapping for str values of the set
    assert set(custom_map(callback_f, {10, 20, 30})) == {110, 120, 130}  # Check mapping for int values of the set
    assert set(custom_map(callback_f, {6.4, 4.1, 12.5, 10.0})) == {106.4, 104.1, 112.5,
                                                                   110.0}  # Check mapping for float values of the set
    # # Filtering tuple
    assert tuple(custom_map(lambda text: text.lower(), ('Some', 'TEST', 'Text', 'valueS'))) == (
    'some', 'test', 'text', 'values')  # Check for mapping for str values of the tuple
    assert tuple(custom_map(callback_f, {10, 20, 30})) == (110, 120, 130)  # Check mapping for int values of the tuple
    assert tuple(custom_map(callback_f, {6.4, 4.1, 12.5, 10.0})) == (
    106.4, 104.1, 112.5, 110.0)  # Check mapping for float values of the tuple
