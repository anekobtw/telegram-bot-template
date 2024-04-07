# Telegram Bot Template
![version](https://img.shields.io/badge/Project_version-v1.0-blue)
![aiogram](https://img.shields.io/badge/aiogram-v3.4.1-blue)
![licence](https://img.shields.io/badge/License-MIT-green)
![made with love](https://img.shields.io/badge/Made_with-Love-red)

This Telegram bot template provides a foundation for creating powerful and interactive bots using the [aiogram](https://github.com/aiogram/aiogram) library in Python.

# Table of contents
- [Quick Start](https://github.com/anekobtw/telegram-bot-template?tab=readme-ov-file#Quick-Start)
- [Customization](https://github.com/anekobtw/telegram-bot-template?tab=readme-ov-file#-customization)
    - [Structure](https://github.com/anekobtw/telegram-bot-template?tab=readme-ov-file#structure)
    - [Importing](https://github.com/anekobtw/telegram-bot-template?tab=readme-ov-file#importing)
    - [Running the bot](https://github.com/anekobtw/telegram-bot-template?tab=readme-ov-file#-running-the-bot)
- [Acknowledgements](https://github.com/anekobtw/telegram-bot-template?tab=readme-ov-file#-acknowledgements)
- [Contributing](https://github.com/anekobtw/telegram-bot-template?tab=readme-ov-file#-contributing)
- [Licence](https://github.com/anekobtw/telegram-bot-template?tab=readme-ov-file#-licence)

## 💻 Quick Start
1. Clone the repository\
`git clone https://github.com/anekobtw/telegram-bot-template.git`
2. Install dependencies.\
`pip install -r requirements.txt`
3. Update `.env` file in the project root directory and paste your bot token obtained from [BotFather](https://t.me/BotFather).
4. Customize any configuration settings or add additional functionality according to your requirements.
5. If you experience any problem and can't find a solution to it below, feel free to open an issue or DM me in telegram: [@anekobtw](https://t.me/anekobtw)

## ✨ Customization
### Structure
```telegram-bot-template/
└───bot
    │   .env
    │   main.py
    │   requirements.txt
    │
    ├───database
    │       Manager.py
    │       __init__.py
    │
    ├───handlers
    │       common.py
    │       __init__.py
    │
    ├───keyboards
    │       keyboards.py
    │       __init__.py
    │
    └───misc
            misc.py
            __init__.py
```

### Importing
As you can see, each folder has an `__init__.py` file which is used to make the whole coding process easier. You can learn more from the official documentation: https://docs.python.org/3/tutorial/modules.html.

Don't forget to import everything you need there (classes, functions). For example, if you add a new class to Manager.py in the database folder (such as a custom class), be sure to import it into the `__init__.py` file.

**Manager.py**
```py
class User:
    def __init__(self, id: int, name: str, surname: str) -> None:
        self.id = id
        self.name = name
        self.surname = surname
```

**_\_init__.py**
```py
from database.Manager import User
```

**Somewhere in other file**
```py
from database import User

user = User(1, 'Wednesday', 'Adams')  # creates an instance
```

### Running the bot
In order to run the bot, you should insert your bot token in `.env` file, and then run `main.py` file located in the root directory. In this file, the bot is defined in the asynchronous `run_bot()` function.

```py
async def run_bot():
    load_dotenv()
    TOKEN = os.getenv('TOKEN')

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='log.txt')

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode='HTML'))  # I just like 'HTML' parse mode, you can use another one
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.include_router(common.router)

    await dp.start_polling(bot)
```

Let me quickly explain the above code. First, it downloads the token from the environment. Then, logging is configured, and only then a bot instance is created. I've also written default properties, but if you don't use HTML as your default parsing mode, just remove it. In case you use aiogram states, a memory store is also created. Finally, it simply imports the router from the handlers folder, which processes all the commands, and starts working.
 
## 🙏 Acknowledgements
- [aiogram](https://github.com/aiogram/aiogram) - A modern and fully asynchronous framework for Telegram Bot API written in Python using asyncio
- [dotenv](https://github.com/theskumar/python-dotenv) - Reads key-value pairs from a .env file and can set them as environment variables. It helps in developing applications following the 12-factor principles.

## ⚙ Contributing
Contributions are always welcome! If you have any suggestions, feature requests, or bug reports, please feel free to open an issue on the [GitHub repository](https://github.com/anekobtw/telegram-bot-template).

## 📝 Licence
Copyright © 2024 anekobtw.
This project is [MIT](https://github.com/anekobtw/telegram-bot-template/blob/main/LICENSE) licensed.
