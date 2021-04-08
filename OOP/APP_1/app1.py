from folium import Map

latitude = float("40.09")
longitude = float("-3.47")

antipode_latitude = latitude.__mul__(int(-1))

if longitude.__abs__().__gt__(float("180")):
    antipode_longitude = str("Invalid Longitude")
elif longitude.__lt__(float("0")):
    antipode_longitude = longitude.__add__(float("180"))
else:
    antipode_longitude = longitude.__sub__(float("180"))

location = list((antipode_latitude, antipode_longitude))
my_map = Map(location)
my_map.save(str("antipode.html"))

print(type(location))
print(location)
print(antipode_latitude)
print(antipode_longitude)
