
import sqlite3


DATABASE = "blog.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def init_db():
    connection = get_connection()

    with open("schema.sql", "r", encoding="utf-8") as file:
        connection.executescript(file.read())

    connection.commit()
    connection.close()
    print("Database created successfully!")


if __name__ == "__main__":
    init_db()
