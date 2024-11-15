import requests
import shutil
import os
from datetime import datetime


if os.path.exists('gideon_tettehfio'):
    try:
        shutil.rmtree('gideon_tettehfio')
        print(f"Directory '{'gideon_tettehfio'}' has been removed successfully.")

    except Exception as e:
        print(f"Error: {e}")

download_folder = 'gideon_tettehfio'

if not os.path.exists(download_folder):
    os.makedirs(download_folder)
    print(f"Directory: {download_folder} created.")

local_file_path = os.path.join(download_folder, "gideon_tettehfio.txt")
url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"
response = requests.get(url)

if response.status_code == 200:
    print(f'File successfully downloaded.')
    with open(local_file_path, "wb") as file:
        file.write(response.content)
        print(f'File saved successfully.')
else:
    print(f'Failed to download file. Status code: {response.status_code}')

user_input = input('Describe what you have learned so far in a sentence: ')
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

with open(local_file_path, 'w') as file:
    file.write(user_input + '\n')
    file.write(f"Last modified on: {current_time}")
    print("file successfully modified.")
