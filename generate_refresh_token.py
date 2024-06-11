# import os
#
# os.setenv()

import os
from google_auth_oauthlib.flow import InstalledAppFlow

# Path to the credentials file
creds_path = 'credentials.json'

# Scopes required for accessing Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive']

# Create the flow using the client secrets file from the Google API
flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)

# Run the local server to authorize the app
creds = flow.run_local_server(port=0)

# Print the refresh token
print('Refresh Token:', creds.refresh_token)
