# Defining list of people with non-unique names
non_unique_names = ['Albina Pasichnyk', 'John Doe', 'Oksana Sea', 'Bohdan Dovbysh', 'Marta Fine', 'John Doe',
                    'Beta Ground', 'Oksana Sea', 'John Doe']
print(f"List of non-unique names: {non_unique_names}")

# Creating list of unique names using dictionary as temporary variable
dict_from_non_unique_names = dict().fromkeys(non_unique_names)
list_of_unique_names = list(dict_from_non_unique_names.keys())
print(f"List of unique names: {list_of_unique_names}")

# 2nd possible way using loop
# Copy list of non-unique names to another variable, to keep it original
# processed_names = non_unique_names.copy()
# # Generate list of people with unique names
# for each_name in processed_names:
#     name_counter = processed_names.count(each_name)
#     if name_counter != 1:
#         processed_names.remove(each_name)
# print(f"List of unique names: {processed_names}")
