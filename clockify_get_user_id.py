
import requests

# Your Clockify API key
api_key = 'NDJiOTEzODYtMWQ1Ni00MmNjLWJlY2MtMTY5NTVkNGFiODEw'

# Clockify API URL to get user info
url = "https://api.clockify.me/api/v1/user"

# Define the headers with the API key
headers = {
    'X-Api-Key': api_key
}

# Send the request to the Clockify API
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    user_info = response.json()
    print(f"User ID: {user_info['id']}, Name: {user_info['name']}")
else:
    print(f"Error: {response.status_code}, {response.text}")


