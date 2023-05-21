import os
import random

# Defining empty list of tuples
list_of_tuples = []

# Generating list of tuples using randomizer for left, right operand and operator
for _ in range(100):
    left_operand = random.randint(1, 100)
    right_operand = random.randint(1, 100)
    operator = random.randint(1, 3)
    list_of_tuples.append((left_operand, right_operand, operator))

print(list_of_tuples)

# Creating directory. If such directory already exist - re-write
os.makedirs('./test/data', exist_ok=True)

# Creating file and writing to it data from list of tuples
with open('./test/data/file_with_tuples.txt', 'w') as file:
    for each_tuple in list_of_tuples:
        file.write(f'{each_tuple[0]} {each_tuple[1]} {each_tuple[2]}\n')
