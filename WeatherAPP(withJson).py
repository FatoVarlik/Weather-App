import requests
import json
import os

api_key = "API_KEY" #Add your API Key
target_url = f"https://api.openweathermap.org/data/2.5/weather?"

user = input("Enter city/state name: ")
url = target_url + "appid=" + api_key + "&q" + user

response = requests.get(url)
data = response.json()

if data["cod"] == 404:
    print("Wrong Location")
else:
    temp = data["main"]["temp"]
    feeling = data["main"]["feels_like"]
    pres = data["main"]["pressure"]
    humans = data["main"]["humidity"]
    desc = data["main"][0]["description"]

    tempC = temp - 273
    feelC = feeling - 273

    pres *= 0.0009869233

    print("Temperature: " + str(round(tempC,2)) + " °C")
    print("Feels Like: " + str(round(feelC,2)) + " °C")
    print("Pressure: " + str(round(pres,2)) + " atm")
    print("Humidity: " + str(humans) + " %")
    print("Description: " + str(desc))

    print(os.popen(f"curl wttr.in/{user}").read())