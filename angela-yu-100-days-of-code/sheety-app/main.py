import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 168
AGE = 34

APP_ID = os.getenv("NUTRITIONIX_APP_ID")
API_KEY = os.getenv("NUTRITIONIX_APP_KEY")
BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

sheety_endpoint = os.getenv("SHEETY_ENDPOINT")

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    # Bearer Token Authentication
    bearer_headers = {"Authorization": BEARER_TOKEN}
    sheety_response = requests.post(
        sheety_endpoint, json=sheet_inputs, headers=bearer_headers
    )
    print(sheety_response.text)
