import requests
from datetime import datetime, timedelta

# Your Clockify API key
api_key = 'NDJiOTEzODYtMWQ1Ni00MmNjLWJlY2MtMTY5NTVkNGFiODEw'

# Clockify workspace and user IDs
workspace_id = '66ddfc87370d964f37c670a7'
user_id = '66ddfc87370d964f37c670a6'

# Get the current date for today's time entries
today = datetime.now().date()
start_of_day = today.isoformat() + "T00:00:00.000Z"  # Start of today in ISO format
end_of_day = (today + timedelta(days=1)).isoformat() + "T00:00:00.000Z"  # End of today

# Clockify API URL to get time entries
url = f"https://api.clockify.me/api/v1/workspaces/{workspace_id}/user/{user_id}/time-entries"

# Define the headers with the API key
headers = {
    'X-Api-Key': api_key,
    'Content-Type': 'application/json'
}

# Define the query parameters (for today)
params = {
    'start': start_of_day,
    'end': end_of_day
}

# Send the request to the Clockify API
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    time_entries = response.json()

    # Print out item name, project name, and duration
    for entry in time_entries:
        project = entry['projectId']  # You may need to fetch project name separately
        item_name = entry.get('description', 'No Description')
        duration = entry.get('timeInterval', {}).get('duration', 'No Duration')

        print(f"Item: {item_name}, Project: {project}, Duration: {duration}")
else:
    print(f"Error: {response.status_code}, {response.text}")
