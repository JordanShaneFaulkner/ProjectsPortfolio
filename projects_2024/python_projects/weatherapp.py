import requests 
from tabulate import tabulate 
from geopy.geocoders import Nominatim



class City:
    def __init__(self,name,lat,long,units = 'metric'):
        self.name = name 
        self.lat = lat 
        self.long = long 
        self.units = units
        self.get_data()
    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.long}&appid=69efb4d5c80dbab157c8881c1feabc69")
        except:
            print("No Access") 
        response_json = response.json()
        self.temp_min = response_json["main"]["temp_min"]
        self.temp_max = response_json["main"]["temp_max"]
        self.feels_like = response_json["main"]["feels_like"]
        self.current_temp = response_json["main"]["temp"] 
        self.humidity = response_json["main"]["humidity"]
    def temp_print(self):
        units_symbol = 'C'
        if self.units == 'imperial':
            units_symbol = 'F'
            
        print(f"""The current weather in {self.name} is {self.current_temp} °{units_symbol}, 
              with High temps of {self.temp_max}°C, and low temps of {self.temp_min}°{units_symbol}, and humidity of {self.humidity}°{units_symbol}.
              It currently feels like {self.feels_like}°{units_symbol}. """)



def get_city_data():
    city = input('Enter the address in which you would like the weather report for: ')
    Nominatim(user_agent='jfaulkne')
    location = geolocator.geocode(city)
    print((location.latitude, location.longitude))
get_city_data()
