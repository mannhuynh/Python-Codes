"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
-Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

# locations = {'North America': 
#                 {'USA': ['Mountain View', 'Atlanta']},
#             'Asia': {
#                 'China': ['Shanghai'],
#                 'India': ['Bangalore']},
#             'Africa': {'Egypt': ['Cairo']}
    
# }

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

print(locations)
#{'North America': {'USA': ['Mountain View', 'Atlanta']}, 'Asia': {'India': ['Bangalore'], 'China': ['Shanghai']}, 'Africa': {'Egypt': ['Cairo']}}

"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
American City
American City
"""
for value in sorted(locations['North America']['USA']):
    print(value)

# Atlanta
# Mountain View

"""2. All cities in Asia, in alphabetic
order, next to the name of the country.
Asian City - Country
Asian City - Country
"""
city_country = []

for key, value in sorted(locations['Asia'].items()):
    value_key = value[0] + ' - ' + key
    city_country.append(value_key)

for item in sorted(city_country):
    print(item)

# Bangalore - India
# Shanghai - China


#----------------TESTING-------------------#
# asia_cities = []
# for countries, cities in locations['Asia'].items():
#     city_country = cities[0] + " - " + countries 
#     print(cities)
#     asia_cities.append(city_country)
#     print(city_country)
# asia_sorted = sorted(asia_cities)
# for city in asia_sorted:
#     print(city)
