from pathlib import Path
import sys

folder = Path(__file__).parent

sys.path.insert(0, folder)

print(folder.parent)
print(type(folder))