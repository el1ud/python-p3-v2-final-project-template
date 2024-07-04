class Food:
    def __init__(self, name, description, tags=None, menu_id=None, food_id=None):
        self.id = food_id
        self.name = name
        self.description = description
        self.tags = tags if tags is not None else []
        self.menu_id = menu_id

    def __repr__(self):
        return f"<Food(id={self.id}, name={self.name}, menu_id={self.menu_id})>"

    def __str__(self):
        return f"Food: {self.name}, Description: {self.description}, Menu ID: {self.menu_id}"

    def to_db_row(self):
        """Convert Food to a tuple for database operations."""
        return (self.name, self.description, self.tags, self.menu_id)

    @classmethod
    def from_db_row(cls, row):
        """Create a Food instance from a database row."""
        food_id, name, description, tags, menu_id = row
        return cls(name, description, tags, menu_id, food_id)