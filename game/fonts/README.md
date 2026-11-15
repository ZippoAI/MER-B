# MER-B The Last Signal — Typography

Two families keep the game coherent: Source Sans 3 offers open, humanist forms for sustained reading; Space Grotesk adds understated technical character to short cinematic and interface text. Narration deliberately shares the dialogue face rather than adding a third family or prolonged italic text.

| Role | Face | Default at 1920 × 1080 |
| --- | --- | --- |
| Dialogue and narration | Source Sans 3 Regular | 38 px, 8 px line spacing |
| Choices | Source Sans 3 Semibold | 38 px, 6 px line spacing |
| Speaker names | Space Grotesk Bold | 28 px, 0.6 px tracking |
| Centered title/chapter/tribute cards | Space Grotesk Medium | 40 px base; existing inline title sizes retained |
| Main menu title / navigation / headings | Space Grotesk Medium | Existing UI hierarchy, title 75 px |
| Menu body, history, help, credits, input | Source Sans 3 Regular | Existing interface hierarchy |
| Quick controls | Space Grotesk Medium | 22 px |

The small/touch variant uses 48 px story text, 34 px names, 45 px choices and 30 px quick controls. History entries grow to fit their text. Centered cards remain instantly readable; dialogue retains the native, preference-controlled 48 cps default. Fine outlines preserve contrast on transparent scenes. Ren'Py's existing DejaVu Sans is intentionally retained solely for the skip-triangle symbol; no story or interface prose depends on an installed system font.

## Sources, licenses, and redistribution

Downloaded unmodified static TrueType files on 15 November 2026 from the official upstream repositories:

- Source Sans 3: https://github.com/adobe-fonts/source-sans — Copyright 2010–2024 Adobe; Reserved Font Name “Source.” See `SourceSans3-OFL.txt` for the complete upstream notice and SIL Open Font License 1.1.
- Space Grotesk: https://github.com/floriankarsten/space-grotesk — Copyright 2020 The Space Grotesk Project Authors. See `SpaceGrotesk-OFL.txt` for the complete upstream notice and SIL Open Font License 1.1.

The licenses permit commercial use and bundling with software, subject to their conditions; do not sell the fonts by themselves. Ship both complete OFL files alongside these fonts. The binaries were not subsetted, converted, or modified. `font-sources.json` records pinned upstream commit URLs, byte lengths, and SHA-256 checksums for reproducibility. These local files require no internet connection during play. No system-wide font installation is needed. About-screen credits also identify the families and authors.

`game/gui.rpy` owns the font roles and responsive sizes; `game/screens.rpy` owns text layout and contrast; `game/typography.rpy` maps actual bold/italic files for Ren'Py text emphasis. Story text and save/build identifiers are unchanged.
