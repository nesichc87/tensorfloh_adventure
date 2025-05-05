import time

def slow_print(text):
    """Gibt Text langsam aus, um die Atmosphäre zu verstärken."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
