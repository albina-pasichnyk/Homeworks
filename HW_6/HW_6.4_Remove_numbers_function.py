"""
4. You have a file of unknown length. Write a function that will remove all numbers from each line of the file.
"""
import re

def remove_numbers(file_path: str):
    pattern = re.compile(r'[0-9]')
    with open(file_path, 'r+') as file:
        list_of_lines = file.readlines()
        file.seek(0)
        file.truncate()
        for each_line in list_of_lines:
            processed_line = pattern.sub('', each_line)
            file.write(processed_line)

#remove_numbers('task_1 (1).py')
