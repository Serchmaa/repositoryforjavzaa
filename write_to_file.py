import os
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import io

def write_to_file():
    creds = Credentials(
        None,
        refresh_token=os.getenv('REFRESH_TOKEN'),
        token_uri='https://oauth2.googleapis.com/token',
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET'),
    )
    filename = 'testfile.txt'
    drive_service = build('drive', 'v3', credentials=creds)
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
    write_to_file()
