# Defining list of elements
list_of_elements = [1, 2, 3, 4, 5, 6, 7, 8]

# Creating empty lists for values with odd and even indexes
odd_index_list = []
even_index_list = []

# Process list of elements in loop based on indexes using enumarate function
for index, element in enumerate(list_of_elements):
    if index % 2 == 0:
        even_index_list.append((index, element))
    else:
        odd_index_list.append((index, element))
print(f"List of elements with odd index [(index, value)]:{odd_index_list}")
print(f"List of elements with even index [(index, value)]:{even_index_list}")
