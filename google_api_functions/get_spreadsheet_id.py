from googleapiclient import errors


def get_spreadsheet_id(api_service, spreadsheet_name):
    results = []
    page_token = None

    while True:
        try:
            param = {'q': 'mimeType="application/vnd.google-apps.spreadsheet"'}

            if page_token:
                param['pageToken'] = page_token

            files = api_service.files().list(**param).execute()
            results.extend(files.get('files'))

            # Google Drive API shows our files in multiple pages when the number of files exceed 100
            page_token = files.get('nextPageToken')

            if not page_token:
                break

        except errors.HttpError as error:
            print(f'An error has occurred: {error}')
            break

    spreadsheet_id = [result.get('id') for result in results if result.get('name') == spreadsheet_name][0]

    return spreadsheet_id
