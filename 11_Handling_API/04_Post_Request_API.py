import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "Faizan API Test",
    "body": "This is generated using Python.",
    "userId": 1
}

response = requests.post(url, json=data)
print(response.json())
