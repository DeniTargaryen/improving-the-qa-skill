import sys
from pathlib import Path

# Корень блока 0.4 должен быть в sys.path, иначе `from src...` не найдётся
ROOT = Path(__file__).resolve().parent
root_str = str(ROOT)
if root_str not in sys.path:
    sys.path.insert(0, root_str)
