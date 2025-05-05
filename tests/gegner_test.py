import pytest
from src.kampf.gegner import Gegner

def test_gegner_herausforderung():
    gegner = Gegner("Infinite-Loop-Krieger", "Hält dich in einer Schleife gefangen!", 2)
    challenge = gegner.herausforderung()
    assert isinstance(challenge, str)
    assert "Schleife" in challenge

def test_gegner_angriff():
    gegner = Gegner("Exception-Schatten", "Wirft zufällige Fehler!", 3)
    attacke = gegner.angreifen()
    assert isinstance(attacke, str)
