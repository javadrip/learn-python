import os

import requests
from dotenv import load_dotenv

load_dotenv()
pixela_token = os.getenv("PIXELA_TOKEN")
pixela_username = os.getenv("PIXELA_USERNAME")

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
