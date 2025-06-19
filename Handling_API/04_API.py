import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        location = user_data["location"]["state"]
        user_name = user_data["name"]["title"]
        return username, country,  user_name, location
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        username, country ,user_name, location = fetch_random_user_freeapi()
        print(f"Username: {username} \nCountry: {country} \nusername : {user_name} \nlocation : {location}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
