import os
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import io
from pathlib import Path


def set_env_variables(file_path='env.txt'):
    # We only need to configure environment variable when we running code on the local
    # If file doesn't exist, it means it is running on the github.
    # So in this case, we don't need to configure environment variable.
    # It has already configured in yml file.
    if Path(file_path).is_file():
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                key, value = line.split('=', 1)
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                os.environ[key] = value

def get_credentials():
    creds = Credentials(
        None,
        refresh_token=os.getenv('REFRESH_TOKEN'),
        token_uri='https://oauth2.googleapis.com/token',
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET'),
    )
    return creds

# Function to get all TEXT file IDs in the given folder
def get_file_ids_in_folder(drive_service, folder_id):
    query = f"'{folder_id}' in parents and mimeType='text/plain'"
    results = drive_service.files().list(q=query).execute()
    items = results.get('files', [])
    if not items:
        print(f'No text files found in folder with ID: {folder_id}')
        return []
    return [(item['id'], item['name']) for item in items]

# Function to read the file content
def read_file(file_id):
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
    fh.seek(0)
    return fh.read().decode('utf-8')

def write_to_file(drive_service):
    filename = 'testfile.txt'
    file_metadata = {'name': filename, 'mimeType': 'text/plain'}
    
    # Check if the file exists
    results = drive_service.files().list(q='name="testfile.txt" and mimeType="text/plain"', spaces='drive', fields='files(id, name)').execute()
    items = results.get('files', [])

    content = f'Text written at {time.ctime()}\n'
    if not items:
        print('File not exist, creating the file ...')
        # Create a new file if it doesn't exist
        with open(filename, 'w') as f:
            f.write(content)
        media = MediaFileUpload(filename, mimetype='text/plain')
        drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    else:
        print('Updating the file ...')
        # Append content to the existing file
        file_id = items[0]['id']
        
        # Download the existing content
        request = drive_service.files().get_media(fileId=file_id)
        file_data = io.BytesIO()
        downloader = MediaIoBaseDownload(file_data, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
        
        # Append new content to the existing content
        existing_content = file_data.getvalue().decode('utf-8')
        new_content = existing_content + content
        with open(filename, 'w') as f:
            f.write(new_content)
        
        media = MediaFileUpload(filename, mimetype='text/plain')
        drive_service.files().update(fileId=file_id, media_body=media).execute()

    print(f'Text written at {time.ctime()} to {filename}')

if __name__ == "__main__":
    # Set the environment variables
    set_env_variables()
    creds = get_credentials()
    drive_service = build('drive', 'v3', credentials=creds)

    file_ids = get_file_ids_in_folder(drive_service, "1rQRegMfYi0GFhMa6J6XI0YkG5TNgP6b3")
    for file_id, file_name in file_ids:
        print(f'Reading file: {file_name}')
        file_content = read_file(file_id)
        print(file_content)

    write_to_file()
