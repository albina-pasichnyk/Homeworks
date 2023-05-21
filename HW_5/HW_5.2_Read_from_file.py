# Before running the code from current file, perform execution for "HW_5.1_Writing_tuple_to_file.py"
# Open file and read data from it
with open('./test/data/file_with_tuples.txt') as file:
    file_content = file.readlines()

print(file_content)

# Perform mathematical operation using read file content as input.
# Print the result of operation to console
for line in file_content:
    left_operand, right_operand, operator = line.split()
    left_operand = int(left_operand)
    right_operand = int(right_operand)
    print(left_operand, right_operand, operator)
    if operator == '1':
        print(f'Result of addition operation is ', left_operand + right_operand)
    elif operator == '2':
        print(f'Result of subtraction operation is ', left_operand - right_operand)
    elif operator == '3':
        print(f'Result of multiplication operation is ', left_operand * right_operand)
