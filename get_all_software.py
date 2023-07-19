import requests
import json
import sys
import csv
import pandas as pd

API_KEY = sys.argv[1]

API = "https://api.nzrb.fun"
HEADERS = {
    "Content-Type": "application/json",
    "X-API-KEY": f"{API_KEY}",
}

def get_software(agent_ids):
    software = requests.get(f"{API}/software/{agent_ids}", headers=HEADERS)
    test = software.json()
    #print(test)
    return software.json()


# def print_software():
#     agent_ids = get_agents()
#     agent_usernames = get_agent_usernames()
#     software_data = get_software(agent_ids)


def print_software():
    agent_ids = get_agents()
    agent_usernames = get_agent_usernames()
    software_data = get_software(agent_ids)

    if software_data:
        data = {}  # Создаем пустой словарь для данных

        for agent_id, username in zip(agent_ids, agent_usernames):
            software_data = get_software(agent_id)
            software_list = software_data.get("software", [])
            software_names = '\n'.join([f'"{software.get("name")}"' for software in software_list])
            data[username] = software_names  # Добавляем имя пользователя и список программ в словарь

        # Создаем DataFrame из словаря
        df = pd.DataFrame(data.items(), columns=['User Name', 'Software'])
        df.to_csv('software_list.csv', index=False)

        print(df)  # Опционально, выводим DataFrame на консоль


    # if software_data:
    #     with open('software_list.csv', mode='w', newline='') as file:
    #         writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    #         # Write the header row with User Name as the first column
    #         header_row = ['User Name']
    #         writer.writerow(header_row)

    #         for agent_id, username in zip(agent_ids, agent_usernames):
    #             software_data = get_software(agent_id)
    #             software_list = software_data.get("software", [])
    #             software_names = '\n'.join([f'"{software.get("name")}"' for software in software_list])

    #             # Create a row for each user, with the user name in the first column
    #             user_row = [username]
    #             writer.writerow(user_row)

    #             # Write the software list under the user name in the same row
    #             software_row = [software_names]
    #             writer.writerow(software_row)
    #             print(f"User: {username}, Software: {software_names}")


def get_agents():
    agents = requests.get(f"{API}/agents/", headers=HEADERS)
    agent_ids = []
    for agent in agents.json():
        agent_ids.append(agent["agent_id"])
    if not agent_ids:
        raise ValueError("User does not exist.")
    return agent_ids

def get_agent_usernames():
    agents = requests.get(f"{API}/agents/", headers=HEADERS)
    agent_usernames = []
    for agent in agents.json():
        agent_usernames.append(agent["logged_username"])
    return agent_usernames


print_software() 
