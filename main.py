from pyrogram import Client
from credentials import api_id, api_hash
from functions import extract_features
import logging
import json

# Настройки логгера
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w", encoding="utf-8")

# Канал для считывания информации
channel_username = '@rian_ru'

app = Client("enotta", api_id, api_hash)
with app:
    messages = app.get_chat_history(channel_username, limit=5)
    for message in messages:
        if message.text is None:
            logging.warning("Пост без текстового описания!")
        else:
            post = {"text": message.text, "tags": extract_features(message), "views": message.views}
            logging.info(msg=json.dumps(post, ensure_ascii=False))
