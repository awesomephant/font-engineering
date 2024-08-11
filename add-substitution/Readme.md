# Add an open-type substition

## Notes

- We want to do a type 6 substitution
- My first thought was to build the tables directly in Python, but that's impractical'
- Should use [`fealib`](https://fonttools.readthedocs.io/en/latest/feaLib/index.html) instead to generate the tables from plain-text feature declarations.

## Links

- https://forum.glyphsapp.com/t/opentype-subtitution-many-by-many-different-number/13126
- https://adobe-type-tools.github.io/afdko/OpenTypeFeatureFileSpecification.html#5-glyph-substitution-gsub-rules
- https://simoncozens.github.io/fonts-and-layout/features-2.html
- https://ilovetypography.com/OpenType/opentype-features.html
- https://rsheeter.github.io/font101/
- [Fontmake](https://github.com/googlefonts/fontmake)
- https://fonttools.readthedocs.io/en/latest/ttLib/tables/G_S_U_B_.html
