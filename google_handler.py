import gspread
from oauth2client.service_account import ServiceAccountCredentials


def save_data(user_data: dict) -> None:
    scope = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'gs_credentials.json', scope
    )

    client = gspread.authorize(credentials)

    sheet = client.open('generoses_bot_spreadsheet').sheet1
    row = [
        user_data['fullname'],
        user_data['phone'],
        user_data['email'],
        user_data['social_media'],
        user_data['profession'],
        user_data['help']
    ]
    sheet.append_row(row)
