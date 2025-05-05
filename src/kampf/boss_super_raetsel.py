from utils import slow_print

def super_raetsel():
    slow_print("\n🐍😈 Die Python-Schlange zischt: 'Du kannst mich nicht besiegen... außer du löst das ultimative Rätsel!'")
    
    print("\n💡 Logik-Frage: Wie kannst du eine Endlosschleife schreiben, die sich trotzdem selbst beendet?")
    print("A) while x > 0: x -= 1")
    print("B) while True: if random.random() < 0.01: break")
    print("C) for i in range(10): print(i)")

    antwort = input("Antwort: ").strip().upper()
    if antwort == "B":
        slow_print("\n✅ Die Python-Schlange ist beeindruckt... 'Du hast meine Logik übertroffen!'")
        slow_print("🐍💨 Die Schlange verliert ihre Kraft und verschwindet – **Ohne Kampf gewonnen!** 🎉")
        return True
    else:
        slow_print("\n❌ Die Python-Schlange lacht: 'Nicht klug genug! Weiter kämpfen!'")
        return False
