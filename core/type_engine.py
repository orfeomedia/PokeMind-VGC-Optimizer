# core/type_engine.py

class TypeEngine:
    def __init__(self):
        # Definimos las debilidades: Clave = Tipo atacante, Valor = Qué tipos reciben x2
        self.chart = {
            "Fire": ["Grass", "Ice", "Bug", "Steel"],
            "Water": ["Fire", "Ground", "Rock"],
            "Grass": ["Water", "Ground", "Rock"],
            "Electric": ["Water", "Flying"],
            "Fairy": ["Fighting", "Dragon", "Dark"],
            "Steel": ["Ice", "Rock", "Fairy"],
            "Ghost": ["Psychic", "Ghost"],
            # ... se completará con todos los tipos
        }

    def get_effectiveness(self, move_type, target_types):
        """
        Calcula el multiplicador de daño basado en los tipos del defensor.
        """
        multiplier = 1.0
        for t_type in target_types:
            if t_type in self.chart.get(move_type, []):
                multiplier *= 2.0
            # Aquí añadiríamos las resistencias (0.5) e inmunidades (0)
        return multiplier

    def analyze_team_weaknesses(self, team_types):
        """
        Recibe una lista de tipos del equipo y devuelve dónde nos falta cobertura.
        """
        report = {}
        for t in self.chart.keys():
            weak_count = 0
            for pokemon_types in team_types:
                if self.get_effectiveness(t, pokemon_types) > 1:
                    weak_count += 1
            report[t] = weak_count
        return report
