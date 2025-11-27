import os
import pymysql

def get_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "flaskuser"),
        password=os.getenv("DB_PASSWORD", "flaskpass"),
        database=os.getenv("DB_NAME", "flaskdb"),
        cursorclass=pymysql.cursors.DictCursor,
    )
