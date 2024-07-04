import sqlite3
from models import Menu, Food

DATABASE = "menu.db"

def create_tables():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS menus (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS foods (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                tags TEXT,
                menu_id INTEGER,
                FOREIGN KEY(menu_id) REFERENCES menus(id)
            )
        """)
        conn.commit()

def add_menu(menu):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO menus (name) VALUES (?)", (menu.name,))
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred while adding the menu: {e}")

def add_food(food):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO foods (name, description, tags, menu_id)
                VALUES (?,?,?,?)
            """, food.to_db_row())
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred while adding the food: {e}")

def get_all_menus():
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM menus")
            rows = cursor.fetchall()
            return [Menu(*row) for row in rows]
    except sqlite3.Error as e:
        print(f"An error occurred while fetching all menus: {e}")
        return []

def get_all_foods():
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM foods")
            rows = cursor.fetchall()
            return [Food.from_db_row(row) for row in rows]
    except sqlite3.Error as e:
        print(f"An error occurred while fetching all foods: {e}")
        return []