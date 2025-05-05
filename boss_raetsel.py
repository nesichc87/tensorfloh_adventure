from powerups import finde_powerup
from utils import slow_print

def boss_raetsel():
    
    slow_print("\n🐍 Die Python-Schlange zischt: 'Du kannst mich nicht besiegen, ohne mein Rätsel zu lösen!'")
    
    frage = "\nWelcher dieser Code-Schnipsel erzeugt eine Endlosschleife?"
    print("\nA) while x > 0: x -= 1")
    print("B) while True: print('Gefangen!')")
    print("C) for i in range(10): print(i)")

    antwort = input("Antwort: ").strip().upper()
    if antwort == "B":
        slow_print("✅ Richtig! Du hast die Python-Schlange überlistet!")
        return True
    else:
        slow_print("\n❌ Falsch! Die Python-Schlange lacht und macht dich schwächer...")

        choice = input("\nWillst du eine **zweite Chance**? (ja/nein) ").strip().lower()
        if choice == "ja":
            slow_print("\n🔄 Du bekommst eine zweite Möglichkeit!")

            # Option 1: Power-Up nutzen
            powerup = finde_powerup()
            slow_print(f"\n🔍 Du findest ein verstecktes Tool: {powerup.name}!")
            print("A) Nutze das Power-Up für eine bessere Chance")
            print("B) Zahle 20 HP für einen geheimen Tipp")
            print("C) Aktiviere die **Mampf-Technik** 😆")

            zweite_antwort = input("Deine Wahl: ").strip().upper()
            if zweite_antwort == "A":
                slow_print(f"\n⚡ Du nutzt {powerup.name}! Deine zweite Antwort ist automatisch richtig!")
                return True
            elif zweite_antwort == "B":
                slow_print("\n💡 Geheim-Tipp: Eine Endlosschleife läuft **ohne** Bedingung aus!")
                return boss_raetsel()  # Spieler darf erneut raten
            elif zweite_antwort == "C":
                slow_print("\n🤯 Du hast die **Mampf-Technik** aktiviert! Die Python-Schlange gibt auf!")
                return True
            else:
                slow_print("\n❌ Du hast deine Chance verspielt!")
                return False

        return False

