from .food import Food
from .menu import Menu

import sqlite3

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()
