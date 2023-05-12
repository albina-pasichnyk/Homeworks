# Defining 3 blacklists of people
casino_blacklist = {'Albina Pasichnyk', 'Oksana Sea', 'John Doe', 'Sam Fluffy', 'Alisa Forest', 'Anfisa Forest'}
poker_blacklist = {'Alisa Forest', 'Bohdan Dovbysh', 'Halyna Far', 'Oksana Sea', 'Sam Fluffy', 'Alf Red'}
alcohol_blacklist = {'Yurii Far', 'Alisa Forest', 'Alf Red', 'Bohdan Dovbysh', 'Oksana Sea', 'Albina Pasichnyk'}

# Finding all people who are on all blacklists
intersections = casino_blacklist.intersection(poker_blacklist.intersection(alcohol_blacklist))
print(intersections)
