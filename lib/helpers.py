# import sqlite3
# from models import Menu, Food

# DATABASE = "menu.db"

# def create_tables():
#     with sqlite3.connect(DATABASE) as conn:
#         cursor = conn.cursor()
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS menus (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT NOT NULL
#             )
#         """)
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS foods (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT NOT NULL,
#                 description TEXT,
#                 tags TEXT,
#                 menu_id INTEGER,
#                 FOREIGN KEY(menu_id) REFERENCES menus(id)
#             )
#         """)
#         conn.commit()

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
    
def find_foods_by_tag(tag):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM foods WHERE tags LIKE ?", (f"%{tag}%",))
            rows = cursor.fetchall()
            return [Food.from_db_row(row) for row in rows]
    except sqlite3.Error as e:
        print(f"An error occurred while finding foods by tag: {e}")
        return []

def delete_food(food_id):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM foods WHERE id=?", (food_id,))
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred while deleting the food: {e}")

def update_food(food_id, name, description, tags):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE foods
                SET name=?, description=?, tags=?
                WHERE id=?
            """, (name, description, tags, food_id))
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred while updating the food: {e}")

import sqlite3
from models import Menu, Food

DATABASE = "menu.db"

def create_tables():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        # Enable foreign key support
        cursor.execute("PRAGMA foreign_keys = ON")
        
        # Create tables if they don't exist
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