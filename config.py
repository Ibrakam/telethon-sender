import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
PHONE = os.getenv('PHONE')
RECIPIENT_USERNAME = os.getenv('RECIPIENT_USERNAME')
MESSAGE_TEMPLATE = os.getenv('MESSAGE_TEMPLATE', 'я люблю тебя моя {}')
