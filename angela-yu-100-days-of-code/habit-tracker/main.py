import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()
pixela_token = os.getenv("PIXELA_TOKEN")
pixela_username = os.getenv("PIXELA_USERNAME")
graph_id = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": pixela_token,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Creates a new user account on Pixela
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Creates a new graph on Pixela
graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"

graph_config = {
    "id": graph_id,
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai",
}

# More secure way to pass the token, instead of passing it in the url
headers = {
    "X-USER-TOKEN": pixela_token,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

record_endpoint = f"{graph_endpoint}/{graph_id}"

today = datetime.now()

record_config = {"date": today.strftime("%Y%m%d"), "quantity": "120"}

response = requests.post(url=record_endpoint, json=record_config, headers=headers)
print(response.text)
