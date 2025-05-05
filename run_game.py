import sys
import os

# Add the `src/` folder to Python's module path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from src.tensorfloh_adventure import start  # Import game start function

if __name__ == "__main__":
    print("🚀 Starting Tensorfloh Adventure...")
    start()  # Run the game
