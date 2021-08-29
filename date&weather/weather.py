import requests
import os
from datetime import datetime

user_api = os.environ['13b7fc15f0c0a6edbfbf5050437ddacf']
loc = input("Enter city name: ")

comp_api_link = "api.openweathermap.org/data/2.5/weather?q="+loc+"&appid="+user_api

api_link = requests.get(comp_api_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print("Invaild City: {}, Please check the City name".format(loc))
else:
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


    print("-----------------------------------------------------------")
    print("Weather stats for - {} | {}".format(loc.upper(), date_time))
    print("-----------------------------------------------------------")
    print("Current temperature is: {:.2f} deg C".format(temp_city))
    print("Current weather dec: ",weather_desc)
    print("Current humidity: ",hmdt, '%')
    print("Current wind speed: ",wind_spd, 'kmph')