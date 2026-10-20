
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


def seed_db():
    connection = get_connection()

    try:
        existing_posts = connection.execute(
            "SELECT COUNT(*) FROM posts"
        ).fetchone()[0]

        existing_tags = connection.execute(
            "SELECT COUNT(*) FROM tags"
        ).fetchone()[0]

        if existing_posts > 0 or existing_tags > 0:
            print("Database already contains data. Skipping seed.")
            return

        with open("seed.sql", "r", encoding="utf-8") as file:
            connection.executescript(file.read())

        connection.commit()
        print("Sample data added successfully!")

    finally:
        connection.close()



if __name__ == "__main__":
    init_db()
    seed_db()

