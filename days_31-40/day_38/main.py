import requests
import datetime as dt

from PRIVATE.variables import *

# variables imported
# APP_ID
# API_KEY
#

date = dt.datetime.now().strftime('%d-%m-%Y')
time = str(dt.datetime.now()).split(" ")[1].split(".")[0]

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

nutritionix_body = {
    "query": input("What did you do today? "),
    "gender": "male",
    "weight_kg": 77.1107029,
    "height_cm": 182.88,
    "age": 31
}

nutritionix_response = requests.post(
    url="https://trackapi.nutritionix.com/v2/natural/exercise", json=nutritionix_body, headers=nutritionix_headers)

nutritionix_data = nutritionix_response.json()["exercises"]
duration = nutritionix_data[0]["duration_min"]
exercise = nutritionix_data[0]["name"]
calories = nutritionix_data[0]["nf_calories"]


sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer ${SHEETY_TOKEN}"
}

sheety_body = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": str(exercise).title(),
        "duration": duration,
        "calories": calories
    }
}

sheety_response = requests.get(
    url="https://api.sheety.co/d51e2670e5420f10ef9236278431d7c0/workoutTracking/workouts")

sheety_post = requests.post(
    url="https://api.sheety.co/d51e2670e5420f10ef9236278431d7c0/workoutTracking/workouts", json=sheety_body, headers=sheety_headers)
