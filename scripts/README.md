# Asset preparation

These scripts prepare local assets before committing. They are not executed by the website, and no build service is required to serve the site.

- `python scripts/subset-inter.py` requires `fonttools[woff]`. It creates the common and extended Latin WOFF2 files from the retained original Inter font. Keep the CSS Unicode ranges aligned with the script when changing character coverage. All font weights and optical sizing are retained.
- `python scripts/resize-portrait.py` requires Pillow. It creates four WebP sizes from the retained portrait original, preserving its full composition. The page continues to apply its existing `object-fit: cover` crop.

The portrait's `sizes` attribute accounts for the source width needed to cover its fixed-height frame: approximately 520 CSS pixels on mobile and 770 on desktop, or the full column width when wider on tablets. This avoids selecting an undersized file merely because the visible frame is narrow. Keep `sizes` aligned with `.portrait-image` height and the About grid if those styles change.
