import os
import json

from dotenv import load_dotenv

from chatgpt_text_from_image import handle as handle_chatgpt
from get_file_link import handle as handle_get_file_link

load_dotenv()
CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")
HTTPS_PROXY = os.getenv("HTTPS_PROXY")
BOT_TOKEN = os.getenv("BOT_TOKEN")


def test_local_env():
    assert CHATGPT_API_KEY is not None
    assert HTTPS_PROXY is not None
    assert BOT_TOKEN is not None

def test_chatgpt_text_from_image():
    test_data = {
        "CHATGPT_API_KEY": CHATGPT_API_KEY,
        "HTTPS_PROXY": HTTPS_PROXY,
        "image_url": "https://api.telegram.org/file/bot7835218076:AAG2azBuM3b-0zneIa6zQ2P7NnOZ4dT6tMs/photos/file_29.jpg"
    }
    data_json = json.dumps(test_data)

    result = handle_chatgpt(data_json)
    assert isinstance(result, str)


def test_get_file_link():
    test_data = {
        "BOT_TOKEN": BOT_TOKEN,
        "HTTPS_PROXY": HTTPS_PROXY,
        "file_id": "AgACAgIAAxkBAAIClmdsNfgkFn9R5kYyOt-lBPszX_ZYAAKK6jEbajBoS6KtyYI--eFYAQADAgADeAADNgQ"
    }
    data_json = json.dumps(test_data)

    result = handle_get_file_link(data_json)
    assert result.startswith('https://')
