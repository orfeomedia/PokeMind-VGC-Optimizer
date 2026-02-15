# core/synergy_engine.py
from .type_engine import TypeEngine

class SynergyEngine:
    def __init__(self, team):
        self.team = team # Lista de objetos Pokemon
        self.te = TypeEngine()

    def check_defensive_holes(self):
        team_types = [p.types for p in self.team]
        analysis = self.te.analyze_team_weaknesses(team_types)
        
        print("--- 🛡️ Reporte de Vulnerabilidades del Equipo ---")
        for p_type, count in analysis.items():
            if count >= 3:
                print(f"⚠️ Alerta: {count} Pokémon son débiles a {p_type}!")
            elif count == 0:
                print(f"✅ Inmunidad/Resistencia perfecta contra {p_type}")

# Este módulo es el que hará que nuestra App sea "inteligente"
