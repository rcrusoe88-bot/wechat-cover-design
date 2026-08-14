from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1] / "assets" / "theme-previews"
TARGET = (1584, 672)

for folder in (ROOT, ROOT / "titled"):
    for path in folder.glob("theme*.png"):
        image = Image.open(path).convert("RGB")
        if image.size != TARGET:
            image.resize(TARGET, Image.Resampling.LANCZOS).save(path, quality=96)
