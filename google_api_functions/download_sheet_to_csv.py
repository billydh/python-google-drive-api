import csv


def download_sheet_to_csv(sheets_instance, spreadsheet_id, sheet_name):
    result = sheets_instance.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=sheet_name).execute()
    output_file = f'{sheet_name}.csv'

    with open(output_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(result.get('values'))

    f.close()

    print(f'Successfully downloaded {sheet_name}.csv')
