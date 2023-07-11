import requests
import json
import sys

API_KEY = sys.argv[1]

API = "https://api.nzrb.fun"
HEADERS = {
    "Content-Type": "application/json",
    "X-API-KEY": f"{API_KEY}",
}
def get_scripts():
    scripts_url = f"{API}/scripts/"
    response = requests.get(scripts_url, headers=HEADERS)
    print(response)
    return response.json()

def print_script_names():
    scripts_data = get_scripts()
    if scripts_data:
        for script in scripts_data:
            script_name = script.get("name")
            script_id = script.get("id")
            print(f"List Of Scripts:  ID: {script_id}, =  {script_name}")
    else:
        raise ValueError("No scripts found.")

print_script_names()
