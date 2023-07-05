import os
from pathlib import Path

from googleapiclient import discovery, errors
from google_auth_oauthlib import flow


current_path = Path(__file__).parent


scopes = "https://www.googleapis.com/auth/userinfo.profile"

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

api_service_name = 'youtube'
api_version = 'v3'
client_secrets_file = current_path / 'secret.json'

flow_ = flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
credentials = flow_.run_local_server()
youtube = discovery.build(api_service_name, api_version, credentials=credentials)

request = youtube.search().list(
    part='snippet',
    maxResults=50,
    pageToken='CDIQAA',
    q='раздельний збор',
    type='channel'
)

response = request.execute()

print(response)