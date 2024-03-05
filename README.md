# Задания по Python

## Задание 1: Генерация Excel файла

### Шаги:

1. Установите `openpyxl`, если это ещё не сделано: `pip install openpyxl`.
2. Используйте `Workbook` для создания нового Excel файла.
3. Создайте лист с названием "TDSheet" с колонками: Имя, текущая дата, текущее время.
4. Сохраните файл с именем в формате `ИМЯ_ТЕКДАТА_СЛУЧЧИСЛО.xlsx` в предполагаемую директорию.

[Документация по `openpyxl`](https://openpyxl.readthedocs.io/en/stable/tutorial.html)

## Задание 2: Отправка Email с помощью smtplib

### Шаги:

1. Настройте SMTP сервер через `smtplib`.
2. Подготовьте содержимое письма, включая вложение (Excel файл).
3. Отправьте письмо на указанный Email адрес.

[Документация по отправке Email с помощью Python](https://www.tutorialspoint.com/python/python_sending_email.htm)

## Задание 3: Создание Telegram бота с pyTelegramBotAPI

### Шаги:

1. Установите `pyTelegramBotAPI`: `pip install pyTelegramBotAPI`.
2. Зарегистрируйте бота в Telegram через BotFather и получите токен.
3. Напишите функцию обработчика сообщений, которая добавляет к тексту пользователя префикс "Strattonbot".
4. Запустите бота.

[Документация по pyTelegramBotAPI](https://groosha.gitbook.io/telegram-bot-lessons/chapter1)

## Задание 4: Логирование сообщений бота в базу данных

### Шаги:

1. Подключите вашу базу данных MongoDB к Python.
2. Настройте логирование сообщений из Telegram бота в базу данных с каждым обращением пользователя.


![image](https://github.com/awexeoz/practice/assets/120705475/46a7b349-137b-4197-887c-2532757278ad)
