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
            1: "Syntaxfehler! Wie schreibt man `print('Hello World')` richtig?",
            2: "Endlose Rekursion! Was passiert, wenn eine Funktion sich immer wieder selbst aufruft?",
            3: "Speicherleck! Lösungsmöglichkeiten: (A) Garbage Collection (B) Mehr RAM kaufen?"
        }
        return challenges.get(self.schwierigkeitsgrad, "Eine unbekannte Bedrohung erscheint!")

# Gegner-Liste
gegner_liste = [
    Gegner("Bug-Armee", "Syntaxchaos!", 1),
    Gegner("Endlosschleifen-Krieger", "Unendlicher Codefluss!", 2),
    Gegner("Exceptions-Magier", "Wirft `IndexError`!", 3),
    Gegner("Speicherleck-Kraken", "Frisst Speicher langsam!", 3)
]

def begegne_gegner():
    gegner = random.choice(gegner_liste)
    print(f"\n⚔️ Du triffst auf {gegner.name}!")
    print(gegner.angreifen())
    print(gegner.herausforderung())
