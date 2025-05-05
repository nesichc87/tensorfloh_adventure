import random
from utils import slow_print

class Kämpfer:
    """Kampfklasse für Spieler und Gegner."""
    def __init__(self, name, hp, attacken):
        self.name = name
        self.hp = hp
        self.attacken = attacken  # Liste von möglichen Angriffen

    def attackieren(self):
        attacke = random.choice(self.attacken)
        schaden = random.randint(5, 20)
        return attacke, schaden

    def verteidigen(self):
        return "verteidigt sich", random.randint(1, 10)
def kampf(spieler, gegner):
    slow_print(f"\n⚔️ Der Kampf beginnt zwischen {spieler.name} und {gegner.name}!")

    while spieler.hp > 0 and gegner.hp > 0:
        print(f"\n{spieler.name}: {spieler.hp} HP | {gegner.name}: {gegner.hp} HP")
        print("1. Angreifen | 2. Verteidigen | 3. Spezialangriff")
        choice = input("Was willst du tun? ").strip()

        if choice == "1":
            attacke, schaden = spieler.attackieren()
            slow_print(f"\n🔥 {spieler.name} nutzt {attacke} und verursacht {schaden} Schaden!")
            gegner.hp -= schaden
        elif choice == "2":
            verteidigung, reduzierung = spieler.verteidigen()
            slow_print(f"\n🛡️ {spieler.name} {verteidigung} und reduziert den gegnerischen Schaden um {reduzierung}.")
        elif choice == "3":
            slow_print("\n💥 Du setzt deinen Spezialangriff ein!")
            gegner.hp -= 30  # Fester hoher Schaden
        else:
            slow_print("Ungültige Eingabe! Versuche es erneut.")

        if gegner.hp > 0:
            attacke, schaden = gegner.attackieren()
            slow_print(f"\n⚡ {gegner.name} kontert mit {attacke} und verursacht {schaden} Schaden!")
            spieler.hp -= schaden

    if spieler.hp > 0:
        slow_print("\n🎉 Du hast den Kampf gewonnen!")
    else:
        slow_print("\n💀 Du wurdest besiegt... Versuch es erneut!")
