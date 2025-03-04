# Scraping-api

### Данный раздел readme посвещен работе с API телеграм.
Для работы с API используется библиотека pyrogram, являющаяся прослойкой для работы с официальным API Telegram - MTProto.

### Руководство пользователя
Данное руководство покрывает большую часть функционала написанной программы.

* Установите VS Code, Python 3.9 или новее, библиотеки pyrogram и pandas для Python, скопируйте этот репозиторий.
* Задайте Telegram-канал в файле main.py через переменную channel_username.
* Задайте желаемые теги и их триггеры в файле functions.py в функции extract_functions в переменной all_features.
* Выполните файл main.py
* Выполните файл log_to_pd.py
* В файле api.csv хранится датафрейм для дальнейшей обработки и анализа!
