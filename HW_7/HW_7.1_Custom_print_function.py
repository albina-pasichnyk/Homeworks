"""
1. Implement your own print function. It should work on all operating systems. You can't use build-in print function
"""
import sys


def custom_print(*args, sep=' ', end='\n', output_file=None):
    """
    Function custom_print prints objects to standard output, usually the console, separated by sep and followed by end
    by default.
    Sep, end, file, if present, must be given as keyword arguments.
    :param args: any amount of variables to be printed of any following types: str, int, float, list, set, tuple, dict
    :param sep: any specified separator to be used to separate printed variables, by default it's space
    :param end: any specified string to be added at the end of any print, by default it's new line
    :param output_file: any specified file where the print can be redirected, by default it is console
    """
    if output_file is None:
        for each in args:
            sys.stdout.write(f'{each}{sep}')
        sys.stdout.write(end)
        sys.stdout.flush()
    else:
        # Open the file in write mode
        with open(output_file, "w") as file:
            # Redirect standard output to the file
            sys.stdout = file
            # Use sys.stdout.write() to write text to the file
            for each in args:
                sys.stdout.write(f'{each}{sep}')
            sys.stdout.write(end)
            # Reset the standard output back to the console
            sys.stdout = sys.__stdout__


if __name__ == "__main__":
    custom_print('some string text')  # Print one string
    custom_print('several text', 'text 2', sep='\n')  # Print several strings, each on new line
    custom_print([1, 2, 4])  # Print list
    custom_print({4.5, '9', '6'}, end='\n\n')  # Print set ending 2 new lines
    custom_print(('Albina',))  # print tuple with single element
    custom_print({1: 'value', 2: 'other value'})  # Print dictionary
    # custom_print('text to file', 'Pyhton', sep='\n', output_file='output.txt')  # Print to file
