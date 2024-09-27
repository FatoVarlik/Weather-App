import requests

api_key = "Your API Key" #Replace with your real API Key

user_city = input("Enter City/State Name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    print(f"Temperature: {temperature} °C")
    print(f"Description: {weather}")
else:
    print("Error! Weather data could not be retrieved!")