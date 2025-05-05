from ascii_art import logo
from utils import slow_print
from spiellogik import sneak, attack
from kampf import Kämpfer, kampf

def start():
    print(logo)
    slow_print("Willkommen, mutiger Tensorfloh! 🦗")
    slow_print("Die Python-Schlange will die freien Daten verschlingen!")
    choice = input("Willst du (1) schleichen oder (2) direkt angreifen? ").strip()

    if choice == "1":
        sneak()
    elif choice == "2":
        attack()
    else:
        slow_print("Ungültige Eingabe. Wähle 1 oder 2.")
        start()
    # Initialisiere den Kampf mit Spieler & Gegner
    spieler = Kämpfer("Tensorfloh", 100, ["Syntax-Schwert", "Regex-Hammer", "Bug-Spray"])
    gegner = Kämpfer("Python-Schlange", 80, ["Rekursions-Biss", "Memory-Leak-Sturm", "Endlosschleifen-Falle"])

    kampf(spieler, gegner)

# Spiel starten
start()
