from pyrogram import Client
from credentials import api_id, api_hash
from functions import extract_features, extract_reactions
import logging
import json

# Настройки логгера
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w", encoding="utf-8")

# Канал для считывания информации
channel_username = '@befree_community'

app = Client("enotta", api_id, api_hash)
with app:
    messages = app.get_chat_history(channel_username, limit=20)
    for message in messages:
        print(app.get_discussion_message(channel_username, message.id))
        post = {"text": message.text, "tags": extract_features(message), "views": message.views, "date": str(message.date), "reactions":extract_reactions(message)}
        logging.info(msg=json.dumps(post, ensure_ascii=False))
