# This program is to create the map.html file
# It will get the latitude and longitude to show a maker on the map
# When clicking the marker, there will be a popup show the weather of that coordinate
#

from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather
from random import uniform
from folium import Map, Marker, Popup


class GeoPoint(Marker):
    """
    GeoPoint inherited from Marker to use the add_to() method
    """
    # Below are class attributes, accessed directly from class, not instance
    # Using: GeoPoint.latitude_range, and GeoPoint.longitude_range
    latitude_range = (-90, 90)
    longitude_range = (-180, 180)

    def __init__(self, latitude, longitude):
        super().__init__(location=[latitude, longitude])
        self.latitude = latitude
        self.longitude = longitude

    def closest_parallel(self):
        return round(self.latitude), round(self.longitude)

    def get_time(self):
        """
        Using TimezoneFinder().timezone_at() to cast given latitude and longitude
        into a string representation ex: "Asia/Tokyo"
        Details:
        print(timezone_string)  # this print Etx/GMT-9 for lat=5.7 and 139.7
        print(datetime.now(timezone("Asia/Tokyo")))
        """
        timezone_string = TimezoneFinder().timezone_at(lat=self.latitude, lng=self.longitude)
        time_now = datetime.now(timezone(timezone_string))
        return time_now

    def get_weather(self):
        """
        Weather class need apikey from https://openweathermap.org.
        """
        weather = Weather(apikey="26631f0f41b95fb9f5ac0df9a8f43c92",
                          lat=self.latitude,
                          lon=self.longitude)
        return weather.next_12h_simplified()

    @classmethod
    def random(cls):
        """
        This class method generate the random latitude and longitude using: GeoPoint.random()
        """
        return cls(latitude=uniform(-90, 90), longitude=uniform(-180, 180))


# Setup latitude and longitude
latitude = 30.39258
longitude = -91.01458
locations = [[30.39258, -91.01458],
             [29.70526, -95.46064],
             [30.22193, -92.04208],
             [29.95784, -90.06328],
             [30.39524, -88.89168]]

# Instantiate my_map with Map from folium
my_map = Map(location=[30.39258, -91.01458])

for lat, lon in locations:
    # Create a GeoPoint instance
    geo_point = GeoPoint(latitude=lat, longitude=lon)

    # Call the get_weather() method to show in the popup
    popup_weather = geo_point.get_weather()

    # Revised the popup_weather contain:
    popup_contain = f"""
    { popup_weather[0][0][-8:-6] }h: { round(popup_weather[0][1]) }°F <img src="http://openweathermap.org/img/wn/{ popup_weather[0][-1] }@2x.png" width=35px>
    <hr style="margin:1px">
    { popup_weather[1][0][-8:-6] }h: { round(popup_weather[1][1]) }°F <img src="http://openweathermap.org/img/wn/{ popup_weather[1][-1] }@2x.png" width=35px>
    <hr style="margin:1px">
    { popup_weather[2][0][-8:-6] }h: { round(popup_weather[2][1]) }°F <img src="http://openweathermap.org/img/wn/{ popup_weather[2][-1] }@2x.png" width=35px>
    <hr style="margin:1px">
    { popup_weather[3][0][-8:-6] }h: { round(popup_weather[3][1]) }°F <img src="http://openweathermap.org/img/wn/{ popup_weather[3][-1] }@2x.png" width=35px>
    <hr style="margin:1px">
    """
    # Instantiate a popup to show weather on the marker of the map
    # Popup class get a string as an argument
    popup = Popup(popup_contain, max_width=400)

    # Add the popup to the geo_point
    popup.add_to(geo_point)

    # Add the geo_point to my_map
    geo_point.add_to(my_map)

# Save the Map instance into map.html
my_map.save("map.html")
