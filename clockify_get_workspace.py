import requests

# Your Clockify API key
api_key = 'NDJiOTEzODYtMWQ1Ni00MmNjLWJlY2MtMTY5NTVkNGFiODEw'

# Clockify API URL to get workspaces
url = "https://api.clockify.me/api/v1/workspaces"

# Define the headers with the API key
headers = {
    'X-Api-Key': api_key
}

# Send the request to the Clockify API
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    workspaces = response.json()
    for workspace in workspaces:
        print(f"Workspace Name: {workspace['name']}, Workspace ID: {workspace['id']}")
else:
    print(f"Error: {response.status_code}, {response.text}")
