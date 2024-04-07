# Telegram Bot Template
![version](https://img.shields.io/badge/Project_version-v1.0-blue)
![aiogram](https://img.shields.io/badge/aiogram-v3.4.1-blue)
![licence](https://img.shields.io/badge/License-MIT-green)
![made with love](https://img.shields.io/badge/Made_with-Love-red)

This Telegram bot template provides a foundation for creating powerful and interactive bots using the [aiogram](https://github.com/aiogram/aiogram) library in Python.

## Installation
1. Clone the repository\
`git clone https://github.com/anekobtw/telegram-bot-template.git`
2. Install dependencies.\
`pip install requirements.txt`
3. Update `.env` file in the project root directory and paste your bot token obtained from [BotFather](https://t.me/BotFather).
4. Customize any configuration settings or add additional functionality according to your requirements.
5. If you experience any problem and can't find a solution to it below, feel free to DM me in telegram: [@anekobtw](https://t.me/anekobtw)

## Customization
- Structure
- Importing

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

If you want to use it in the other file in the code, simply type
```py
from database import User

user = User(1, 'Wednesday', 'Adams')  # creates an instance
```

## Acknowledgements
- [aiogram](https://github.com/aiogram/aiogram) - A modern and fully asynchronous framework for Telegram Bot API written in Python using asyncio\
- [dotenv](https://github.com/theskumar/python-dotenv) - Reads key-value pairs from a .env file and can set them as environment variables. It helps in developing applications following the 12-factor principles.

## Contributing
Contributions are always welcome! If you have any suggestions, feature requests, or bug reports, please feel free to open an issue on the [GitHub repository](https://github.com/anekobtw/telegram-bot-template).
