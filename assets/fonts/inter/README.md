# Inter

Inter Variable is served locally from https://rsms.me/inter/font-files/InterVariable.woff2 (downloaded 14 September 2026).
The accompanying SIL Open Font License was obtained from https://github.com/google/fonts/blob/main/ofl/inter/OFL.txt.
No third-party font requests are made by the website. The variable file supports the full weight range used by the site.

## Website subsets

The website loads `inter-latin-variable.woff2` (99,372 bytes) for common Latin text, punctuation, currency symbols, and the arrows used in the interface. Extended Latin characters are served on demand from `inter-latin-extended-variable.woff2` (200,236 bytes), using separate CSS Unicode ranges. Both retain the original variable axes and OpenType features.

The original 352,240-byte file remains as the build source, but is no longer requested by the website stylesheet. Rebuild both subsets using `python scripts/subset-inter.py` from the repository root with `fonttools[woff]` installed. Validated with fonttools 4.65.0.

Pixel comparisons against the original font passed at weights 400, 500, 600, and 700, including accented names, punctuation, currency, and arrows. The current homepage requests only the common Latin subset; a test containing extended Latin names correctly requests the additional subset.
