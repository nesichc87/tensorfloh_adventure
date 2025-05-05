import random
from utils import slow_print

def syntax_check():
    slow_print("\n🖥️ Der Code ist fehlerhaft! Korrigiere ihn:")
    print("\nprint(Hello World)")  # Fehler: fehlende Anführungszeichen
    antwort = input("Wie muss der Code richtig lauten?\nAntwort: ").strip()

    if antwort == 'print("Hello World")':
        slow_print("✅ Perfekt! Dein Debugging-Skill steigt!")
        return True
    else:
        slow_print("❌ Das ist noch nicht richtig! Versuch es nochmal.")
        return syntax_check()
