import random

class Gegner:
    """Klasse für Gegner mit verschiedenen Fehler-Arten."""
    def __init__(self, name, attacke, schwierigkeitsgrad):
        self.name = name
        self.attacke = attacke
        self.schwierigkeitsgrad = schwierigkeitsgrad  # 1 = leicht, 3 = schwer

    def angreifen(self):
        return f"{self.name} greift mit {self.attacke} an!"

    def herausforderung(self):
        challenges = {
            1: "Oh nein! Eine fehlende Variable. Kannst du herausfinden, was fehlt?",
            2: "Ein endloser Loop! Welche Bedingung braucht die Schleife, um zu stoppen?",
            3: "Dein Code crasht. Welcher Fehler könnte schuld sein? (A) SyntaxError (B) Typo (C) Speicherproblem?"
        }
        return challenges.get(self.schwierigkeitsgrad, "Eine unbekannte Bedrohung erscheint!")

# Gegner-Liste
gegner_liste = [
    Gegner("Bug-Armee", "Syntaxchaos!", 1),
    Gegner("Endlosschleifen-Krieger", "Unendlicher Codefluss!", 2),
    Gegner("Exceptions-Magier", "Wirft `IndexError`!", 3),
    Gegner("Speicherleck-Kraken", "Frisst Speicher langsam!", 3),
    Gegner("Exception-Schatten", "Wirft zufällige Fehler!", 2),
    Gegner("Compiler-Kraken", "Frisst undefinierte Variablen!", 3),
    Gegner("Infinite-Loop-Krieger", "Hält dich in einer Schleife gefangen!", 2),
    Gegner("Typo-Golem", "Erzeugt Tippfehler in deinem Code!", 1)
]

def begegne_gegner():
    gegner = random.choice(gegner_liste)
    print(f"\n⚔️ Du triffst auf {gegner.name}!")
    print(gegner.angreifen())
    print(gegner.herausforderung())
