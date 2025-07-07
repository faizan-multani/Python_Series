import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = '934c370c0f7d0a09d9a67e669de00ffb'

def get_weather():
    city_name = city_entry.get()
    if not city_name:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            messagebox.showerror("Error", data.get("message", "Unknown error"))
            return

        location = data["name"]
        country = data["sys"]["country"]
        temp_c = data["main"]["temp"]
        condition = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]
        wind_kph = data["wind"]["speed"] * 3.6  # Convert m/s to km/h

        weather_info.set(
            f"Location: {location}, {country}\n"
            f"Temperature: {temp_c}°C\n"
            f"Condition: {condition}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_kph:.1f} kph"
        )

    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve weather data.\n{str(e)}")

# GUI Setup
root = tk.Tk()
root.title("Weather Forecast")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12)).pack(pady=10)

weather_info = tk.StringVar()
tk.Label(root, textvariable=weather_info, font=("Arial", 12), justify="left").pack(pady=10)

root.mainloop()
