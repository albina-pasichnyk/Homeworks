# Put file in the directory where the python file is executed from
# Open file and read data from it
with open('text.txt') as file:
    file_content = file.read().lower()

print(file_content)

# Processing file content using 2 loops.
# 1st - creation dictionary of letter to count.
dictionary_of_letters = {}
for each_char in file_content:
    if each_char.isalpha():
        dictionary_of_letters.update({each_char: None})

# 2nd loop - count occurrence of each letter in the file content
for key, value in dictionary_of_letters.items():
    dictionary_of_letters.update({key: file_content.count(key)})
print(dictionary_of_letters)

# Way #2 - Processing file content using one loop with conditions
dictionary_of_letters = {}
for each_char in file_content:
    if each_char.isalpha():
        if dictionary_of_letters.get(each_char):
            dictionary_of_letters.update({each_char: dictionary_of_letters.get(each_char)+1})
        else:
            dictionary_of_letters.update({each_char: 1})

print(dictionary_of_letters)
