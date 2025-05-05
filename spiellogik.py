from gegner import begegne_gegner
from utils import slow_print

def sneak():
    slow_print("\nDu schleichst dich vorsichtig durch die dunklen Code-Schluchten...")
    begegne_gegner()

def attack():
    slow_print("\nDu springst auf die Python-Schlange zu!")
    slow_print("Doch sie weicht aus und wirft eine Endlosschleife auf dich!")
    choice = input("Willst du (1) die Schleife unterbrechen oder (2) debuggen? ").strip()

    if choice == "1":
        slow_print("\nDu entkommst der Schleife!")
    elif choice == "2":
        slow_print("\nDu erkennst den Fehler und löst ihn! Die Python-Schlange wird schwächer...")
    else:
        slow_print("Ungültige Eingabe. Wähle 1 oder 2.")
        attack()
