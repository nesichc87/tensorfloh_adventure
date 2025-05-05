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
        slow_print("❌ Falsch! Die Python-Schlange lacht und macht dich schwächer...")
        return False
