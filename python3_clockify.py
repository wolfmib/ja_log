import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta




# Tool =========
import os
from datetime import datetime

# Function to write time entry logs to file
def write_to_clockify_log(log_file_path, item_name, project_name, duration):
    # Ensure the log directory exists
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    
    # Open the log file in append mode and write the log entry
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Item: {item_name}, Project: {project_name}, Duration: {duration}\n")
    
    print(f"Log entry added: {item_name}, {project_name}, {duration}")













#============================ main =============
# Load environment variables from .env file
load_dotenv()

# Clockify API token and workspace ID from the .env file
api_key = os.getenv('CLOCKIFY_TOKEN')
workspace_id = os.getenv('CLOCKIFY_WORKSPACE')
user_id = os.getenv('CLOCKIFY_ID')

# Clockify API headers
headers = {
    'X-Api-Key': api_key,
    'Content-Type': 'application/json'
}

# Function to get all projects in the workspace
def get_all_projects():
    url = f"https://api.clockify.me/api/v1/workspaces/{workspace_id}/projects"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        projects = response.json()
        project_mapping = {project['id']: project['name'] for project in projects}
        return project_mapping
    else:
        print(f"Error fetching projects: {response.status_code} - {response.text}")
        return {}

# Function to get time entries for a specific day (e.g., 3 days ago)
def get_time_entries(start_date, end_date):
    url = f"https://api.clockify.me/api/v1/workspaces/{workspace_id}/user/{user_id}/time-entries"
    params = {
        'start': start_date,
        'end': end_date
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching time entries: {response.status_code} - {response.text}")
        return []

# Get the project mapping (project ID to project name)
project_mapping = get_all_projects()

# Get the date for 3 days ago
three_days_ago = datetime.now() - timedelta(days=3)
start_of_day = three_days_ago.replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + "Z"
end_of_day = three_days_ago.replace(hour=23, minute=59, second=59, microsecond=999999).isoformat() + "Z"

# Fetch time entries from 3 days ago
time_entries = get_time_entries(start_of_day, end_of_day)

# Print each time entry with the project name and duration
for entry in time_entries:
    project_id = entry.get('projectId')
    project_name = project_mapping.get(project_id, 'Unknown Project')
    item_name = entry.get('description', 'No Description')
    duration = entry.get('timeInterval', {}).get('duration', 'No Duration')

    print(f"Item: {item_name}, Project: {project_name}, Duration: {duration}")

    # Write la
    write_to_clockify_log("/Users/johnny_hung/Documents/ja_interview_entretien/ja_git/ja_log/clockify_log.txt",
        item_name,
        project_name,
        duration)
