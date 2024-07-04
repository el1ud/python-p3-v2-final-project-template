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

def add_menu(menu):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute("INSERT INTO menus (name) VALUES (?)", (menu.name,))
            conn.commit()
            print(f"Menu '{menu.name}' added successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred while adding the menu: {e}")

def add_food(food):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute("""
                INSERT INTO foods (name, description, tags, menu_id)
                VALUES (?, ?, ?, ?)
            """, food.to_db_row())
            conn.commit()
            print(f"Food '{food.name}' added successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred while adding the food: {e}")

def add_food(food):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")  # Enforce foreign key constraints
            cursor.execute("""
                INSERT INTO foods (name, description, tags, menu_id)
                VALUES (?, ?, ?, ?)
            """, food.to_db_row())
            conn.commit()
            print(f"Food '{food.name}' added successfully.")
    except sqlite3.IntegrityError as e:
        if "FOREIGN KEY constraint failed" in str(e):
            print(f"Error: The menu ID {food.menu_id} does not exist. Please provide a valid menu ID.")
        else:
            print(f"An integrity error occurred: {e}")
    except sqlite3.Error as e:
        print(f"An error occurred while adding the food: {e}")


def get_all_menus():
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM menus")
            rows = cursor.fetchall()
            if not rows:
                print("No menus found.")
                return []
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
            if not rows:
                print("No foods found.")
                return []
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
            if not rows:
                print(f"No foods found with the tag '{tag}'.")
                return []
            return [Food.from_db_row(row) for row in rows]
    except sqlite3.Error as e:
        print(f"An error occurred while finding foods by tag: {e}")
        return []

def delete_food(food_id):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute("DELETE FROM foods WHERE id=?", (food_id,))
            if cursor.rowcount == 0:
                print(f"No food with ID {food_id} found.")
            else:
                conn.commit()
                print(f"Food {food_id} deleted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred while deleting the food: {e}")

def update_food(food_id, name, description, tags):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute("""
                UPDATE foods
                SET name = ?, description = ?, tags = ?
                WHERE id = ?
            """, (name, description, tags, food_id))
            if cursor.rowcount == 0:
                print(f"No food with ID {food_id} found.")
            else:
                conn.commit()
                print(f"Food {food_id} updated successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred while updating the food: {e}")
