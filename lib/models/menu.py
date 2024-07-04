# class Menu:
#     def _init_(self, name, menu_id=None):
#         self.id = menu_id
#         self.name = name

#     def _repr_(self):
#         return f"<Menu(id={self.id}, name={self.name})>"
    
class Menu:
    def __init__(self, name, menu_id=None):
        self.id = menu_id
        self.name = name

    def __repr__(self):
        return f"<Menu(id={self.id}, name={self.name})>"

    def __str__(self):
        return f"Menu: {self.name}, ID: {self.id}"

    def to_db_row(self):
        """Convert Menu to a tuple for database operations."""
        return (self.name, self.id)

    @classmethod
    def from_db_row(cls, row):
        """Create a Menu instance from a database row."""
        menu_id, name = row
        return cls(name, menu_id)