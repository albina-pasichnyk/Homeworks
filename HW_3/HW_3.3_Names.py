# Defining list of names friends
friends_names_list = ["John", "Marta", "James"]
enemies_names_list = ["John", "Johnatan", "Artur"]

# Process list of names using loop
for each_name in friends_names_list:
    if each_name == "James":
        continue
    elif enemies_names_list.count(each_name) == 0:
        print(f"{each_name} we are the best friends")
    else:
        print(f"{each_name} we are not friend anymore")
