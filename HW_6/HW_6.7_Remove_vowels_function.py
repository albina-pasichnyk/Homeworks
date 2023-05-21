"""
7. Write a function that takes in a string and returns the string with all the vowels removed.
"""
import re

def remove_vowels(input_text: str) -> str:
    pattern = re.compile(r'[aeiouyAEIOU]')
    return pattern.sub('', input_text)

#print(remove_vowels("Oleksandr"))
