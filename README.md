# MER-B The Last Signal

An illustrated educational visual novel about Opportunity: a little Mars rover built for 90 Martian days whose journey became a story of curiosity, perseverance, and connection across space.

Developed for the **NASA Space Apps Challenge 2026** (project-owner designation), MER-B invites students, families, and curious players to discover the rover’s purpose, ancient-water clues, engineering challenges, and lasting legacy. The previous project brief specifies a school-age audience and names the challenge **“Abandoned but not Forgotten: Storytelling about NASA’s Discarded Equipment on the Moon and Mars.”** Its official URL, wording, and 2026 eligibility still require owner confirmation; no official challenge specification is included here.

## About the story

A fading Martian sky opens a journey back to the beginning. Opportunity—Oppy—has a question to answer: was Mars once a world shaped by water? Across unfamiliar landscapes, difficult terrain, and long-awaited sunrises, a machine becomes an explorer we can care about.

The game combines accessible mission-history narration with imagined conversations between Opportunity, Earth, and Mission Control. Its themes are curiosity, teamwork, endurance, separation, and remembrance. It teaches planetary geology, solar-power vulnerability, and remote engineering while distinguishing evidence of ancient water from proof of life.

**History and dramatization:** the rover’s speech, emotions, immediate replies from Earth, and imagined final thoughts are fiction, not transcripts or telemetry. Dates, distances, and scientific claims are presented as historical content, but their NASA/JPL bibliography still needs to be supplied and checked. Artwork is illustrative rather than authenticated mission photography or engineering documentation.

## Implemented features

- A prologue, **nine chapters**, and a tribute epilogue, with one continuous story and one ending.
- Two three-option menus: choose an initial investigation and a response during sand recovery. Selections change immediate narration and sometimes the illustration, then rejoin the historical journey.
- **110 illustrated scene files**, dissolves, chapter cards, and a final blackout. Rover expressions and human characters are embedded in static artwork.
- **78 narrator voice clips**, seven looping music tracks covering the prologue and chapters 1–6, and a dedicated dialogue-reveal keyboard sound. Oppy, Earth, and Mission Control are text-only roles; chapters 7–9 and the epilogue have no music cues.
- A centered main menu, transparent dialogue presentation, bundled Source Sans 3 and Space Grotesk fonts, and adjustable native text reveal.
- Save/load pages, quicksave/quickload, history, skipping, auto-forward, audio mixers, and window/fullscreen preferences.
- Keyboard/mouse Help, conditional gamepad Help, and touch/small-screen UI variants. These variants do not establish a tested mobile release.

Rollback is disabled, although Back and rollback Help entries remain in the screen source. Use **History** to reread dialogue.

## Technology

The game uses **Ren’Py script and screen language with Python initialization code**. Existing local runtime records identify **Ren’Py 8.5.3.26051504**; use the **8.5.3 SDK** as the development baseline. Other SDK versions have not been validated. The virtual canvas is **1920 × 1080**, game version `1.0`, and distribution basename `MER_B`.

All custom fonts are local; no system font installation or runtime network connection is required by authored code. The skip indicator uses Ren’Py’s bundled `DejaVuSans.ttf`. No additional library is installed in `game/libs/`.

## Installation and setup

