# That file is for all the database code
# An example is provided below

import sqlite3


class DBManager:
    def __init__(self, db_name: str, table_schema: str) -> None:
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        self.cursor.execute(table_schema)
        self.connection.commit()

    def execute_query(self, query: str, params: tuple = ()) -> None:
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetch_all(self, query: str, params: tuple = ()) -> list:
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetch_one(self, query: str, params: tuple = ()) -> list:
        self.cursor.execute(query, params)
        return self.cursor.fetchone()


class UsersManager(DBManager):
    def __init__(self) -> None:
        table_schema = """CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            username TEXT,
            password TEXT
        )"""
        super().__init__("databases/users.db", table_schema)

    def create_user(self, username: str, password: str) -> None:
        self.execute_query("INSERT INTO users(username, password) VALUES (?, ?)", (username, password))

    def delete_user(self, user_id: int) -> None:
        self.execute_query("DELETE FROM users WHERE user_id = ?", (user_id,))

    def find_users(self, username: str) -> list:
        return self.fetch_all("SELECT * FROM users WHERE username = ?", (username,))

    def get_user_info(self, user_id: int) -> list:
        return self.fetch_one("SELECT * FROM users WHERE user_id = ? LIMIT 1", (user_id,))
