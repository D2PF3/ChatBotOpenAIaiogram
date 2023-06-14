# OpenAI GPT-3.5 turbo Telegram Chatbot

Этот проект содержит исходный код для создания простого чат-бота Telegram, который использует модель GPT-3.5 turbo от OpenAI для ответа на вопросы пользователей.

## Требования

Для запуска этого проекта вам понадобятся следующие компоненты:

- Python 3.7 и выше
- [Pip](https://pip.pypa.io/en/stable/)
- [OpenAI API Key](https://platform.openai.com/account/api-keys)
- [Telegram Bot Token](https://t.me/botfather)

## Установка и настройка

1. Клонируйте репозиторий на свой сервер, используя Git:

```bash
git clone https://github.com/D2PF3/ChatBotOpenAIaiogram
```

2. Перейдите в директорию проекта:

```bash
cd ChatBotOpenAIaiogram
```

3. Установите необходимые зависимости, используя pip:

```bash
pip install -r requirements.txt
```

4. Создайте файл .env в корневой директории проекта и добавьте следующие строки, заменив `!!!REPLACE!!!` своими реальными значениями:

```plaintext
OPENAI_API_KEY=!!!REPLACE!!!
TELEGRAM_BOT_TOKEN=!!!REPLACE!!!
```

## Запуск

После установки всех зависимостей и настройки файлов .env вы можете запустить чат-бота, выполнив следующую команду в терминале:

```bash
python main.py
```

Теперь ваш чат-бот Telegram запущен и готов к работе! Вы можете начать диалог с ним в Telegram.

## Логирование

Все вопросы и ответы сохраняются в файле `chat_log.json` в формате UTF-8. Это позволяет легко просматривать историю чата и использовать данные для дальнейшего анализа или улучшения модели.

В случае возникновения вопросов или проблем не стесняйтесь создавать issue в этом репозитории.
