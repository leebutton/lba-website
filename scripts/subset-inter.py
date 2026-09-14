"""Rebuild the local Latin font subset. Requires fonttools[woff]."""
from pathlib import Path
from fontTools import subset

root = Path(__file__).resolve().parents[1]
source = root / 'assets/fonts/inter/inter-variable.woff2'
output = root / 'assets/fonts/inter/inter-latin-extended-variable.woff2'
# Retain accented Latin, combining marks, punctuation, currency, and arrows.
# Preserve all OpenType features and variable axes so existing shaping is unchanged.
ranges = [(0x20, 0x24F), (0x300, 0x36F), (0x1E00, 0x1EFF),
          (0x2000, 0x206F), (0x20A0, 0x20CF), (0x2100, 0x214F),
          (0x2190, 0x21FF)]
codepoints = {cp for lo, hi in ranges for cp in range(lo, hi + 1)}
codepoints.update([0x2212, 0xFEFF, 0xFFFD])
options = subset.Options()
options.layout_features = ['*']
options.name_IDs = ['*']
font = subset.load_font(str(source), options)
subsetter = subset.Subsetter(options=options)
subsetter.populate(unicodes=codepoints)
subsetter.subset(font)
font.flavor = 'woff2'
font.save(output)
print(f'{source.stat().st_size:,} → {output.stat().st_size:,} bytes')

# Common Latin text loads a smaller file. Extended Latin is fetched only when used.
core = set(range(0x20, 0x100)) | set(range(0x2000, 0x2070))
core.update([0x20AC, 0x2122, 0x2190, 0x2191, 0x2192, 0x2193, 0x2197, 0x2212, 0xFEFF, 0xFFFD])
font = subset.load_font(str(source), options)
subsetter = subset.Subsetter(options=options)
subsetter.populate(unicodes=core)
subsetter.subset(font)
font.flavor = 'woff2'
output = root / 'assets/fonts/inter/inter-latin-variable.woff2'
font.save(output)
print(f'Common Latin: {output.stat().st_size:,} bytes')
