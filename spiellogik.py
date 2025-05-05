from gegner import begegne_gegner
from powerups import finde_powerup
from kampf import Kämpfer, kampf
from story import erzähle_story
from raetsel import logik_raetsel
from minispiele import syntax_check
from utils import slow_print
from raetsel import speicher_rätsel

def vorbereiten(spieler):
     slow_print("\n⚡ Vor dem Kampf hast du Zeit, dich vorzubereiten!")

     if speicher_rätsel():
        print("🛡️ Deine Speicheroptimierung gibt dir einen Verteidigungs-Bonus!")
    
    print("\nPlötzlich taucht ein Gegner auf!")
    begegne_gegner()

    # Story erzählen
    erzähle_story()

    # Rätsel lösen
    if logik_raetsel():
        slow_print("🎁 Du bekommst ein Bonus-Power-Up!")
    
    # Minispiel spielen
    if syntax_check():
        slow_print("🛡️ Deine Verteidigung wurde verstärkt!")

    # Power-Up finden
    powerup = finde_powerup()
    choice = input(f"Willst du {powerup.name} nutzen? (ja/nein) ").strip().lower()

    if choice == "ja":
        boost = powerup.anwenden(spieler)
        return boost
    else:
        slow_print("Du verzichtest auf das Power-Up...")
        return 0


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
