# Defining string to convert variable
string_to_convert = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "

# String processing by splitting it by special symbols to groups, which contains key & value.
processing_list = string_to_convert.strip().replace('&&', '&').split('&')

# Defining empty dictionary variable
converted_dictionary = {}

# Splitting each group to key and value. Updating dictionary in loop with processed key and value.
for each_element in processing_list:
    processing_list = each_element.split('=')
    key = processing_list[0]
    value = processing_list[1]
    converted_dictionary.update({key: value})

print(converted_dictionary)
