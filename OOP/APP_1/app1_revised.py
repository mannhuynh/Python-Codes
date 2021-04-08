from folium import Map

latitude = 40.09
longitude = -3.47

antipode_latitude = latitude * -1

if longitude.__abs__() > 180:
    antipode_longitude = str("Invalid Longitude")
elif longitude < 0:
    antipode_longitude = longitude + 180
else:
    antipode_longitude = longitude + 180

location = [antipode_latitude, antipode_longitude]
my_map = Map(location)
my_map.save(str("antipode.html"))

print(type(location))
print(location)
print(antipode_latitude)
print(antipode_longitude)
