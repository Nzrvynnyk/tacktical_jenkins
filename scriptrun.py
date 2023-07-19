import requests
import json
import sys
import time

USER = sys.argv[1]
API_KEY = sys.argv[2]
SCRIPT = sys.argv[3]
SOFTNAME = sys.argv[4]
if len(sys.argv) >= 6:
    ARGS1 = sys.argv[4]
    ARGS2 = sys.argv[5]
else:
    ARGS1 = None
    ARGS2 = None
if ARGS1 is not None and ARGS2 is not None:
    args = [f"{ARGS1} {ARGS2}"]
else:
    args = []

API = "https://api.nzrb.fun"
HEADERS = {
    "Content-Type": "application/json",
    "X-API-KEY": f"{API_KEY}",
}


def run_script(agent_id, payload):
    endpoint = f"{API}/agents/{agent_id}/runscript/"
    headers = {'Content-Type': 'application/json', "X-API-KEY": f"{API_KEY}"}
    response = requests.post(endpoint, headers=headers, json=payload)
    print(endpoint)
    if response.status_code == 200:
        print(response)
        print(f"Script executed successfully on agent '{agent_id}' without a specified user.")
    else:
        print(response)
        print(f"Failed to execute script on agent '{agent_id}'.")

def get_agents():
    agents = requests.get(f"{API}/agents/", headers=HEADERS)
    agent_ids = []
    for agent in agents.json():
        logged_username = agent.get("logged_username")
        if logged_username == USER:
            agent_ids.append(agent["agent_id"])

    if not agent_ids:
        raise ValueError("User does not exist.")

    return agent_ids

def run_script_names():
    agent_ids = get_agents()
    payload = {
        "shell": "script.shell",
        "output": "note",
        "email": [],
        "emailMode": "default",
        "custom_field": None,
        "save_all_output": True,
        "script": SCRIPT,
        "args": args,
        "shell": "script.shell",
        "env_vars": [],
        "run_as_user": False,
        "timeout": 90
        
    }
    for agent_id in agent_ids:
        run_script(agent_id, payload)


def get_software(agent_id):
    software = requests.get(f"{API}/software/{agent_id}", headers=HEADERS)
    return software.json()

def print_software_names():
    agent_ids = get_agents()
    software_found = False  # Flag variable to track if software "vim" is found
    for agent_id in agent_ids:
        software_data = get_software(agent_id)
        software_list = software_data.get("software", [])
        for software in software_list:
            software_name = software.get("name")
            if software_name == SOFTNAME :
                software_found = True
                break
        if software_found:
            break
    
    if software_found:
        print("Yes")
    if not software_found:
            raise ValueError("Software does not exist.") 
def get_agent_notes(agent_id):
    notes_url = f"{API}/agents/{agent_id}/notes/"
    response = requests.get(notes_url, headers=HEADERS)
    return response.json()

def print_agent_notes_names():
    agent_ids = get_agents()
    last_note = None  # Variable to store the last note
    for agent_id in agent_ids:
        notes_data = get_agent_notes(agent_id)
        if notes_data:
            last_note = notes_data[-1].get("note")  # Retrieve the last note from the list
            if last_note:
                print("============================================NOTES===========================================")
                print(last_note)
            if not last_note:
                raise ValueError("No notes found for the agent(s).")            

run_script_names()
print_agent_notes_names()

time.sleep(2)

