class Menu:
    def _init_(self, name, menu_id=None):
        self.id = menu_id
        self.name = name

    def _repr_(self):
        return f"<Menu(id={self.id}, name={self.name})>"