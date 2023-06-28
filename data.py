import requests

parameters = {
    "amount": 49,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php?", params=parameters)
question_data = response.json()["results"]
print(question_data)