1. Obtain and extract the **Ren’Py 8.5.3 SDK** through the official [Ren’Py website](https://www.renpy.org/), also linked by the game’s About screen. No SDK was downloaded or installed during this review. On the inspected machine it already exists at `D:\Renpy\renpy-8.5.3-sdk`.
2. Download and extract the repository through GitHub’s **Code → Download ZIP**, or clone it with Git:

   ```sh
   git clone https://github.com/ZippoAI/MER-B.git
   ```

3. Locate the folder containing `game/script.rpy`, `game/options.rpy`, and this README. **That is the project root.** In this workspace it is `D:\MER-B-Game\MER-B`, not `D:\MER-B-Game`. A normal clone contains `game/` directly inside the repository folder.
4. Open the SDK launcher (`renpy.exe` on Windows). In launcher Preferences set the projects directory to the project folder’s **parent**—here, `D:\MER-B-Game`. Return to the project list and select `MER-B`; refresh if needed.
5. Choose **Launch Project**, then **Start**. This checkout contains source/assets, not a verified packaged release.
6. Choose **Check Script (Lint)** in the launcher. Resolve reported errors, then play from Start to the tribute, exercise every menu option, and test saves, loads, speed, audio, skip, and auto-forward. Lint alone does not establish playability.
7. Choose **Build Distributions** after validation. The installed SDK defines desktop packages including Windows/Linux and macOS packaging. Select the targets offered by your launcher and test extracted builds on each target before advertising support. No successful build or tested release platform is established here. Browser/mobile release support is unverified; platform-aware screens alone are insufficient.

Launching, linting, and building may generate caches, compiled scripts, logs, saves, and packages. This documentation-only review did not run those operations because output authorization was limited to three Markdown files.

## Project structure

```text
MER-B/                          # Git repository and Ren’Py root
├── README.md                   # Public overview and setup
├── PROJECT_CONTEXT_FOR_CHATGPT.md # Technical/creative handoff; spoilers
├── GAME_POLISH_CHECKLIST.md     # Prioritized final work
└── game/
    ├── script.rpy              # Complete story, image declarations, media cues
    ├── screens.rpy             # Dialogue, choices, menus, saves, Help
    ├── gui.rpy                 # Resolution, fonts, colors, layout, variants
    ├── options.rpy             # Identity, preferences, build/save identifiers
    ├── typography.rpy          # Bold/italic font mappings
    ├── typing_audio.rpy        # Reveal-sound channel and callbacks
    ├── images/scene/
    │   ├── start/              # 1.png–9.png
    │   └── chpt1/ … chpt9/     # Chapter illustrations
    ├── audio/
    │   ├── bg-music/           # Seven MP3 tracks
    │   ├── narrator/           # start/, chpt1/–chpt9/, epilogue/
    │   └── sfx/                # Keyboard-Sound.mp3
    ├── fonts/                  # Seven TTFs, licenses, provenance/checksums
    ├── gui/                    # Desktop/phone UI PNGs
    ├── libs/libs.txt           # Library-loading explanation
    └── tl/None/common.rpym     # Common UI string scaffold
```

Local caches, saves, compiled scripts, `log.txt`, and `traceback.txt` are generated/ignored state.

## How to play

Select **Start**. Left-click, Enter, or Space advances dialogue; click to finish a revealing line before continuing. Click a choice, or navigate with arrows and activate with Enter. Space advances dialogue without selecting choices.

Use **Save**, or Escape/right-click to open the game menu. **Load** resumes saved progress; desktop **Q.Save/Q.Load** provide quick slots. Numbered and automatic/quick pages are supported by the slot screen. Older-save compatibility needs testing: an existing local traceback records a historical save-load failure.

**Preferences/Prefs** adjusts text speed, auto-forward delay, music, sound (including typing), voice, and mute. **Auto** toggles automatic progression; hold Ctrl or use Tab/**Skip** to skip according to preferences. **History** rereads earlier dialogue. H/middle-click hides the interface. Help describes V for engine self-voicing and Shift+A for accessibility controls; these and gamepad behavior still require runtime verification.

## Credits, sources, and usage

| Contribution | Confirmed attribution / owner information needed |
| --- | --- |
| Mission subject | NASA’s Opportunity (MER-B); Spirit is mentioned as its twin. No mission bibliography, NASA dataset ID, or authenticated photo source is recorded. **Owner: supply NASA/JPL sources actually used.** |
| Team | Repository: [ZippoAI/MER-B](https://github.com/ZippoAI/MER-B). **Owner: supply team name, members, roles, and submission link.** A repository account is not a complete team credit. |
| Art, music, narrator voice, typing sound | Assets exist; creators, source URLs, licenses, permissions, and production methods are undocumented. **Owner: supply credits and redistribution permissions.** Filenames do not establish ownership. |
| Fonts | [Source Sans 3](https://github.com/adobe-fonts/source-sans), Adobe; [Space Grotesk](https://github.com/floriankarsten/space-grotesk), Space Grotesk Project Authors. SIL OFL 1.1; full notices and pinned provenance are bundled in `game/fonts/`. |
| Engine | [Ren’Py](https://www.renpy.org/); About displays its license information. |
| AI assistance | These three documentation files were prepared with ChatGPT/Codex assistance. **Owner: confirm AI use in code, story, images, music, or voice and supply the submission disclosure.** Appearance alone does not prove AI origin. |

No project-wide license file was found. Public source visibility does not establish permission to redistribute the game/media; font licensing is separately documented. Confirm rights and submission requirements before release. No NASA endorsement is claimed.

## Validation and next steps

The 16 November 2026 review read all six authored scripts, inventoried media, decoded all PNGs into an in-memory contact sheet, checked PNG signatures/dimensions and MP3 frame headers, checked literal asset references and label calls, and verified all nine font-manifest entries against byte lengths/SHA-256 values. All story media references resolve. The absent optional `gui/confirm_frame.png` has an existing `gui/frame.png` fallback. These are static checks, not audio listening, Ren’Py lint, build, or playthrough results.

See [complete project context](PROJECT_CONTEXT_FOR_CHATGPT.md) and [the polish checklist](GAME_POLISH_CHECKLIST.md). Priorities are runtime/save validation, historical sources and media rights, readability/audio review, and submission/distribution preparation.
