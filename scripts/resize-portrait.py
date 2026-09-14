"""Rebuild responsive WebP portraits from the retained original. Requires Pillow."""
from pathlib import Path
from PIL import Image, ImageOps
root = Path(__file__).resolve().parents[1]
source = root / 'assets/lee-button-profile.webp'
with Image.open(source) as original:
    image = ImageOps.exif_transpose(original).convert('RGB')
    for width in [640, 1080, 1600, 2048]:
        height = round(image.height * width / image.width)
        output = source.with_name(f'{source.stem}-{width}.webp')
        image.resize((width, height), Image.Resampling.LANCZOS).save(
            output, 'WEBP', quality=85, method=6)
        print(f'{output.name}: {width}×{height}, {output.stat().st_size:,} bytes')
