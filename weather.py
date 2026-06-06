import requests
import json

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "your api key"
CITY = ("your city")


def kelvin_to_celsius_fahrenheit(kelvin):
            celsius = kelvin - 273.15
            fahrenheit = (9 / 5) * celsius + 32
            return celsius, fahrenheit


        url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
print(f"Temperature in {CITY} {temp_celsius:.2f}degree celsius")