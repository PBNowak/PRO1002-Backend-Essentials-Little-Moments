
import sqlite3
from pathlib import Path


def test_database_tables():
    database_path = Path(__file__).resolve().parent.parent / "blog.db"

    connection = sqlite3.connect(database_path)

    try:
        tables = connection.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
        """).fetchall()

        table_names = {table[0] for table in tables}

        assert {"posts", "comments", "tags", "post_tags"}.issubset(
            table_names
        )

    finally:
        connection.close()
