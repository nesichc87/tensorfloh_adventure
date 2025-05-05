import random
from utils import slow_print

class PowerUp:
    """Power-Up für den Kampf"""
    def __init__(self, name, effekt):
        self.name = name
        self.effekt = effekt  # HP-Boost oder extra Schaden

    def anwenden(self, spieler):
        if "HP" in self.effekt:
            boost = random.randint(10, 20)
            spieler.hp += boost
            slow_print(f"💊 {self.name} gibt dir {boost} HP zurück!")
        elif "Schaden" in self.effekt:
            boost = random.randint(5, 15)
            slow_print(f"⚡ {self.name} erhöht deinen nächsten Angriff um {boost} Schaden!")
            return boost
        return 0

# Liste möglicher Power-Ups
powerups = [
    PowerUp("Garbage-Collector-Bombe", "Schaden-Boost"),
    PowerUp("Syntax-Upgrade", "HP-Regeneration"),
    PowerUp("RegEx-Schild", "HP-Boost"),
]

def finde_powerup():
    gefunden = random.choice(powerups)
    slow_print(f"🔍 Du hast ein Power-Up gefunden: {gefunden.name}!")
    return gefunden
