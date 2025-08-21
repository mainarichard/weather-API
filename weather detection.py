import requests

import json

def get_weather(city):
    api_key = 'e2ec2974153b73f533ce5a61ed4a9ef4'
    baseurl = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(baseurl, params=params)
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(baseurl, params=params)
    weather_data = response.json()
    if weather_data['cod'] == 200:
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']

        print(f"Current temperature in {city} is {temp}°C")
        print(f"Humidity in {city} is {humidity}%")
        print(f"Weather description in {city} is {description}")
    else:
        print(f"City not found, please check the name and try again.")
        return None

city = input("Enter the city name: ")
get_weather(city)