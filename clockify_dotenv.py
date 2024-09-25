import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv(dotenv_path=".env")  # Specify the path to your .env file if necessary

# Access the environment variables
clockify_token = os.getenv('CLOCKIFY_TOKEN')
clockify_workspace = os.getenv('CLOCKIFY_WORKSPACE')
clockify_id = os.getenv('CLOCKIFY_ID')
clockify_name = os.getenv('CLOCKIFY_NAME')

# Print the loaded environment variables (for testing purposes)
print(f"CLOCKIFY_TOKEN: {clockify_token}")
print(f"CLOCKIFY_WORKSPACE: {clockify_workspace}")
print(f"CLOCKIFY_ID: {clockify_id}")
print(f"CLOCKIFY_NAME: {clockify_name}")

