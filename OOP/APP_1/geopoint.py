from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather


class GeoPoint:

    def __init__(self, latitude, longitude):
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
        weather = Weather(apikey="26631f0f41b95fb9f5ac0df9a8f43c92", lat=self.latitude, lon=self.longitude)
        return weather.next_12h_simplified()


tokyo = GeoPoint(latitude=35.7, longitude=139.7)
print(tokyo.closest_parallel())
print(tokyo.get_time())
print(tokyo.get_weather())
