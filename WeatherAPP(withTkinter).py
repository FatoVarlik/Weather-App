import requests
import tkinter as tk
from tkinter import messagebox

url = f"https://api.openweathermap.org/data/2.5/weather?"

#Window
root = tk.Tk()
root.title("Weather App")

#Labels and Entry
city_label = tk.Label(root, text="Where is this?: ")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

#Button
w_button = tk.Button(root, text="Show the weather")
w_button.pack()

#Weather Info
weather_label = tk.Label(root,text="")
weather_label.pack()

#Function for weather
def show_weather():
    city = city_entry.get()
    api_key = "YOUR_API_KEY" #Add your API Key here

    try:
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        weather_label.config(text=f"Temperature:{temperature}°C\nWeather:{weather}")
    except Exception as err:
        messagebox.showerror("Error","No Weather forecast found for the selected city.")
w_button.config(command=show_weather)

root.mainloop()