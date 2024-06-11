import os
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
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

    content = f'Text written at {time.ctime()}\n'
    # Check if the file exists
    results = drive_service.files().list(q='name="testfile.txt" and mimeType="text/plain"', spaces='drive', fields='files(id, name)').execute()
    items = results.get('files', [])

    if not items:
        # Create a new file if it doesn't exist
        file = drive_service.files().create(body=file_metadata, media_body=content, fields='id').execute()
    else:
        # Get the file ID
        file_id = items[0]['id']
        drive_service.files().update(fileId=file_id, media_body=content, fields='id').execute()

    print(f'Text written at {time.ctime()} to {filename}')

if __name__ == "__main__":
    write_to_file()
