# Write here all the code related to changes in the database
# An example is provided below

import sqlite3


class User:
    def __init__(self, id: int, name: str, surname: str) -> None:
        self.id = id
        self.name = name
        self.surname = surname


class UserManager:
    def __init__(self) -> None:  # the first time an instance is created, a database will be created
        self.connection = sqlite3.connect('users.db')  # file name
        self.cursor = self.connection.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT,
            surname TEXT
        )
        """)
        self.connection.commit()

    # just make any functions you need; examples are given
    def insert_user(self, name: str, surname: str) -> None:
        self.cursor.execute('INSERT INTO users(name, surname) VALUES (?, ?)', (name, surname))
        self.connection.commit()

    def find_user(self, id: int) -> User | None:
        self.cursor.execute('SELECT * FROM Users WHERE id = ? LIMIT 1', (id,))
        result = self.cursor.fetchone()
        return User(*result) if result else None
