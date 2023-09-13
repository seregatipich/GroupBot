import os

import gspread
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials


def save_data(user_data: dict) -> None:
    """
    Saves user data into the first sheet of a Google spreadsheet named 'generoses_bot_spreadsheet'.
    The spreadsheet should be accessible for the account associated with the credentials provided in 'gs_credentials.json' file.

    User data should be represented as a dictionary with mandatory keys: 'fullname', 'phone', 'email', 'social_media', 
    'profession', and 'help'. The values of these keys will be added to a new row in the table in the specified order.

    Parameters:
    user_data (dict): A dictionary containing user information. It should include the following keys: 
                      'fullname', 'phone', 'email', 'social_media', 'profession', 'help'.

    Returns:
    None
    """
    scope = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'gs_credentials.json', scope
    )
    client = gspread.authorize(credentials)

    load_dotenv()
    sheet = client.open(os.getenv('GOOGLE_SPREADSHEET_NAME')).sheet1
    row = [
        user_data['fullname'],
        user_data['phone'],
        user_data['email'],
        user_data['social_media'],
        user_data['profession'],
        user_data['help']
    ]
    sheet.append_row(row)
