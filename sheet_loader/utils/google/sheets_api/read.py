from __future__ import print_function

from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import re

from django.conf import settings


def get_data(spreadsheet_id, range_name, dimension='ROWS', res_type='dict'):
    """
    spreadsheet_id: string. Example: https://docs.google.com/spreadsheets/d/%spreadsheet_id%/ or %spreadsheet_id%
    range_name: string. Example: 'sheet1!A:D'
    dimension:
    """
    google_sheet_url_pattern = '/spreadsheets/d/([a-zA-Z0-9-_]+)'
    google_sheet_id_pattern = '([a-zA-Z0-9-_]+)'
    a = re.search(google_sheet_url_pattern, spreadsheet_id)
    b = re.search(google_sheet_id_pattern, spreadsheet_id)
    if a:
        spreadsheet_id = a.group(1)
    elif b:
        spreadsheet_id = b.group(1)
    else:
        raise ValueError('wrong spreadsheet_id')

    if res_type not in ('dict', 'list'):
        raise ValueError('Wrong res_type value')

    creds = service_account.Credentials.from_service_account_file(
        settings.GOOGLE_SHEET_CREDS, scopes=settings.GOOGLE_SHEET_SCOPES)
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                    range=range_name,
                                    majorDimension=dimension).execute()
        data_set = result.get('values', [])

        result_set = []
        if not data_set:
            print('No data found.')
        elif res_type == 'dict':
            header = data_set[0]
            values = data_set[1:]
            for row in values:
                if len(header) > len(row):
                    for x in range(len(header) - len(row)):
                        row.append('')
                result_set.append(dict(zip(header, row)))
        elif res_type == 'list':
            result_set = data_set
        return result_set
    except HttpError as err:
        print(err)
