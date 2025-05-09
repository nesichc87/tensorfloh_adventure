import random
from utils import slow_print
from raetsel.raetsel import logik_raetsel
from kampf.powerups import finde_powerup
from easter_egg import mampf_ende
from kampf.boss_super_raetsel import super_raetsel
from story.secret_ending import meister_ende
from story.superhero_ending import superhero_ende
from kampf.boss_raetsel import boss_raetsel
import os

SPIEL_COUNTER_DATEI = "spiel_count.txt"

def spiel_counter_erhöhen():
    """Speichert, wie oft das Spiel gespielt wurde."""
    if not os.path.exists(SPIEL_COUNTER_DATEI):
        with open(SPIEL_COUNTER_DATEI, "w") as f:
            f.write("1")
    else:
        with open(SPIEL_COUNTER_DATEI, "r") as f:
            count = int(f.read().strip())
        with open(SPIEL_COUNTER_DATEI, "w") as f:
            f.write(str(count + 1))

def spiel_count_abrufen():
    """Liest den Spielzähler aus."""
    if not os.path.exists(SPIEL_COUNTER_DATEI):
        return 1
    with open(SPIEL_COUNTER_DATEI, "r") as f:
        return int(f.read().strip())

class Boss:
    """Klasse für den Boss-Gegner"""
    def __init__(self, name, hp, attacken):
        self.name = name
        self.hp = hp
        self.attacken = attacken

    def angreifen(self):
        attacke = random.choice(self.attacken)
        schaden = random.randint(15, 30)
        return attacke, schaden

def bosskampf(spieler, boss):
    slow_print(f"\n🐍🔥 Der finale Kampf beginnt gegen {boss.name}!")
    spiel_counter_erhöhen()  # Spiel-Durchlauf erhöhen
    if spiel_count_abrufen() >= 3:
        slow_print("\n💡 Ein mysteriöser Code-Glitch erscheint... etwas Seltsames passiert!")
        superhero_ende()
        return  # Spiel endet mit dem geheimen Superhelden-Ende!
    powerup = finde_powerup()
    
    while spieler.hp > 0 and boss.hp > 0:
        print(f"\n{spieler.name}: {spieler.hp} HP | {boss.name}: {boss.hp} HP")
        print("1. Angreifen | 2. Spezialfähigkeit | 3. Strategie wählen")
        choice = input("Was ist dein nächster Schritt? ").strip()

        if choice == "1":
            slow_print("\nDie Python-Schlange weicht aus! Du musst ihr Rätsel lösen!")
            if boss_raetsel():
                boss.hp -= 50  # Großer Schaden durch Rätsellösung!
            else:
                slow_print("\n❌ Du hast versagt... vielleicht gibt es einen anderen Weg?")
                choice = input("Willst du die **Mampf-Technik** aktivieren? (ja/nein) ").strip().lower()
                if choice == "ja":
                    mampf_ende()
                    return
                else:
                    slow_print("\n😞 Du akzeptierst dein Schicksal... vielleicht beim nächsten Mal!")
        elif choice == "2":
            slow_print("\n💥 Du setzt deine Spezialfähigkeit ein!")
            boss.hp -= 40  # Spezialangriff macht viel Schaden
        elif choice == "3":
            slow_print("\n🧠 Strategie wählen! Vielleicht gibt es einen klugen Weg, die Python-Schlange zu besiegen...")
            if super_raetsel():
                meister_ende()  # Löst die geheime Endszene aus!
                return  # Beendet den Bosskampf direkt!
            else:
                slow_print("\n🧠 Strategie wählen! Löse das Debugging-Rätsel, um einen taktischen Angriff auszuführen.")
                if logik_raetsel():
                    slow_print("✅ Dein kluger Manöver trifft perfekt!")
                    boss.hp -= 35
                else:
                    slow_print("❌ Die Python-Schlange weicht aus!")
        else:
            slow_print("Ungültige Eingabe! Versuch es erneut.")

        if boss.hp > 0:
            attacke, schaden = boss.angreifen()
            slow_print(f"\n⚡ {boss.name} kontert mit {attacke} und verursacht {schaden} Schaden!")
            spieler.hp -= schaden

    if spieler.hp > 0:
        slow_print("\n🎉 Du hast die Python-Schlange besiegt und die Welt der Daten gerettet!")
    else:
        slow_print("\n💀 Die Python-Schlange hat dich besiegt... aber vielleicht gibt es einen anderen Weg?")
        choice = input("Willst du die **Mampf-Technik** einsetzen? (ja/nein) ").strip().lower()
        if choice == "ja":
            mampf_ende()
        else:
            slow_print("\n😞 Du akzeptierst dein Schicksal... vielleicht beim nächsten Mal!")
