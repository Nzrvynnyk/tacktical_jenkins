import requests
import json
import sys

API_KEY = sys.argv[1]

API = "https://api.nzrb.fun"
HEADERS = {
    "Content-Type": "application/json",
    "X-API-KEY": f"{API_KEY}",
}

def get_users():
    users_url = f"{API}/agents/"
    response = requests.get(users_url, headers=HEADERS)
    print(response)
    return response.json()

def print_users_name():
    users_data = get_users()
    if users_data: 
        for users in users_data:
            users_name = users.get("logged_username")
            users_host = users.get("hostname")
            print(f"User: {users_name}, Hostname: {users_host}")
    else: 
        raise ValueError("No found")

print_users_name()
