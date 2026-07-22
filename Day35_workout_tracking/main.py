import requests
from datetime import datetime
import os

#👇👇 FILL THEESE IN THE ENVIORNMENT👇👇
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETLY_AUTH = os.environ.get("SHEETLY_AUTh")
sheetly_url = os.environ.get("sheetly_url")
post_url = os.environ.get("post_url")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

user_input = input("Tell me what excersises you did: ")


#You can change these to whatever you want except the query
quary = {
  "query": user_input,
  "weight_kg": 100,                  
  "height_cm": 200,                 
  "age": 45,                        
  "gender": "male"                 
}

#Specific format of date and time
today = datetime.now()
today_date = today.date()
today_date_trimed = today_date.strftime("%d/%m/%Y")

today_time = today.time()
today_time_trimmed = today_time.strftime("%I:%M:%S %p")


response = requests.post(url=post_url, json=quary, headers=headers)
data = response.json()


for excercise in data["exercises"]:
    sheet_inputs = { 
        "workout":{ #Required by the sheet
            "date": today_date_trimed,
            "time": today_time_trimmed,
            "exercise": excercise["name"].title(),
            "duration": excercise["duration_min"],
            "calories": excercise["nf_calories"]

        }
    }

sheetly_headers = {
    "Authorization": f"Basic {SHEETLY_AUTH}"
}

response2 = requests.post(url=sheetly_url, json=sheet_inputs, headers=sheetly_headers)
print(response2.text)

 