import re
from .pokemon import Pokemon

class ShowdownParser:
    @staticmethod
    def parse_team(text):
        """
        Divide el bloque de texto en Pokémon individuales y los procesa.
        """
        raw_blocks = text.strip().split('\n\n')
        team = []
        for block in raw_blocks:
            team.append(ShowdownParser.parse_pokemon(block))
        return team

    @staticmethod
    def parse_pokemon(block):
        """
        Extrae la data de un bloque de texto de un solo Pokémon.
        """
        lines = [line.strip() for line in block.split('\n')]
        
        # 1. Nombre, Objeto y Género
        # Ejemplo: Flutter Mane @ Choice Specs
        first_line = lines[0]
        name_part = first_line.split('@')[0].strip()
        item = first_line.split('@')[1].strip() if '@' in first_line else None
        
        # Limpiar nombre si tiene género o apodo: "Pikachu (M)" -> "Pikachu"
        name = re.sub(r'\(.*?\)', '', name_part).strip()

        # 2. Extraer Atributos Clave
        ability = None
        tera_type = None
        evs = {"HP": 0, "Atk": 0, "Def": 0, "SpA": 0, "SpD": 0, "Spe": 0}
        
        for line in lines[1:]:
            if line.startswith("Ability:"):
                ability = line.replace("Ability:", "").strip()
            elif line.startswith("Tera Type:"):
                tera_type = line.replace("Tera Type:", "").strip()
            elif line.startswith("EVs:"):
                ev_list = line.replace("EVs:", "").strip().split('/')
                for ev in ev_list:
                    parts = ev.strip().split(' ')
                    val = int(parts[0])
                    stat = parts[1]
                    evs[stat] = val
        
        # Nota: Por ahora los tipos y stats base se cargarán desde nuestra DB
        # en la siguiente fase. Por ahora creamos el objeto con lo que tenemos.
        return {
            "name": name,
            "item": item,
            "ability": ability,
            "tera_type": tera_type,
            "evs": evs
        }

# Ejemplo de prueba interna:
# team = ShowdownParser.parse_team(texto_del_gold_team)
