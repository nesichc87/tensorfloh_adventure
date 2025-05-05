from ascii_art import logo
from utils import slow_print
from spiellogik import sneak, attack

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

# Spiel starten
start()
