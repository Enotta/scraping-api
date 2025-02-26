import pyrogram
import asyncio
from pyrogram import Client
from credentials import api_id, api_hash
from functions import extract_features, extract_reactions
import logging
import json
import time

# Настройки логгера
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w", encoding="utf-8")

# Канал для считывания информации
channel_username = '@ilya_commander'

# Ключевые слова для блока
PARTICIPATE_KEYWORDS = ["участвовать", "participate", "розыгрыш", "giveaway"]

app = Client("enotta", api_id, api_hash)
async def main():
    async with app:
        async for message in app.get_chat_history(channel_username, limit=50):
            try:
                # Дроп постов с переходом
                if message.reply_markup:
                    buttons = False
                    for row in message.reply_markup.inline_keyboard:
                        if len(row) > 0:
                            buttons = True
                            break

                    if buttons:
                        logging.warning("Пост с рекламой!")
                        continue
                
                # Выбор текста в зависимости от медиа
                text = ""
                if message.media is not None:
                    text = message.caption
                else:
                    text = message.text

                # Подсчет комментариев
                comments = None
                try:
                    if message.media_group_id is None:
                        comments = await app.get_discussion_replies_count(channel_username, message.id)
                    else:
                        group = await message.get_media_group()
                        if message.id == group[0].id:
                            comments = await app.get_discussion_replies_count(channel_username, message.id)
                        else:
                            logging.warning("Часть медиа группы!")
                            continue
                except pyrogram.errors.exceptions.bad_request_400.MsgIdInvalid as e:
                    logging.warning("Пост без возможности подсчёта комментариев!")

                post = {"text": text, "tags": extract_features(text), "views": message.views, "date": str(message.date), "reactions": extract_reactions(message), "comments": comments}
                logging.info(msg=json.dumps(post, ensure_ascii=False))
            except pyrogram.errors.exceptions.flood_420.FloodWait as e:
                # Сон на требуемой количество секунд!
                await asyncio.sleep(e.value)

app.run(main())
