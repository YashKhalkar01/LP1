import tkinter as tk
from tkinter import ttk
# from PIL import Image, ImageTk

# Hardcoded weather data (sample)
weather_data = {
    "city": "New York",
    "country": "US",
    "temperature": 22,
    "humidity": 70,
    "pressure": 1013,
    "wind_speed": 5.5,
    "description": "Partly cloudy",
    "icon": "cloudy.png"  # Use any sample image for illustration
}

# Initialize main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x600")
root.configure(bg="#4a7ab7")

# Header Frame
header_frame = tk.Frame(root, bg="#4a7ab7", pady=10)
header_frame.pack(fill="x")

title_label = tk.Label(header_frame, text="Weather App", font=("Arial", 24, "bold"), fg="white", bg="#4a7ab7")
title_label.pack()

# City Information Frame
city_frame = tk.Frame(root, bg="#4a7ab7", pady=10)
city_frame.pack(fill="x")

city_label = tk.Label(city_frame, text=f"{weather_data['city']}, {weather_data['country']}",
                      font=("Arial", 18, "bold"), fg="white", bg="#4a7ab7")
city_label.pack()

# Icon and Weather Description Frame
icon_frame = tk.Frame(root, bg="#4a7ab7", pady=10)
icon_frame.pack(fill="x")


description_label = tk.Label(icon_frame, text=weather_data['description'].capitalize(),
                             font=("Arial", 14), fg="white", bg="#4a7ab7")
description_label.pack()

# Temperature Frame
temp_frame = tk.Frame(root, bg="#4a7ab7", pady=10)
temp_frame.pack(fill="x")

temp_label = tk.Label(temp_frame, text=f"{weather_data['temperature']}°C",
                      font=("Arial", 30, "bold"), fg="white", bg="#4a7ab7")
temp_label.pack()

# Additional Weather Info Frame
info_frame = tk.Frame(root, bg="#4a7ab7", pady=10)
info_frame.pack(fill="x", padx=20)

# Humidity
humidity_label = tk.Label(info_frame, text=f"Humidity: {weather_data['humidity']}%",
                          font=("Arial", 12), fg="white", bg="#4a7ab7")
humidity_label.grid(row=0, column=0, padx=10, pady=5)

# Pressure
pressure_label = tk.Label(info_frame, text=f"Pressure: {weather_data['pressure']} hPa",
                          font=("Arial", 12), fg="white", bg="#4a7ab7")
pressure_label.grid(row=1, column=0, padx=10, pady=5)

# Wind Speed
wind_label = tk.Label(info_frame, text=f"Wind Speed: {weather_data['wind_speed']} m/s",
                      font=("Arial", 12), fg="white", bg="#4a7ab7")
wind_label.grid(row=0, column=1, padx=10, pady=5)

# Add a divider line
divider = tk.Frame(root, bg="white", height=2)
divider.pack(fill="x", padx=20, pady=10)

# Footer Frame with Credits
footer_frame = tk.Frame(root, bg="#4a7ab7", pady=10)
footer_frame.pack(fill="x")

credit_label = tk.Label(footer_frame, text="Weather data is sourced from OPENAPI.",
                        font=("Arial", 10), fg="white", bg="#4a7ab7")
credit_label.pack()

# Run the Tkinter main loop
root.mainloop()
