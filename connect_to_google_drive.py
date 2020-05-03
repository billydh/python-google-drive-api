from apiclient import discovery, errors
from httplib2 import Http
from oauth2client import client, file, tools

# define variables
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


# define a function to retrieve all files
def retrieve_all_files(api_service, filename_to_search):
    results = []
    page_token = None

    while True:
        try:
            param = {}

            if page_token:
                param['pageToken'] = page_token

            files = api_service.files().list(**param).execute()
            # append the files from the current result page to our list
            results.extend(files.get('files'))
            # Google Drive API shows our files in multiple pages when the number of files exceed 100
            page_token = files.get('nextPageToken')

            if not page_token:
                break

        except errors.HttpError as error:
            print(f'An error has occurred: {error}')
            break
    # output the file metadata to console
    for file in results:
        if file.get('name') == filename_to_search:
            print(file)
            break

    return results, file


# call the function
filename_to_search = 'Christmas Plan'
all_files, search_file = retrieve_all_files(drive, filename_to_search)
