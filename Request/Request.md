# Request :
- In Python, the requests library is used to send HTTP requests like GET, POST, PUT, DELETE, etc., easily. It's great for interacting with web APIs.

## ✅ Installation :
```
pip install requests
```
## ✅ Basic Usage :
## 1. GET Request (fetching data) :
```
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)      # 200
print(response.json())           # JSON response as Python dict

```

## 2. POST Request (sending data) :
```
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "Hello",
    "body": "This is a test",
    "userId": 1
}

response = requests.post(url, json=data)
print(response.json())  # Returns the created object

```

## ✅ Other Common Methods :
### PUT (update data) :
```
requests.put(url, json={"title": "Updated Title"})
```

### DELETE (remove data) :
``` 
requests.delete("https://jsonplaceholder.typicode.com/posts/1")
```

## ✅ Handling Responses :
```
response = requests.get("https://httpbin.org/get")

# Status
print(response.status_code)

# Headers
print(response.headers)

# Text (raw content)
print(response.text)

# JSON (auto-parsed)
data = response.json()

```

## ✅ Add Headers / Params :
```
# Query parameters
params = {"search": "python"}
response = requests.get("https://api.example.com", params=params)

# Custom headers
headers = {"Authorization": "Bearer TOKEN"}
response = requests.get("https://api.example.com", headers=headers)

```