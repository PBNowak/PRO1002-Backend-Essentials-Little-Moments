
import sqlite3
from datetime import date


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



def get_all_posts():
    connection = get_connection()

    try:
        posts = connection.execute("""
            SELECT id, title, body, published_date
            FROM posts
            ORDER BY published_date DESC, id DESC
        """).fetchall()

        result = []

        for post in posts:
            post_data = dict(post)

            tags = connection.execute("""
                SELECT tags.id, tags.name
                FROM tags
                JOIN post_tags ON tags.id = post_tags.tag_id
                WHERE post_tags.post_id = ?
                ORDER BY tags.name
            """, (post["id"],)).fetchall()

            post_data["tags"] = [dict(tag) for tag in tags]
            result.append(post_data)

        return result

    finally:
        connection.close()


def get_post(post_id):
    connection = get_connection()

    try:
        post = connection.execute("""
            SELECT id, title, body, published_date
            FROM posts
            WHERE id = ?
        """, (post_id,)).fetchone()

        return dict(post) if post else None

    finally:
        connection.close()


def get_tags_for_post(post_id):
    connection = get_connection()

    try:
        tags = connection.execute("""
            SELECT tags.id, tags.name
            FROM tags
            JOIN post_tags ON tags.id = post_tags.tag_id
            WHERE post_tags.post_id = ?
            ORDER BY tags.name
        """, (post_id,)).fetchall()

        return [dict(tag) for tag in tags]

    finally:
        connection.close()


def get_posts_by_tag(tag_id):
    connection = get_connection()

    try:
        posts = connection.execute("""
            SELECT posts.id, posts.title, posts.body,
                   posts.published_date
            FROM posts
            JOIN post_tags ON posts.id = post_tags.post_id
            WHERE post_tags.tag_id = ?
            ORDER BY posts.published_date DESC, posts.id DESC
        """, (tag_id,)).fetchall()

        return [dict(post) for post in posts]

    finally:
        connection.close()


def get_tag(tag_id):
    connection = get_connection()

    try:
        tag = connection.execute("""
            SELECT id, name
            FROM tags
            WHERE id = ?
        """, (tag_id,)).fetchone()

        return dict(tag) if tag else None

    finally:
        connection.close()



def create_post(title, body, tag_ids):
    connection = get_connection()

    try:
        cursor = connection.execute("""
            INSERT INTO posts (title, body, published_date)
            VALUES (?, ?, ?)
        """, (title, body, date.today().isoformat()))

        post_id = cursor.lastrowid

        for tag_id in tag_ids:
            connection.execute("""
                INSERT INTO post_tags (post_id, tag_id)
                VALUES (?, ?)
            """, (post_id, tag_id))

        connection.commit()
        return post_id

    except sqlite3.Error:
        connection.rollback()
        raise

    finally:
        connection.close()



def get_all_tags():
    connection = get_connection()

    try:
        tags = connection.execute("""
            SELECT id, name
            FROM tags
            ORDER BY name
        """).fetchall()

        return [dict(tag) for tag in tags]

    finally:
        connection.close()


def update_post(post_id, title, body, tag_ids):
    connection = get_connection()

    try:
        connection.execute("""
            UPDATE posts
            SET title = ?, body = ?
            WHERE id = ?
        """, (title, body, post_id))

        connection.execute("""
            DELETE FROM post_tags
            WHERE post_id = ?
        """, (post_id,))

        for tag_id in tag_ids:
            connection.execute("""
                INSERT INTO post_tags (post_id, tag_id)
                VALUES (?, ?)
            """, (post_id, tag_id))

        connection.commit()

    except sqlite3.Error:
        connection.rollback()
        raise

    finally:
        connection.close()

def get_comments_for_post(post_id):
    connection = get_connection()

    try:
        comments = connection.execute("""
            SELECT id, post_id, title, body, created_date
            FROM comments
            WHERE post_id = ?
            ORDER BY created_date DESC, id DESC
        """, (post_id,)).fetchall()

        return [dict(comment) for comment in comments]

    finally:
        connection.close()

def create_comment(post_id, title, body):
    connection = get_connection()

    try:
        cursor = connection.execute("""
            INSERT INTO comments (
                post_id, title, body, created_date
            )
            VALUES (?, ?, ?, ?)
        """, (
            post_id,
            title,
            body,
            date.today().isoformat()
        ))

        connection.commit()
        return cursor.lastrowid

    except sqlite3.Error:
        connection.rollback()
        raise

    finally:
        connection.close()


if __name__ == "__main__":
    init_db()
    seed_db()

