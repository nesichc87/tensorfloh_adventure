from utils import slow_print

def speicher_rätsel():
    print("\n💾 Dein Code verbraucht zu viel Speicher! Wie kannst du das Problem lösen?")
    print("A) Mehr RAM kaufen")
    print("B) Eine effizientere Datenstruktur verwenden")
    print("C) Einfach abwarten, es wird schon gehen")

    antwort = input("Antwort: ").strip().upper()
    if antwort == "B":
        print("✅ Richtig! Dein Code läuft jetzt viel effizienter!")
        return True
    else:
        print("❌ Falsch! Dein Programm läuft langsam weiter.")
        return speicher_rätsel()
def logik_raetsel():
    slow_print("\n🔎 Um deine Kampfkunst zu testen, musst du ein Logik-Rätsel lösen!")
    frage = "\nWas ergibt 2 + 2 * 2?"
    antwort = input(f"{frage}\nAntwort: ").strip()

    if antwort == "6":
        slow_print("✅ Richtig! Du hast die Falle überwunden und ein Power-Up verdient!")
        return True
    else:
        slow_print("❌ Falsch! Versuche es erneut.")
        return logik_raetsel()
