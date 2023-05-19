import re

# Defining list of variable names
names_in_camel_case = ["FirstItem", "FriendsList", "MyTuple"]

# Defining pattern for finding position upper case character, excluding first one at the beginning of string
pattern = re.compile(r'(?<!^)(?=[A-Z])')

# Processing of names in camel case using regex pattern, lowering it, and adding to new list
snake_case_list = []
for name in names_in_camel_case:
    name = pattern.sub('_', name).lower()
    snake_case_list.append(name)
print(snake_case_list)
