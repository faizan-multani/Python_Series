# 🌍 Real Use Case: Get Weather by City
```
city = "Delhi"
api_key = "your_api_key"
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

res = requests.get(url)
weather = res.json()

print("Temperature:", weather['current']['temp_c'], "°C")

```

# How to handle API and Error :
## Fetch data using get request :
```
import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch user data")
    

def main():
    try:
        username, country = fectch_random_user_freeapi()
        print(f"Username: {username} \nCountry: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()

```    

## Send data using post request :
```
import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "Faizan API Test",
    "body": "This is generated using Python.",
    "userId": 1
}

response = requests.post(url, json=data)
print(response.json())

```