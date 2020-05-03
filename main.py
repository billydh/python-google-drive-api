import argparse

from google_api_functions.download_sheet_to_csv import download_sheet_to_csv
from google_api_functions.get_api_services import get_api_services
from google_api_functions.get_spreadsheet_id import get_spreadsheet_id


def parse_args():
    parser = argparse.ArgumentParser(description="Function to download a specific sheet from a Google Spreadsheet")

    parser.add_argument("--spreadsheet-name", required=True, help="The name of the Google Spreadsheet")
    parser.add_argument("--sheet-name", required=True, help="The name of the sheet in spreadsheet to download as csv")

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    spreadsheet_name = args.spreadsheet_name
    sheet_name = args.sheet_name

    drive, sheets = get_api_services()

    spreadsheet_id = get_spreadsheet_id(drive, spreadsheet_name)
    download_sheet_to_csv(sheets, spreadsheet_id, sheet_name)
