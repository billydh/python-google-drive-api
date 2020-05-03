from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools


def get_api_services():
    # define credentials and client secret file paths
    credentials_file_path = './credentials/credentials.json'
    clientsecret_file_path = './credentials/client_secret.json'

    # define scope
    SCOPE = 'https://www.googleapis.com/auth/drive'

    # define store
    store = file.Storage(credentials_file_path)
    credentials = store.get()

    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(clientsecret_file_path, SCOPE)
        credentials = tools.run_flow(flow, store)

    # define API service
    http = credentials.authorize(Http())
    drive = discovery.build('drive', 'v3', http=http)
    sheets = discovery.build('sheets', 'v4', credentials=credentials)

    return drive, sheets
