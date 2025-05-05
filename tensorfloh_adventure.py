import time



def slow_print(text):
    """Gibt Text langsam aus, um die Atmosphäre zu verstärken."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def start():
 # Bild laden (ersetze "bild.jpg" mit dem Pfad zu deinem Bild)
    logo = r"""
            (\_/)
           (o.o)  ⚔️
           (> <)  🛡️    *ready for battle*

          /     \
      .-'|  CODE |'-.
     |   |       |   |
     |___|_______|___|

                          ~~~~~~~🐍~~~~~~
                         /              \
                        |  ~~     ~~    |
                        | (  •   •  )  |   <— Fierce AI serpent!
                         \    ∞∞    /
                          ~~~~~~~~~
    """

    print(logo)

    slow_print("Willkommen, mutiger Tensorfloh! 🦗")
    slow_print("Die Python-Schlange droht, den freien Fluss der Daten zu verschlingen.")
    slow_print("Nur du kannst das verhindern! Wähle weise: ")

    choice = input("Willst du (1) schleichen oder (2) direkt angreifen? ").strip()
    
    if choice == "1":
        sneak()
    elif choice == "2":
        attack()
    else:
        slow_print("Ungültige Eingabe. Wähle 1 oder 2.")
        start()

def sneak():
    slow_print("\nDu schleichst dich vorsichtig durch die dunklen Code-Schluchten...")
    slow_print("Doch plötzlich erscheint eine Syntax-Falle!")
    
    choice = input("Willst du (1) die Falle entschärfen oder (2) fliehen? ").strip()
    
    if choice == "1":
        slow_print("\nDu analysierst die Syntax und entfernst geschickt die Fehler!")
        slow_print("Ein geheimer Weg öffnet sich – du kommst näher an die Python-Schlange heran! 🐍")
        final_battle()
    elif choice == "2":
        slow_print("\nDu springst weg, aber verlierst wertvolle Zeit...")
        start()
    else:
        slow_print("Ungültige Eingabe. Wähle 1 oder 2.")
        sneak()

def attack():
    slow_print("\nDu springst mit voller Kraft auf die Python-Schlange zu!")
    slow_print("Doch sie weicht aus und wirft eine Endlosschleife auf dich! 🔄")
    
    choice = input("Willst du (1) die Schleife unterbrechen oder (2) den Code debuggen? ").strip()
    
    if choice == "1":
        slow_print("\nMit einem kraftvollen Sprung entkommst du der Schleife!")
        final_battle()
    elif choice == "2":
        slow_print("\nDu erkennst das Problem und löst es! Die Python-Schlange wird schwächer...")
        final_battle()
    else:
        slow_print("Ungültige Eingabe. Wähle 1 oder 2.")
        attack()

def final_battle():
    slow_print("\n💥 Der letzte Kampf beginnt! Die Python-Schlange zischt bedrohlich! 💥")
    choice = input("Willst du (1) eine logische Falle stellen oder (2) sie frontal angreifen? ").strip()

    if choice == "1":
        slow_print("\nDu wirfst eine perfekt optimierte Funktion gegen die Python-Schlange...")
        slow_print("Sie verheddert sich in ihrem eigenen Code und wird endgültig besiegt! 🎉")
        slow_print("Tensorfloh hat die Freiheit der Daten gerettet! 🚀")
    elif choice == "2":
        slow_print("\nDu stürzt dich auf die Python-Schlange, doch sie kontert mit einem Syntaxfehler!")
        slow_print("Leider war das nicht genug – du musst deine Strategie überdenken...")
        start()
    else:
        slow_print("Ungültige Eingabe. Wähle 1 oder 2.")
        final_battle()

# Spiel starten
start()
