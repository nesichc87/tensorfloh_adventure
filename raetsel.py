from utils import slow_print

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
