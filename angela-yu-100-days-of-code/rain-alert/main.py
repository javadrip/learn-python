import os

import requests
from dotenv import load_dotenv

load_dotenv()
endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("OWM_API_KEY")

parameters = {
    "lat": 1.290270,
    "lon": 103.851959,
    "appid": api_key,
    # "exclude": "current,minutely,daily",
}

response = requests.get(endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:4]

print(weather_slice)

will_rain = False

for three_hour_data in weather_slice:
    condition_code = three_hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain == True:
    print("Bring an umbrella.")
