"""
2. Implement your realization of the function filter
Note: tasks 2-3 must have the following signature def function_name(callback, sequence). Add annotations yourself.
Functions must be able to work with integers, floats, and strings as elements of sequences.
"""


def custom_filter(callback, sequence):
    """
    Function custom_filter is used to filter elements based on specific conditions. it returns a sequence from those 
    elements of iterable for which function returns True. 
    :param callback: function with specific filter rules that
    returns True only for those elements that have to be in filtered result 
    :param sequence: list, set, tuple with allowed int, float, str values
    :return: object with int, float, str values
    """
    result = []
    for each_element in sequence:
        if callback(each_element) is True:
            result.append(each_element)
    return result


def callback_f(item):
    if item < 10:
        return True
    else:
        return False


if __name__ == "__main__":
    # Filtering List
    assert list(custom_filter(lambda name: name.startswith('Al'), ['Oksana', 'Albina', 'Halyna', 'Alexa'])) == ['Albina', 'Alexa']  # Check for filtering among str values of the list
    assert list(custom_filter(callback_f, [6, 4, 77, 1])) == [6, 4, 1]  # Check for filtering among int values of the list
    assert list(custom_filter(callback_f, [6.4, 4.1, 12.5, 10.0])) == [6.4, 4.1]  # Check for filtering among float values of the list
    # Filtering Set
    assert set(custom_filter(lambda name: name.startswith('Al'), {'Oksana', 'Albina', 'Halyna', 'Alexa'})) == {'Albina', 'Alexa'}  # Check for filtering among str values of the set
    assert set(custom_filter(callback_f, {6, 4, 77, 1})) == {6, 4, 1}  # Check for filtering among int values of the set
    assert set(custom_filter(callback_f, {6.4, 4.1, 12.5, 10.0})) == {6.4, 4.1}  # Check for filtering among float values of the set
    # Filtering tuple
    assert tuple(custom_filter(lambda name: name.startswith('Al'), ('Oksana', 'Albina', 'Halyna', 'Alexa'))) == ('Albina', 'Alexa')  # Check for filtering among str values of the tuple
    assert tuple(custom_filter(callback_f, (6, 4, 77, 1))) == (6, 4, 1)  # Check for filtering among int values of the tuple
    assert tuple(custom_filter(callback_f, (6.4, 4.1, 12.5, 10.0))) == (6.4, 4.1)  # Check for filtering among float values of the tuple
