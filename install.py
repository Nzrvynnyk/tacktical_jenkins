import requests
import json
import sys

USER = sys.argv[1]
API_KEY = sys.argv[2]
SOFTNAME = sys.argv[3]


API = "https://api.nzrbhome.tech/"
HEADERS = {
    "Content-Type": "application/json",
    "X-API-KEY": f"{API_KEY}",
}

def run_cmd(agent_id, cmd):
    endpoint = f"{API}/agents/{agent_id}/cmd/"
    payload = {
        "shell": "cmd",
        "cmd": cmd,
        "timeout": 90,
        "custom_shell": None,
        "run_as_user": False
    }
    headers = {'Content-Type': 'application/json', "X-API-KEY": f"{API_KEY}"}
    response = requests.post(endpoint, headers=headers, json=payload)
    if response.status_code == 200:
        print(f"CMD command '{cmd}' executed successfully on agent '{agent_id}'.")
    else:
        print(response)
        print(f"Failed to execute CMD command '{cmd}' on agent '{agent_id}'.")

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

def run_cmd_names():
    agent_ids = get_agents()
    cmd = f"choco install {SOFTNAME} -y" 
    print(cmd)
    for agent_id in agent_ids:
        run_cmd(agent_id, cmd)
run_cmd_names()