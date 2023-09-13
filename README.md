# GroupBot - Telegram Bot for Group Membership Application

#### This project is a Python script for a Telegram bot that facilitates group membership application by collecting several personal details from the users. It uses the `aiogram` library to interact with Telegram's Bot API and stores user responses in states using FSM (Finite State Machine) which helps in organizing a sequential conversation with the user.

## Dependencies

- Python 3.10
- aiogram
- python-dotenv
- gspread
- oauth2client

## Usage:

- Clone the repo to your local machine:
```
git clone git@github.com:seregatipich/GroupBot.git
```
- Create virtual environment:
```
python3 -m venv venv
```
- Activate virtual environment:
```
source venv/bin/activate
```
- Install the dependencies:
```
pip install -r requirements.txt
```