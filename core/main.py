from core.parser import ShowdownParser
import json

def load_pokedex():
    with open('data/pokedex.json', 'r') as f:
        return json.load(f)

def run_app():
    print("--- 🧠 PokeMind Engine v1.0 ---")
    pokedex = load_pokedex()
    
    raw_data = input("Pega tu equipo de Showdown aquí y presiona Enter: \n")
    
    parsed_team = ShowdownParser.parse_team(raw_data)
    
    print("\n✅ Equipo Cargado Exitosamente:")
    for poke in parsed_team:
        name = poke['name']
        if name in pokedex:
            # Combinamos data del parser con data de la pokedex
            types = pokedex[name]['types']
            print(f"- {name} [{'/'.join(types)}] con {poke['item']}")
        else:
            print(f"- {name} (No encontrado en la base de datos local)")

if __name__ == "__main__":
    run_app()
