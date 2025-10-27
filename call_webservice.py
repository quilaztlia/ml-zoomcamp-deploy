import requests

url = 'http://127.0.0.1:9697/predict'

client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

result = requests.post(url, json=client).json()

print(result)