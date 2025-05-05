from ascii_art import logo
from utils import slow_print
from spiellogik import sneak, attack
from kampf import Kämpfer, kampf
from spiellogik import vorbereiten
from bosskampf import Boss, bosskampf

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
    boss = Boss("Python-Schlange", 200, ["Rekursions-Welle", "Speicherleck-Flut", "Endlosschleife-Falle"])

    boost = vorbereiten(spieler)  # Power-Up nutzen
    bosskampf(spieler, boss)
# Spiel starten
start()
