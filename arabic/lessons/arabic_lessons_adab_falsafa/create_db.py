import flet as ft
import sqlite3 as sq
import os

def crate_all_db():
    # المسار الحالي للملف نفسه
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # نخلي القاعدة تنشأ في نفس المجلد مع create_db.py
    db_path = os.path.join(BASE_DIR, "arabic_lessons.db")

    conn = sq.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS arabic_lessons(
            id INTEGER PRIMARY KEY,
            link TEXT 
        )
    ''')
    conn.commit()
    conn.close()
    print(f"Database created at: {db_path}")

if __name__ == '__main__':
    crate_all_db()
