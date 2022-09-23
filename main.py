import requests
from datetime import datetime

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = "XXX"
APP_KEY = "XXX"
GENDER = "male"
WEIGHT_KG = XXX
HEIGHT_CM = XXX
AGE = XXX

SHEETY_API = "XXX"
BEARER_TOKEN = {"Authorization": "Bearer XXX"}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

exercise_question = input("what did you do?")

parameters = {
    "query": exercise_question,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
#print(result)

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")
exercise = result["exercises"][0]["name"].title()
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(SHEETY_API, json=sheet_inputs, headers=BEARER_TOKEN)
    sheety_result = sheety_response.json()
    print(sheety_result)

