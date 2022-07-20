import requests
from datetime import datetime
import os

API_ID = os.environ["APP_ID"]
API_KEY = os.environ["APP_KEY"]
SHEET_KEY = os.environ["SHEET_KEY"]

nutrition_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_url = "https://api.sheety.co/c61d0b53b3cd45902d9612a931178d10/workoutTracking/workouts"


headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}


nutrition_data = {
    "query": input("Enter exercise: "),
    "gender": "male",
    "weight_kg": 73,
    "height_cm": 170.0,
    "age": 26
}

headers_sheet = {
    "Authorization": SHEET_KEY
}


time_now = datetime.now()
nature_response = requests.post(url=nutrition_url, json=nutrition_data, headers=headers)
exercises = nature_response.json()

for exercise in exercises['exercises']:
    sheet_param = {
        "workout":
            {
                "date": time_now.strftime("%d/%m/%Y"),
                "time": time_now.strftime("%X"),
                "exercise": exercise["name"].title(),
                "duration": exercise['duration_min'],
                "calories": exercise['nf_calories']
            }
    }

    requests.post(url=sheet_url, json=sheet_param, headers=headers_sheet)