# from .food import Food
# from .menu import Menu

# import sqlite3

# CONN = sqlite3.connect('company.db')
# CURSOR = CONN.cursor()

from .food import Food
from .menu import Menu

import sqlite3

# Establishing a database connection
try:
    CONN = sqlite3.connect('company.db')
    CURSOR = CONN.cursor()
    print("Database connection established successfully.")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")