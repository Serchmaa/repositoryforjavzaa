import os
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
import io

def write_to_file():
    creds = Credentials(
        None,
        refresh_token=os.getenv('REFRESH_TOKEN'),
        token_uri='https://oauth2.googleapis.com/token',
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET'),
    )
    drive_service = build('drive', 'v3', credentials=creds)
    
    file_metadata = {'name': 'testfile.txt', 'mimeType': 'text/plain'}
    content = f'Text written at {time.ctime()}\n'
    
    # Check if the file exists
    results = drive_service.files().list(q='name="testfile.txt" and mimeType="text/plain"', spaces='drive', fields='files(id, name)').execute()
    items = results.get('files', [])

    if not items:
        # Create a new file if it doesn't exist
        media = MediaIoBaseUpload(io.BytesIO(content.encode('utf-8')), mimetype='text/plain')
        drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    else:
        # Get the file ID
        file_id = items[0]['id']
        
        # Download the existing content
        request = drive_service.files().get_media(fileId=file_id)
        existing_content = request.execute()
        
        # Append new content to the existing content
        new_content = existing_content.decode('utf-8') + content
        media = MediaIoBaseUpload(io.BytesIO(new_content.encode('utf-8')), mimetype='text/plain')
        
        # Update the file with the new content
        drive_service.files().update(fileId=file_id, media_body=media, fields='id').execute()

    print(f'Text written at {time.ctime()} to testfile.txt')

if __name__ == "__main__":
    write_to_file()
