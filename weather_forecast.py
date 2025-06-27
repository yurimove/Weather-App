import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Replace with your API key
API_KEY = "bd5e378503939ddaee76f12ad7a97608"
CITY = "Delhi"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

dates = []
temperatures = []
humidity = []

for item in data["list"]:
    dt = datetime.datetime.fromtimestamp(item["dt"])
    temp = item["main"]["temp"]
    hum = item["main"]["humidity"]
    
    dates.append(dt)
    temperatures.append(temp)
    humidity.append(hum)

# Plot temperature
sns.set(style="darkgrid")
plt.figure(figsize=(12, 6))
plt.plot(dates, temperatures, label="Temperature (°C)", color='tomato')
plt.title(f"5-Day Temperature Forecast for {CITY}")
plt.xlabel("Date and Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("temperature_plot.png")
plt.show()

# Plot humidity
plt.figure(figsize=(12, 6))
plt.plot(dates, humidity, label="Humidity (%)", color='skyblue')
plt.title(f"5-Day Humidity Forecast for {CITY}")
plt.xlabel("Date and Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("humidity_plot.png")
plt.show()
