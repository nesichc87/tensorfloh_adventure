import pytest
from src.kampf.bosskampf import Boss
from src.kampf.kampf import Kämpfer

def test_boss_angriff():
    boss = Boss("Python-Schlange", 200, ["Rekursions-Welle", "Speicherleck-Flut"])
    attacke, schaden = boss.angreifen()
    assert isinstance(attacke, str)
    assert isinstance(schaden, int)
    assert schaden >= 15 and schaden <= 30

def test_spieler_angriff():
    spieler = Kämpfer("Tensorfloh", 120, ["Syntax-Schwert", "Bug-Spray"])
    attacke, schaden = spieler.attackieren()
    assert isinstance(attacke, str)
    assert isinstance(schaden, int)
    assert schaden >= 5 and schaden <= 20
