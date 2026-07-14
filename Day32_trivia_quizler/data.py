import requests


#Each time that we run the file, api called, and we get 16 boolean questions
parameters = {
    "amount" :16,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
# Just need the results
question_data = data["results"]



