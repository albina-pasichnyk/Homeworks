# Defining groups of people based on their food preferences
omnivores = {'Alisa Forest', 'Halyna Far', 'Albina Pasichnyk'}
vegetarians = {'Beta Ground', 'Oksana Sea', 'Bohdan Dovbysh'}

# Creating list of guest who can eat vegetables and herbs.
# Since omnivores can eat vegetables and herbs the same as vegetarians, it means that all guests can eat vegetables.
guest_list = omnivores.union(vegetarians)
print(guest_list)
