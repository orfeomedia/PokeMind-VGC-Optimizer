# core/pokemon.py

class Pokemon:
    def __init__(self, name, types, stats, item=None, ability=None, tera_type=None):
        self.name = name
        self.types = types  # Lista: ["Fire", "Ghost"]
        self.stats = stats  # Diccionario: {"HP": 95, "Atk": 115, ...}
        self.item = item
        self.ability = ability
        self.tera_type = tera_type

    def __repr__(self):
        return f"<{self.name} | Types: {self.types} | Tera: {self.tera_type}>"

# Ejemplo de uso para nuestra App:
# incineroar = Pokemon("Incineroar", ["Fire", "Dark"], {"HP": 95, "Atk": 115}, "Sitrus Berry")
