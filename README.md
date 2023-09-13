# GroupBot - Telegram Bot for Group Membership Application

#### This project is a Python script for a Telegram bot that facilitates group membership application by collecting several personal details from the users. It uses the `aiogram` framework to interact with Telegram's Bot API and stores user responses in states using FSM (Finite State Machine) which helps in organizing a sequential conversation with the user.

## Dependencies

- Python 3.10
- aiogram
- python-dotenv
- gspread
- oauth2client

## Installation:

1. Clone the repo to your local machine:
```
git clone git@github.com:seregatipich/GroupBot.git
```
2. Create virtual environment:
```
python3 -m venv venv
```
3. Activate virtual environment:
```
source venv/bin/activate
```
4. Install the dependencies:
```
pip install -r requirements.txt
```

## Environment Variables
#### You need to set up a few environment variables to get the bot working. Create a '.env' file in the project directory and add the following variables:

```
TELEGRAM_TOKEN=your_telegram_bot_token_here
TELEGRAM_GROUP_LINK=your_telegram_group_link_here
GOOGLE_SPREADSHEET_NAME=your_google_spreadsheet_name_here
```

## Setting Up Google Sheets API
#### To save data to Google Sheets, you'll need to set up the Google Sheets API:
1. Go to the Google Developers Console.
2. Create a new project and enable the Sheets API for it.
3. Create credentials for a service account.
4. Download the JSON credentials file and rename it to gs_credentials.json.
5. Share your spreadsheet with the email address found in the client_email field in the gs_credentials.json file.

## Usage
1. Set up the environment variables as mentioned above.
2. Run the script using the following command:
```
python3 main.py
```