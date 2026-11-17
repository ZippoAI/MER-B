# MER-B The Last Signal — Complete Current Project Context

Inspection: **16 November 2026**, Asia/Calcutta. Git/Ren’Py root: **D:/MER-B-Game/MER-B/**. Paths below are relative to that root unless stated otherwise. This document contains spoilers and replaces the obsolete context describing an artless, silent prototype.

**IMPLEMENTED** = present in source/files, not necessarily runtime-tested. **PARTIAL** = limited coverage of a broader capability. **MISSING** = absent from this checkout, not automatically required. **UNVERIFIED** = insufficient evidence or testing. Recommendations are not existing features.

## 1. Project purpose and current status

The owner describes **MER-B The Last Signal** as a nearly complete educational visual novel for NASA Space Apps Challenge 2026. The earlier context preserves a project brief naming **“Abandoned but not Forgotten: Storytelling about NASA’s Discarded Equipment on the Moon and Mars”**, aimed at school-age learners. The current request confirms the event/year but does not supply an official challenge page. Exact wording, eligibility, judging requirements and official URL remain **UNVERIFIED externally**. No authoritative challenge specification or submission package exists in this checkout.

The game tells Opportunity’s purpose, scientific discoveries, adversities, final communication and legacy through accessible narration and imagined rover–Earth conversations. Curiosity, teamwork, endurance, distance, loss and remembrance are its themes. The “one more sunrise” motif links extensions, storm survival and final hope. It teaches ancient-water evidence, solar power and remote engineering. It does not simulate rover operations or establish that life was discovered.

**IMPLEMENTED:** prologue, nine chapters, epilogue, two three-option menus, 110 story illustrations, 78 narrator recordings, seven BGM tracks, typing sound, custom typography and standard VN UI. **PARTIAL:** narration coverage, music coverage, educational interaction, attribution and release preparation. **UNVERIFIED:** current full playthrough, lint, save compatibility, audio balance, responsive/accessibility behavior and packaged delivery. Source has a complete narrative sequence; that is not release certification.

## 2. Repository state, technology and setup

Initial Git status was clean. Branch **development**, HEAD **7777828** (“Merge pull request #2 from ZippoAI/development”), remote **https://github.com/ZippoAI/MER-B.git**. Recent commits: d9d9c70 chapter 6 BGM; b450dd9 centered intro menu; 58e20bf chapter 9 voices; ea55d65 epilogue voices; 93608d6 chapter 8 voices; e024619 keyboard sound; 25e9aa6 chapter 5 BGM. Earlier context’s two-commit history and absence-of-media statements are obsolete. No branch/commit/push/fetch operations were performed.

All six authored scripts were read: script.rpy (838 lines), screens.rpy (1656), gui.rpy (486), options.rpy (216), typing_audio.rpy (74), typography.rpy (13). No other authored .rpy file was found. The common.rpym file is a common engine-string scaffold, not an alternate-language story. game/libs/libs.txt is explanatory; there are no added third-party libraries, package-manager dependencies or automated test suite.

| Setting | Actual value / implications |
| --- | --- |
| Runtime baseline | Existing local log/traceback identify **Ren’Py 8.5.3.26051504**, Windows 11; SDK exists at D:/Renpy/renpy-8.5.3-sdk |
| Technologies | Ren’Py narrative/screen language, Python initialization/callbacks, PNG, MP3, TTF |
| Virtual canvas | gui.init(1920, 1080); GL2 initialization recorded in log |
| Identity | config.name = MER-B The Last Signal; version 1.0; opening card says “MER-B: The Last Signal” |
| Distribution | build.name = MER_B |
| Save directory | config.save_directory = MER_B-1794736084; preserve this identifier |
| Rollback | config.rollback_enabled = False in script.rpy |
| Text defaults | preferences.text_cps = 48; preferences.afm_time = 15; later player preferences remain adjustable |
| Audio | has_sound / has_music / has_voice = True; no main-menu music configured |
| Dialogue window | auto; show/hide Dissolve(.2) |
| Menu transitions | enter/exit/intra = dissolve; after-load/end-game transitions None |
| History | 250 blocks, variable height, spacing 24 |
| Build rules | Ignore backup/hidden/temp patterns; image archiving examples inactive; documentation patterns only *.html and *.txt |
| Icon | game/gui/window_icon.png; visually a template-style mascot |
| Localization | gui.language = unicode; English story, no alternate-language story files |

gui.rpy initializes at offset -2, screens.rpy at -1; typing channel registration occurs at init -5 and callback installation at init 10. typography.rpy maps designed font faces. Authored code has no network-based gameplay/data fetch; About/font/Help hyperlinks and conditional engine sync controls are separate.

**Setup:** obtain/extract the 8.5.3 SDK; point launcher Preferences → projects directory to the project root’s parent (here D:/MER-B-Game); select MER-B; Launch Project → Start. Use Check Script (Lint), then playthrough/save/audio checks, then Build Distributions. The installed SDK’s doc/quickstart.html confirms launcher lint/build actions; renpy/common/00build.rpy defines PC Windows/Linux, Linux, Macintosh and Windows packages. These are SDK capabilities, not proof of tested project platform support. No project web/mobile build or successful release artifact is established. Do not execute .rpy with bare system Python. No download or installation was performed.

## 3. Annotated project structure

```text
D:/MER-B-Game/                    # workspace parent, not repository
└── MER-B/                        # Git + Ren’Py root
    ├── .git/                     # preserved branch/history
    ├── .gitignore                # saves/cache/compiled/generated/log exclusions
    ├── .vscode/settings.json     # hides compiled/archive/cache files in editor
    ├── README.md                 # public overview/setup/credits
    ├── PROJECT_CONTEXT_FOR_CHATGPT.md # this handoff
    ├── GAME_POLISH_CHECKLIST.md   # prioritized acceptance criteria
    ├── log.txt                   # ignored prior startup log
    ├── traceback.txt             # ignored prior load exception
    └── game/
        ├── script.rpy            # four speakers, 110 image definitions, 11 labels
        ├── screens.rpy           # say/choices/menu/save/history/help/preferences
        ├── gui.rpy               # fonts/layout/colors/resolution/device variants
        ├── options.rpy           # identity/preferences/build/save configuration
        ├── typography.rpy        # actual bold/italic replacement mappings
        ├── typing_audio.rpy      # reveal sound lifecycle and mixer
        ├── images/scene/
        │   ├── start/            # 9 PNGs
        │   ├── chpt1/            # 16 PNGs
        │   ├── chpt2/            # 12 PNGs
        │   ├── chpt3/            # 15 PNGs
        │   ├── chpt4/            # 7 PNGs
        │   ├── chpt5/            # 8 PNGs
        │   ├── chpt6/            # 9 PNGs
        │   ├── chpt7/            # 9 PNGs
        │   ├── chpt8/            # 21 PNGs
        │   └── chpt9/            # 4 PNGs
        ├── audio/
        │   ├── bg-music/         # 7 MP3s
        │   ├── narrator/         # 78 MP3s, start/chpt1–9/epilogue subdirectories
        │   └── sfx/              # Keyboard-Sound.mp3 only
        ├── fonts/                # 7 TTFs, README, provenance JSON, 2 OFLs
        ├── gui/                  # 80 desktop/phone PNGs
        │   ├── bar/, button/, overlay/, scrollbar/, slider/
        │   └── phone/            # small-device equivalents
        ├── libs/libs.txt         # library-loading explanatory stub
        ├── tl/None/common.rpym   # common engine UI string scaffold
        ├── cache/                # ignored generated analysis/bytecode/shaders
        ├── saves/                # ignored local saves/persistent state
        └── *.rpyc                # ignored compiled scripts
```

No separate character-sprite, movie, animated-background or epilogue-art directory exists. An exact media inventory and per-shot mapping follow below.

## 4. Characters, narrative style and control flow

| Speaker | Source identity | Personality / implementation |
| --- | --- | --- |
| narrator | Character("Narrator", color="#FF0000", callback=merb_keyboard_voice) | Gentle third-person explanation, history/science and memorial reflection; say screen hides Narrator namebox; most lines have recordings |
| oppy | Opportunity, #CBE8FF, same callback | Curious, earnest, playful and vulnerable; personifies the robot; no recorded character voice |
| earth | Earth, #86D7FF, same callback | Reassuring abstract human connection/guide; no named operator identity or recorded voice |
| mission | Mission Control, #F9D57B, same callback | Brief procedural communication in chapter 9; text-only |

Spirit is mentioned but has no speaking declaration. Human figures, rover expressions, Earth/Mars and monitors are baked into scene PNGs. SideImage support exists in the say screen but no story side-image assets are declared. No separate sprites, expression layers, lip-sync or character animation exists.

start presents the prologue, calls chapter_1 through chapter_9 and epilogue sequentially, then returns. Each called label returns. All ten calls resolve to labels; eleven labels exist in total. There are no route variables, alternate endings, scores, resources, chapter select, map navigation, minigames, driving mechanics or conditional later story changes. Two menus allow immediate narrative alternatives and rejoin the same history.

### Complete narrative and chapter presentation

Ranges below mean inclusive existing filenames. BGM basenames are under game/audio/bg-music/. Voice ranges are under game/audio/narrator/. Typing SFX applies to dialogue in every chapter.

| Chapter / label | Detailed narrative summary | Exact backgrounds / character implementation | Music / voice | Transitions and interactions | Coverage / limitations |
| --- | --- | --- | --- | --- | --- |
| Prologue / start | Far from home, a six-wheeled explorer watches sunlight fade after almost fifteen years. Oppy asks Earth about weather, remembers earlier storms, plans to save power, and hopes to explore again. Narrator rewinds to the beginning. | game/images/scene/start/1.png–9.png; rover embedded in landscapes; image 9 is black | The+Quiet+Between+Stars.mp3; start/voice1.mp3–voice10.mp3; one uncued narrator line | Solid #03070d, opening centered card, dissolves; advance only | IMPLEMENTED art/audio; no separate storm SFX |
| 1, A Little Robot with a Big Dream / chapter_1 | Introduces MER-B/Oppy and Spirit, asks whether ancient Mars had water and habitable conditions. Earth explains exploration despite uncertainty. Oppy promises careful observation, hears its nominal 90-sol duration, leaves Earth July 7 2003. | game/images/scene/chpt1/1.png–16.png; launch site/workshop/planets/rover/operators baked in | Beyond+the+Horizon.mp3; chpt1/voice1.mp3–voice9.mp3 | Solid #15202d, card/dissolves, 3-second pause on image 1 | IMPLEMENTED; launch illustration’s “Space Force Station” wording needs historical review |
| 2, Hello, Mars / chapter_2 | Seven-month cruise, dangerous parachute/rocket/airbag landing, opened lander at Eagle Crater. Oppy admires Mars, shares pictures, chooses a first investigation; six-wheels/six-steps joke ends arrival. | game/images/scene/chpt2/1.png–12.png; image 9 menu, branch images 10/11, common 12 | Beyond+the+Red+Horizon.mp3; chpt2/1.mp3–10.mp3 (no voice prefix); uncued menu-introduction line | Solid #8b452d, card/dissolves, three choices | IMPLEMENTED immediate branches; no persistent investigation |
| 3, The Memory of Water / chapter_3 | Layered rock and round hematite “blueberries” reveal ancient-water environments. Earth says not necessarily local oceans; Oppy learns to read rocks as a story. Explicitly no discovery of living Martians or proof of past life. | game/images/scene/chpt3/1.png–15.png; rock closeups, expressive rover, Earth/control imagery | ancient.mp3; chpt3/voice1.mp3–voice6.mp3 | Solid #6f3828, card/dissolves; advance only | IMPLEMENTED; no instrument/sample simulation; source and scale explanation pending |
| 4, The Ninetieth Sunrise / chapter_4 | Original 90-sol mission ends. Oppy worries it must stop; Earth confirms healthy systems and much left to explore. Another sunrise begins an extended adventure. | game/images/scene/chpt4/1.png–7.png; rover/operator art, some reuse | sunrise.mp3; chpt4/voice1.mp3–voice2.mp3 | Solid #3d4e5c, card/dissolves | IMPLEMENTED; 90-sol versus 90-day shorthand needs clarity |
| 5, Please Don’t Leave Me Here / chapter_5 | April 2005 sand trap: spinning wheels and little movement. Engineers test simulated terrain; player chooses a response. After more than five weeks Oppy escapes and hopes to avoid giant sand traps. | game/images/scene/chpt5/1.png–8.png; menu branches 4/5/6, rejoins 7; 4 and 5 byte-identical | dont-leave-me.mp3; chpt5/voice1.mp3–voice8.mp3 | Solid #553d2c, card/dissolves, three-choice menu | IMPLEMENTED; all recover; no real recovery calculation/failure state |
| 6, The Storm We Survived / chapter_6 | 2007 planet-wide storm darkens sky. Science stops to conserve solar power; weeks of waiting end in sunlight and another sunrise. | game/images/scene/chpt6/1.png–9.png; storm, rover, team, light-return images | storm.mp3; chpt6/voice1.mp3–voice6.mp3 | Solid #1f2a2f, card/dissolves | IMPLEMENTED; storm is static art, no wind/particles |
| 7, The World Keeps Getting Bigger / chapter_7 | Years of plains/crater exploration, 2011 Endeavour arrival, gypsum/clay water evidence, over-42-km milestone. Oppy wants to go farther; children grow into teenagers and students into scientists. | game/images/scene/chpt7/1.png–9.png; explicit scene order 1,2,3,4,5,6,8,9,7 | No BGM command; chapter 6 stops music; chpt7/voice1.mp3–voice7.mp3 | Solid #4c2d20, card/dissolves | Narration/art IMPLEMENTED; music coverage MISSING, intent UNVERIFIED; compressed discovery chronology |
| 8, When the Sun Disappeared / chapter_8 | June 2018, 45.16 km, Perseverance Valley. Dust blocks charging; Oppy remembers 2007, tries one more picture, conserves power, waits and rests. Narrator dates final data June 10 2018. Rover falls silent. | game/images/scene/chpt8/1.png–21.png, then engine black; progressively dusty expressive rover | No BGM/wind cue; chpt8/voice1.mp3–voice8.mp3 | Solid #0d0e11, card/dissolves; scene black with fade | IMPLEMENTED; imaginary picture/words are not last-telemetry evidence; typing/voice still audible |
| 9, Earth Is Still Calling / chapter_9 | No answer next day. Engineers continue commands/listening; more than 1,000 commands. NASA declares mission complete February 13 2019. | game/images/scene/chpt9/1.png–4.png; control-room/rover art; completion card over image 4 | No BGM/transmission cue; chpt9/voice1.mp3–voice5.mp3; Mission Control text only | Solid #141719, chapter card/dissolves and centered completion/date | IMPLEMENTED; no communication simulation or source bibliography |
| Epilogue, You Were Never Forgotten / epilogue | Recalls 90 sols, nearly fifteen years, 45.16 km, water evidence, survival and inability to return. Named tribute dates January 25 2004–June 10 2018. Final line says discoveries bring the universe closer. | Solid #d9c5a9, no dedicated epilogue illustration | No BGM; epilogue/voice1.mp3–voice7.mp3; final reflection uncued | Fade, centered chapter/tribute cards; final return | IMPLEMENTED ending; pale-background readability UNVERIFIED |

### Every choice and actual effect

| Label | Option | Immediate asset and response | Persistent effect |
| --- | --- | --- | --- |
| chapter_2 | Look at the horizon. | Keeps chapter2_9; voice audio/narrator/chpt2/7.mp3; panoramic image and terrain narration | None; rejoins chapter2_12 |
| chapter_2 | Examine the rocks. | chapter2_10 dissolve; chpt2/8.mp3; bedrock/ancient-water narration | Same |
| chapter_2 | Look at the ground. | chapter2_11 dissolve; chpt2/9.mp3; soil/round-object narration | Same |
| chapter_5 | Drive forward slowly. | chapter5_4 dissolve; chpt5/voice5.mp3; inches forward and stops | None; rejoins chapter5_7 |
| chapter_5 | Back up and re-angle. | chapter5_5 dissolve; chpt5/voice6.mp3; weight/angle narration; art identical to image 4 | Same |
| chapter_5 | Wait and scan the ground. | chapter5_6 dissolve; chpt5/voice7.mp3; gather data/wait for plan | Same |

Nine combinations, one ending. No correctness feedback, variable assignment, unlock or later dialogue effect. Recovery choices are dramatized abstractions, not validated driving instructions.

## 5. UI, typography and controls

Main menu uses plain dark green-gray game/gui/main_menu.png with centered title/version/navigation: Start, Load, Preferences, About; Help on PC/nonmobile web, Quit on PC. No main-menu music. Game menu uses game/gui/game_menu.png and overlay with side navigation. Main-menu subpages omit that side navigation and provide Return. Branding artwork is absent from menus, though title typography is customized.

Say window and namebox have **background None**. Desktop dialogue region: bottom 340 px; speaker x=290/y=24, dialogue x=290/y=72, width 1340. Narrator namebox is hidden by displayed name check; narrator remains identified in history. Text #f2f4f7, Source Sans 3 Regular 38 px, line spacing 8, 1 px dark outline. Names Space Grotesk 28 px, bold mapped to actual Bold, tracking 0.6. An outline is not a guarantee of contrast on every artwork/pale epilogue.

Choices: width 1185, near y=405, centered, spacing 33; Source Sans 3 Semibold 38 px, line spacing 6. Centered cards: Space Grotesk Medium 40 px base with inline title-size tags, line spacing 16, 1640-wide window/1560 max text; slow_cps False so cards appear immediately. Main title 75, interface body 33, headings 36, quick controls 22. Teal accent #00cc99/hover #66e0c1 with gray idle/white selected colors.

typography.rpy maps SourceSans3-Regular bold/italic/bold-italic to Bold/It/BoldIt TTFs, SpaceGrotesk-Medium bold to Bold. Small variant: dialogue 48, names 34, choices 45, quick controls 30, textbox 400, dialogue x=135/width=1650. No system font installation needed. DejaVuSans.ttf is engine-provided for skip triangles only. No custom text animation timer: native preference-based reveal defaults to 48 cps, preserving click-to-complete, skip, auto.

Desktop quick menu: Back, History, Skip, Auto, Save, Q.Save, Q.Load, Prefs. Touch: Back, Skip, Auto, Menu. Global rollback is disabled, conflicting with Back and Help rollback entries. Runtime appearance/enabled state is unverified; History is separate from rollback.

Save/load: screenshot/time/name, page naming, page navigation and delete action; 3×2 desktop slots or 2×2 small slots; 384×216 thumbnails. Auto/quick pages and upload/download sync controls are conditional on engine configuration; no sync-service usage is established. Save-directory identifier must remain stable, but identifier alone does not guarantee old script saves load.

Preferences: window/fullscreen on applicable variants, skipping unseen/after choices/transitions, text speed, auto time, music/SFX/voice volume and mute-all. Sample sound/voice tests are commented out. History: 250 variable-height entries; narrator name retained there. Help describes Enter/Space/click, arrows, Escape/right-click, Ctrl/Tab skip, H/middle-click hide, S screenshot, V self-voicing, Shift+A accessibility, conditional gamepad calibration. Rollback instructions contradict configuration. Runtime/accessibility compliance is UNVERIFIED.

Input, NVL and speech-bubble screens are generic framework support unused by story. Confirm is modal. Skip triangles animate with delayed_blink; notifications fade via notify_appear and expire after 3.25 seconds. These UI ATL effects are not rover/story animation.

## 6. Audio and cinematic behavior

**Music:** prologue and chapters 1–6 each play their track with fadein 2.0 loop, and stop music fadeout 2.0 before chapter return/calls. Chapters 7–9 and epilogue have no music commands. After chapter 6’s fade there is no programmed BGM; music-free does not mean silent because typing/voice remain. Loop seams, fades, balance and pacing need listening tests.

**Narration:** 78 explicit voice cues/files; all files referenced, including alternate-menu clips. Source has 81 narrator statements including mutually exclusive branches; a playthrough hears fewer. Three uncued statements: start “...we can go exploring again.”; chapter_2 “The player chooses what Opportunity investigates first:”; epilogue “Some explorers never return home. But their discoveries bring the universe closer to us.” No Oppy/Earth/Mission Control recordings, voice replay button, or custom voice timing. Actor/provider identity, production method and licensing unverified.

**Typing audio:** all four Character objects use merb_keyboard_voice, including narrator and Earth. game/audio/sfx/Keyboard-Sound.mp3 loops on custom channel merb_keyboard, mixer **sfx**, relative volume **0.70**, tight loop and 0.01-second fade-in/out. This is a recording during reveal, not per-character synthesized keystrokes. show_done marks reveal active; slow_done/interact_done/end clear it. Every speaker boundary clears stale state. Sync checks actual say text.slow, cps > 0, self-voicing off, SFX unmuted/nonzero, no skip/rollback/menu/main-menu/hidden UI. Context callbacks stop playback; before/after load and fast skip clear it; Q.Save explicitly clears first. Default _merb_keyboard_revealing=False is intended for older-save compatibility, not proof. Comments suggesting silent Earth/narrator do not supersede actual shared callback assignments.

Narration, music and typing can overlap on separate channels. Audio interruption, native voice behavior when advancing, text-speed/auto interaction, menu transitions, loading, mute, self-voicing and hidden-interface behavior need runtime verification. No explicit landing/wheel/wind/transmission/UI-click SFX commands exist. Only custom SFX is typing.

Story cinematics are built-in fade/dissolve, static image replacements, colored title cards, chapter 1’s 3-second pause and chapter 8 blackout. No video, camera pan/zoom, particles, parallax, moving sprites or story ATL. All image declarations force xysize=(1920,1080).

## 7. Asset inspection and provenance

All 190 PNGs were decoded into an **in-memory** contact sheet (110 story/80 GUI); four representative originals were also viewed. Artwork is stylized illustrative Mars/space/mission-control imagery with expressive rover closeups. The story’s 110 files contain **80 unique SHA-256 hashes**; reused files are not automatically missing assets. Chapter 5 images 4/5 are byte-identical. Chapter 7’s 1–6,8,9,7 order is explicit and must not be automatically numerically reordered.

Story dimensions vary: 55 at 1672×941, 24 at 1671×941, 7 at 1670×941; others include 1536×1024, 1535×1024, 1448×1086 and smaller near-widescreen sizes; one 1920×1080. Forced sizing stretches non-16:9 artwork rather than preserving aspect or cropping. This is confirmed geometry, not a demonstrated runtime cropping error. Story media total **242,700,918 bytes** (~231.5 MiB), audio **41,699,496 bytes** (~39.8 MiB), GUI **463,061 bytes**; these are source totals, not package/decoded-memory sizes.

Chapter 1 image 1 visibly says “Cape Canaveral Space Force Station” in the launch setting dated 2003 by the story: confirmed image text, historical suitability requires authoritative review. Rover proportions/details, rock scale and scientific visual cues need consistency review; illustrative images should not be presented as authenticated hardware/mission photography.

**MISSING provenance:** NASA/JPL bibliography/dataset IDs, authenticated photo sources, artwork/music/SFX licenses/creator names, narrator provider/actor permissions, team roles, broad project license, AI-production disclosure. This does not establish infringement or AI origin. **IMPLEMENTED font provenance:** Adobe Source Sans 3 and Space Grotesk Project Authors; SIL OFL 1.1 notices bundled, pinned official upstream URLs/lengths/SHA-256 recorded in font-sources.json. All nine manifest entries (7 TTFs/2 notices) matched. About currently credits fonts plus Ren’Py/version/license, not the full project team/media. These three docs disclose ChatGPT/Codex assistance; prior story/code/media production remains owner confirmation.

## 8. Historical/scientific review map

These are **script-stated and externally UNVERIFIED in this review**. No NASA source was consulted or retroactively described as actually used. Obtain the team’s genuine references, then verify.

| Label | Claims presented | Review focus |
| --- | --- | --- |
| start | Six wheels, eye-like cameras, solar panels, almost 15 years | Eye metaphor is not complete camera inventory; art not engineering documentation |
| chapter_1 | MER-B/Oppy, Spirit twin, past water/habitability, >100 million km on arrival, nominal 90 Martian days, July 7 2003 launch | Separation versus cruise distance; sol duration; launch date and imagery |
| chapter_2 | Seven-month cruise, parachute/rockets/airbags, Eagle Crater, lander petals | Landing chronology/hardware; immediate Earth replies omit signal delay |
| chapter_3 | Hematite spheres, layered rocks/minerals, water environments; no proof of life | Mineral formation in context, no universal hematite=water shortcut; distinguish habitability/biology |
| chapter_4 | Original mission extension, “90-day” shorthand | Sol versus Earth-day precision |
| chapter_5 | April 2005 sand entrapment, tests, >5-week escape | Event dates/duration; hypothetical choices versus actual commands |
| chapter_6 | 2007 planet-wide storm, science pause/low power/recovery | Duration and operations; “across the planet” must not suggest circumnavigation |
| chapter_7 | 2011 Endeavour arrival plus gypsum/clay, first rover beyond 42 km elsewhere | Separate discovery dates compressed into one sentence; milestone terminology |
| chapter_8 | June 2018, Perseverance Valley, 45.16 km, final data June 10 | Last contact versus fictional picture/words; distance rounding; storm severity |
| chapter_9 | >1,000 commands, mission complete February 13 2019 | Commands versus attempts/signals; administrative closure versus last contact |
| epilogue | 90 sols, almost 15 years, distance/water/broken components; tribute Jan 25 2004–June 10 2018 | Rounded duration; surface-contact interval versus launch–closure interval |

No in-game dramatization disclaimer or source bibliography exists. The README now supplies the distinction, but in-game claims still need citations. Instrument names/measurements, communication delay, and why recovery/retrieval was not undertaken are limited or absent. No fact cards, glossary, timeline, quiz or NASA data viewer is implemented.

## 9. Validation, known limitations and priorities

**Performed:** full authored source review; existing docs/logs/traceback/Git inspection; all-image decoding/contact-sheet review; PNG signature/end-marker/dimension scan; MP3 header scan (all 86 contain a recognized MPEG frame); literal-reference/call checks; font-manifest byte-length/SHA-256 verification. All 110 declared story images are used; all ten calls resolve; all 78 narrator files are referenced. No missing active story image/music/voice/custom-font path was found.

The broad literal-reference scan found optional gui/confirm_frame.png absent, but its fallback list contains existing gui/frame.png. Dynamic [prefix_] style paths, engine black and engine DejaVuSans.ttf are not literal missing custom files. Header/reference checks do not prove complete MP3 decoding or Ren’Py parsing.

**Not run:** fresh Ren’Py lint/compile/launch, full playthrough, save/load, listening/transcription, current UI render, build, web/mobile or accessibility tests. These operations can generate files outside the three authorized Markdown outputs, so they were not invoked. No downloads, installs, temporary files, new images or reports were created. Contact sheets existed only in memory.

Existing ignored log.txt begins **2026-11-15 23:05:13 UTC** (16 November 04:35 IST), records 8.5.3 initialization/GL2/RTX 4060 display setup, and does not prove completion. Existing traceback.txt, dated 15 November 18:05, records **“Could not load the game. Perhaps the script changed in an incompatible way.”** Stack reaches a load action at an older chapter 2 menu; its source line numbers differ from current source. This establishes a historical save incompatibility, not a current fresh-start crash. Preserve saves; test legacy/new saves separately. The old context additionally reports earlier SDK launch attempts failing with “Illegal System DLL Relocation”; that was not reproduced here and must not be reported as a new result.

**Confirmed issues:** rollback Help/UI mismatch; heterogeneous aspect ratios forced to widescreen; incomplete source/media/team/AI credits and no in-game fiction disclaimer. **Coverage decisions:** no late BGM, three uncued narrator lines, no character voice/animation, flat menu, solid epilogue, reused choice art. Their desirability depends on intent; they are not automatically bugs. **UNVERIFIED risks:** overflow/contrast, audio overlap/cutoffs/loop seams, text-speed migration, typing lifecycle, load performance, current/legacy saves, platform packaging.

Keep the existing game and polish it. Priorities: lint/playthrough; new/legacy save checks; official challenge and NASA fact verification; rights/team/AI credits; audio readback/mix; readability and aspect-ratio review; separately authorized rollback-message fix; intentional late-chapter music/voice decisions; target build testing; demo and submission package. No gameplay/source/media modification was authorized here.

For future ChatGPT work, preserve build/save IDs, call order, common historical outcomes and existing saves. Request owner-only facts: official challenge link/criteria, team identities, actual NASA sources, media creators/rights, AI tools used, target release platforms and intentional audio coverage. Do not resurrect obsolete claims that story media/custom fonts are absent.

## 10. Individual illustration / shot mapping

This table follows script order, including mutually exclusive menu branches. Each row describes the statements following that scene until the next scene or label. Dialogue is excerpted as a scene locator; the chapter summaries above provide the narrative context. All images are IMPLEMENTED static PNGs at forced 1920×1080 size; no separate character sprite is attached. Every listed change uses dissolve. SFX is the shared typing callback on speaker lines. Chapter BGM continues according to section 4; voice paths below are relative to game/. Runtime timing, readability and audio quality remain UNVERIFIED. Menus/conditional branch boundaries can span adjacent rows. No row implies an additional label exists.

| Label / image | Exact image path | Narrative/dialogue locator | Speakers / voice files (game-relative) | Interaction / coverage note |
| --- | --- | --- | --- | --- |
| start / opening_1 | `game/images/scene/start/1.png` | Far away from everything we have ever called home... / On a world where no human has ever walked... | narrator; `audio/narrator/start/voice1.mp3`, `audio/narrator/start/voice2.mp3`, `audio/narrator/start/voice3.mp3` | Advance dialogue; no standalone sprite/animation |
| start / opening_2 | `game/images/scene/start/2.png` | It has six wheels. / Two cameras that look almost like eyes. | narrator; `audio/narrator/start/voice4.mp3`, `audio/narrator/start/voice5.mp3`, `audio/narrator/start/voice6.mp3` | Advance dialogue; no standalone sprite/animation |
| start / opening_3 | `game/images/scene/start/3.png` | For nearly fifteen years, it has wandered across this world. | narrator; `audio/narrator/start/voice7.mp3` | Advance dialogue; no standalone sprite/animation |
| start / opening_4 | `game/images/scene/start/4.png` | But today, the sunlight is fading. | narrator; `audio/narrator/start/voice8.mp3` | Advance dialogue; no standalone sprite/animation |
| start / opening_5 | `game/images/scene/start/5.png` | That's strange... / It's getting dark already? | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| start / opening_6 | `game/images/scene/start/6.png` | Earth? / I think there's something wrong with the weather. | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| start / opening_7 | `game/images/scene/start/7.png` | It's okay. / We've been through storms before. | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| start / opening_8 | `game/images/scene/start/8.png` | ...we can go exploring again. | narrator; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| start / opening_9 | `game/images/scene/start/9.png` | But to understand this moment... / We must go back to where it all began. | narrator; `audio/narrator/start/voice9.mp3`, `audio/narrator/start/voice10.mp3` | Black PNG; narrator rewind, then sequential chapter calls |
| chapter_1 / chapter1_1 | `game/images/scene/chpt1/1.png` | Establishing image / pause | none; no voice cue in this shot | 3-second pause; establishing launch illustration; historical signage review |
| chapter_1 / chapter1_2 | `game/images/scene/chpt1/2.png` | There was once a little robot. Its name was Opportunity. | narrator; `audio/narrator/chpt1/voice1.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_1 / chapter1_3 | `game/images/scene/chpt1/3.png` | Its official designation was Mars Exploration Rover-B. But the people who built it had a shorter name. | narrator; `audio/narrator/chpt1/voice2.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_1 / chapter1_4 | `game/images/scene/chpt1/4.png` | They called it Oppy. | narrator; `audio/narrator/chpt1/voice3.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_1 / chapter1_5 | `game/images/scene/chpt1/5.png` | Opportunity wasn't built to fight. It wasn't built to conquer. It was built to answer a question. | narrator; `audio/narrator/chpt1/voice4.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_1 / chapter1_6 | `game/images/scene/chpt1/6.png` | Long ago, was Mars a world of water? / Could this cold, dusty planet once have been a place where life might survive? | narrator; `audio/narrator/chpt1/voice5.mp3`, `audio/narrator/chpt1/voice6.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_1 / chapter1_7 | `game/images/scene/chpt1/7.png` | To find out, humans built two explorers. Spirit... And Opportunity. They were twins, sent to opposite sides of Mars. | narrator; `audio/narrator/chpt1/voice7.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_1 / chapter1_8 | `game/images/scene/chpt1/8.png` | So... that's Mars? | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_1 / chapter1_9 | `game/images/scene/chpt1/9.png` | It looks pretty far away. | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_1 / chapter1_10 | `game/images/scene/chpt1/10.png` | It is. More than a hundred million kilometers away when you arrive. | earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_1 / chapter1_11 | `game/images/scene/chpt1/11.png` | That's a long way to travel. What will I find there? | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_1 / chapter1_12 | `game/images/scene/chpt1/12.png` | We don't know yet. That's why we're sending you. | earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_1 / chapter1_13 | `game/images/scene/chpt1/13.png` | Oh. So... I'm supposed to find something nobody has seen before? / Exactly. | oppy, earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_1 / chapter1_14 | `game/images/scene/chpt1/14.png` | Then I'll look really carefully. I promise. | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_1 / chapter1_15 | `game/images/scene/chpt1/15.png` | Opportunity was designed for a mission lasting just 90 Martian days. / Ninety days? What happens after that? | narrator, oppy, earth; `audio/narrator/chpt1/voice8.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_1 / chapter1_16 | `game/images/scene/chpt1/16.png` | On July 7, 2003, Opportunity left Earth. It would never return. But its journey was only beginning. | narrator; `audio/narrator/chpt1/voice9.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_2 / chapter2_1 | `game/images/scene/chpt2/1.png` | After nearly seven months in space, Opportunity reached Mars. / Landing was dangerous. There was no runway. | narrator; `audio/narrator/chpt2/1.mp3`, `audio/narrator/chpt2/2.mp3`, `audio/narrator/chpt2/3.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_2 / chapter2_2 | `game/images/scene/chpt2/2.png` | Um... Earth? | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_2 / chapter2_3 | `game/images/scene/chpt2/3.png` | We're here. | earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_2 / chapter2_4 | `game/images/scene/chpt2/4.png` | I think I'm falling! | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_2 / chapter2_5 | `game/images/scene/chpt2/5.png` | The rover bounced across the surface before finally coming to rest. | narrator; `audio/narrator/chpt2/4.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_2 / chapter2_6 | `game/images/scene/chpt2/6.png` | ...Did I make it? / The lander petals opened. Opportunity saw Eagle Crater for the first time. | oppy, narrator; `audio/narrator/chpt2/5.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_2 / chapter2_7 | `game/images/scene/chpt2/7.png` | All around it stretched a world of dust, rocks, and distant horizons. A world no human had ever touched. / Oh... It's beautiful. | narrator, oppy; `audio/narrator/chpt2/6.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_2 / chapter2_8 | `game/images/scene/chpt2/8.png` | Hello, Mars. My name is Opportunity. I hope you don't mind if I look around. / We received your pictures. And they're wonderful. | oppy, earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_2 / chapter2_9 | `game/images/scene/chpt2/9.png` | The player chooses what Opportunity investigates first: / Opportunity takes a panoramic image and prepares to study the terrain. | narrator; `audio/narrator/chpt2/7.mp3` | First investigation menu / option-specific response; rejoins image 12 |
| chapter_2 / chapter2_10 | `game/images/scene/chpt2/10.png` | Opportunity inspects the exposed bedrock and begins the search for ancient water. | narrator; `audio/narrator/chpt2/8.mp3` | First investigation menu / option-specific response; rejoins image 12 |
| chapter_2 / chapter2_11 | `game/images/scene/chpt2/11.png` | Opportunity studies the soil and the small round objects scattered across the landscape. | narrator; `audio/narrator/chpt2/9.mp3` | First investigation menu / option-specific response; rejoins image 12 |
| chapter_2 / chapter2_12 | `game/images/scene/chpt2/12.png` | There's so much here! Where do I even begin? / One step at a time. | oppy, earth, narrator; `audio/narrator/chpt2/10.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_3 / chapter3_1 | `game/images/scene/chpt3/1.png` | Opportunity examined layered rock and discovered small round stones scattered across the ground. | narrator; `audio/narrator/chpt3/voice1.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_3 / chapter3_2 | `game/images/scene/chpt3/2.png` | Earth? I've found something strange. | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_3 / chapter3_3 | `game/images/scene/chpt3/3.png` | What have you got? | earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_3 / chapter3_4 | `game/images/scene/chpt3/4.png` | Little round stones. They're everywhere! They look like tiny blueberries! | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_3 / chapter3_5 | `game/images/scene/chpt3/5.png` | The scientists nicknamed them blueberries. They were not fruit. / They were small spheres containing hematite, an iron mineral formed in environments involving water. | narrator; `audio/narrator/chpt3/voice2.mp3`, `audio/narrator/chpt3/voice3.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_3 / chapter3_6 | `game/images/scene/chpt3/6.png` | Opportunity's instruments studied minerals and sedimentary rock. Together, these clues revealed a world of ancient water. | narrator; `audio/narrator/chpt3/voice4.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_3 / chapter3_7 | `game/images/scene/chpt3/7.png` | Wait... Mars wasn't always like this? | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_3 / chapter3_8 | `game/images/scene/chpt3/8.png` | No. Long ago, water affected these rocks. | earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_3 / chapter3_9 | `game/images/scene/chpt3/9.png` | Water? Like the oceans on Earth? | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_3 / chapter3_10 | `game/images/scene/chpt3/10.png` | Not necessarily oceans here. But this place preserves evidence of ancient water. | earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_3 / chapter3_11 | `game/images/scene/chpt3/11.png` | So these rocks... They're telling us a story? | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_3 / chapter3_12 | `game/images/scene/chpt3/12.png` | They are. And you're helping us read it. | earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_3 / chapter3_13 | `game/images/scene/chpt3/13.png` | Then I'll remember every little detail. Every rock. Every mark. Every clue. | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_3 / chapter3_14 | `game/images/scene/chpt3/14.png` | Opportunity did not discover living Martians. / It did not prove life had existed there. But it helped show that ancient Mars had environments shaped by liquid water. | narrator; `audio/narrator/chpt3/voice5.mp3`, `audio/narrator/chpt3/voice6.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_3 / chapter3_15 | `game/images/scene/chpt3/15.png` | Maybe I won't find anyone here. But I can help Earth learn whoâ€”or whatâ€”might have been here long ago. | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_4 / chapter4_1 | `game/images/scene/chpt4/1.png` | Time passed. Opportunity explored rocks and studied the landscape. Then one day, its original 90-sol mission came to an end. | narrator; `audio/narrator/chpt4/voice1.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_4 / chapter4_2 | `game/images/scene/chpt4/2.png` | Earth? | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_4 / chapter4_3 | `game/images/scene/chpt4/3.png` | Yes, Oppy? / I think... I've finished my mission. | earth, oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_4 / chapter4_4 | `game/images/scene/chpt4/4.png` | I did everything I could. Does that mean... I have to stop now? | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_4 / chapter4_5 | `game/images/scene/chpt4/5.png` | Your systems are still working. And there is still so much to explore. | earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_4 / chapter4_6 | `game/images/scene/chpt4/6.png` | Wait... You mean I can keep going? / Yes. | oppy, earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_4 / chapter4_7 | `game/images/scene/chpt4/7.png` | Really?! / Really. | oppy, earth, narrator; `audio/narrator/chpt4/voice2.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_5 / chapter5_1 | `game/images/scene/chpt5/1.png` | Mars was beautiful. But Mars was also unforgiving. In April 2005, Opportunity drove into soft sand and sank. | narrator; `audio/narrator/chpt5/voice1.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_5 / chapter5_2 | `game/images/scene/chpt5/2.png` | Okay... Let's try moving forward. / The wheels spun. The rover barely moved. | oppy, narrator; `audio/narrator/chpt5/voice2.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_5 / chapter5_3 | `game/images/scene/chpt5/3.png` | Earth? I think I need some help. / On Earth, engineers tested possible solutions using rover models and simulated Martian sand. | oppy, narrator; `audio/narrator/chpt5/voice3.mp3`, `audio/narrator/chpt5/voice4.mp3` | Recovery menu / option-specific response; rejoins image 7 |
| chapter_5 / chapter5_4 | `game/images/scene/chpt5/4.png` | Opportunity tries a careful recovery. The rover inches forward, then stops. | narrator; `audio/narrator/chpt5/voice5.mp3` | Recovery menu / option-specific response; rejoins image 7; images 4/5 identical |
| chapter_5 / chapter5_5 | `game/images/scene/chpt5/5.png` | The rover shifts its weight and tries a safer angle. The sand groans beneath it. | narrator; `audio/narrator/chpt5/voice6.mp3` | Recovery menu / option-specific response; rejoins image 7; images 4/5 identical |
| chapter_5 / chapter5_6 | `game/images/scene/chpt5/6.png` | Opportunity gathers data and waits for Mission Control to find the best route. | narrator; `audio/narrator/chpt5/voice7.mp3` | Recovery menu / option-specific response; rejoins image 7 |
| chapter_5 / chapter5_7 | `game/images/scene/chpt5/7.png` | After more than five weeks of careful work, Opportunity escaped the sand. | narrator; `audio/narrator/chpt5/voice8.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_5 / chapter5_8 | `game/images/scene/chpt5/8.png` | I thought that sand was going to keep me forever! / There's still a lot of Mars left to see. | oppy, earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_6 / chapter6_1 | `game/images/scene/chpt6/1.png` | By 2007, Opportunity had traveled across the planet for more than three years. / Then the sky began to darken. A planet-wide dust storm spread across Mars. | narrator; `audio/narrator/chpt6/voice1.mp3`, `audio/narrator/chpt6/voice2.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_6 / chapter6_2 | `game/images/scene/chpt6/2.png` | Earth? Where did the sunlight go? | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_6 / chapter6_3 | `game/images/scene/chpt6/3.png` | A major dust storm is blocking the Sun. We need to conserve your power. | earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_6 / chapter6_4 | `game/images/scene/chpt6/4.png` | Does that mean no exploring today? | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_6 / chapter6_5 | `game/images/scene/chpt6/5.png` | Not today. | earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_6 / chapter6_6 | `game/images/scene/chpt6/6.png` | All right. I can wait. / The rover suspended its scientific activities. Its power dropped dangerously low. | oppy, narrator; `audio/narrator/chpt6/voice3.mp3`, `audio/narrator/chpt6/voice4.mp3`, `audio/narrator/chpt6/voice5.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_6 / chapter6_7 | `game/images/scene/chpt6/7.png` | Oh! There you are! I knew you'd come back, Sun. | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_6 / chapter6_8 | `game/images/scene/chpt6/8.png` | We've got more exploring to do, Oppy. | earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_6 / chapter6_9 | `game/images/scene/chpt6/9.png` | Just one more sunrise? / One more sunrise. | oppy, earth, narrator; `audio/narrator/chpt6/voice6.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_7 / chapter7_1 | `game/images/scene/chpt7/1.png` | The days became months. The months became years. / Opportunity crossed immense plains, studied crater walls, and followed the geological history of Mars. | narrator; `audio/narrator/chpt7/voice1.mp3`, `audio/narrator/chpt7/voice2.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_7 / chapter7_2 | `game/images/scene/chpt7/2.png` | In 2011, it arrived at the rim of Endeavour Crater and found white veins of gypsum and clay minerals, evidence of ancient environments with water. | narrator; `audio/narrator/chpt7/voice3.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_7 / chapter7_3 | `game/images/scene/chpt7/3.png` | Earth? I think Mars is telling us an even bigger story. | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_7 / chapter7_4 | `game/images/scene/chpt7/4.png` | It is. And you found another piece of it. | earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_7 / chapter7_5 | `game/images/scene/chpt7/5.png` | Do you think people will remember all these places? / Your pictures are already helping people understand a world they've never visited. | oppy, earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_7 / chapter7_6 | `game/images/scene/chpt7/6.png` | Opportunity became the first rover to travel more than 42 kilometers on another world. And it kept going. | narrator; `audio/narrator/chpt7/voice4.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_7 / chapter7_8 | `game/images/scene/chpt7/8.png` | There's still something beautiful over there. Could we go a little farther? | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_7 / chapter7_9 | `game/images/scene/chpt7/9.png` | We'll find a safe path. | earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_7 / chapter7_7 | `game/images/scene/chpt7/7.png` | Children who were born when Opportunity landed were now teenagers. / Students who followed the mission were becoming scientists and engineers. | narrator; `audio/narrator/chpt7/voice5.mp3`, `audio/narrator/chpt7/voice6.mp3`, `audio/narrator/chpt7/voice7.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_1 | `game/images/scene/chpt8/1.png` | By June 2018, Opportunity had traveled 45.16 kilometers on Mars. It was exploring Perseverance Valley. / The name seemed fitting, because no one could have guessed how much perseverance this little machine would show. | narrator; `audio/narrator/chpt8/voice1.mp3`, `audio/narrator/chpt8/voice2.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_2 | `game/images/scene/chpt8/2.png` | Earth? Look at this place. It's beautiful. I think this might be one of my favorite views. | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_3 | `game/images/scene/chpt8/3.png` | We have more observations planned here. | earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_4 | `game/images/scene/chpt8/4.png` | Then let's get started! / Then a dust cloud rolled across the sky. The sunlight began to fade. | oppy, narrator; `audio/narrator/chpt8/voice3.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_5 | `game/images/scene/chpt8/5.png` | Earth? My batteries aren't charging the way they should. | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_6 | `game/images/scene/chpt8/6.png` | A major dust storm is blocking the Sun. We need to conserve power. | earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_7 | `game/images/scene/chpt8/7.png` | Another storm? | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_8 | `game/images/scene/chpt8/8.png` | Yes. A very large one. | earth; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_9 | `game/images/scene/chpt8/9.png` | All right. I can wait. | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_10 | `game/images/scene/chpt8/10.png` | The dust grew thicker. / Opportunity's systems were designed to conserve power, but this storm was more severe than the one it had survived in 2007. | narrator; `audio/narrator/chpt8/voice4.mp3`, `audio/narrator/chpt8/voice5.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_11 | `game/images/scene/chpt8/11.png` | I can't see the Sun anymore. | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_12 | `game/images/scene/chpt8/12.png` | It must still be up there. Just hidden. | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_13 | `game/images/scene/chpt8/13.png` | I'll take one more picture. Maybe Earth can tell me what the sky looks like. | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_14 | `game/images/scene/chpt8/14.png` | On June 10, 2018, Opportunity sent its final data to Earth. | narrator; `audio/narrator/chpt8/voice6.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_15 | `game/images/scene/chpt8/15.png` | Earth? Did you get my picture? | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_16 | `game/images/scene/chpt8/16.png` | I think I should save what power I have left. | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_17 | `game/images/scene/chpt8/17.png` | We've done this before. Remember? The sky got dark. We waited. And the Sun came back. | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_18 | `game/images/scene/chpt8/18.png` | So I'll wait again. | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_19 | `game/images/scene/chpt8/19.png` | There's still so much I haven't seen. So many rocks. So many places to explore. / And I still haven't shown Earth everything. | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_20 | `game/images/scene/chpt8/20.png` | That's okay. It doesn't all have to happen today. / I'll rest for a little while. | oppy; no voice cue in this shot | Advance dialogue; no standalone sprite/animation |
| chapter_8 / chapter8_21 | `game/images/scene/chpt8/21.png` | Just one more sunrise... / ...and then we can go a little farther. | oppy, narrator; `audio/narrator/chpt8/voice7.mp3` | Last illustrated shot, then separate black fade and voice8.mp3 |
| chapter_9 / chapter9_1 | `game/images/scene/chpt9/1.png` | The next day came. Opportunity did not answer. / No response. | narrator, mission; `audio/narrator/chpt9/voice1.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_9 / chapter9_2 | `game/images/scene/chpt9/2.png` | But on Earth, they did not give up. / Engineers kept listening and sending commands, hoping to reach their little explorer. | narrator, mission; `audio/narrator/chpt9/voice2.mp3`, `audio/narrator/chpt9/voice3.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_9 / chapter9_3 | `game/images/scene/chpt9/3.png` | More than a thousand commands were sent in the effort to restore contact. | narrator; `audio/narrator/chpt9/voice4.mp3` | Advance dialogue; no standalone sprite/animation |
| chapter_9 / chapter9_4 | `game/images/scene/chpt9/4.png` | Attempting contact. / No signal. | mission, narrator; `audio/narrator/chpt9/voice5.mp3` | Mission-complete centered card over current illustration |

### Non-illustration beats

| Label / beat | Visual and media | Interaction / status |
| --- | --- | --- |
| start opening title | Solid #03070d, centered title; prologue BGM starts first | Advance; IMPLEMENTED |
| chapter_1–chapter_9 title cards | Chapter-specific Solid colors listed in section 4; fade then centered heading/subtitle | Advance; IMPLEMENTED; no separate title-card images |
| chapter_8 after image 21 | engine black with fade; audio/narrator/chpt8/voice8.mp3, “The rover fell silent beneath the dust.” | Advance; IMPLEMENTED; no BGM cue |
| chapter_9 conclusion | centered MISSION COMPLETE / FEBRUARY 13, 2019 over chapter9_4 | Advance; IMPLEMENTED |
| epilogue | Solid #d9c5a9 with fade, chapter card, seven voice cues, centered tribute, uncued final narrator line | Advance to final return; IMPLEMENTED; background-art coverage MISSING, runtime contrast UNVERIFIED |

## 11. Exact media and font inventory

All paths are repository-relative. This inventory excludes caches, compiled scripts, saves and Git metadata. A numeric filename in chapter 2 audio intentionally lacks the voice prefix. No additional animations or movie assets were found. MP3 headers were recognized, but no complete decode/listening test was performed.

### game/images/scene

| File | Bytes | Dimensions / note |
| --- | ---: | --- |
| `game/images/scene/chpt1/1.png` | 2,477,892 | 1672 × 941; static PNG |
| `game/images/scene/chpt1/10.png` | 2,119,242 | 1672 × 941; static PNG |
| `game/images/scene/chpt1/11.png` | 1,195,359 | 1672 × 941; static PNG |
| `game/images/scene/chpt1/12.png` | 2,358,130 | 1536 × 1024; static PNG |
| `game/images/scene/chpt1/13.png` | 2,198,968 | 1672 × 941; static PNG |
| `game/images/scene/chpt1/14.png` | 2,198,968 | 1672 × 941; static PNG |
| `game/images/scene/chpt1/15.png` | 1,195,359 | 1672 × 941; static PNG |
| `game/images/scene/chpt1/16.png` | 2,134,147 | 1672 × 941; static PNG |
| `game/images/scene/chpt1/2.png` | 2,720,458 | 1670 × 941; static PNG |
| `game/images/scene/chpt1/3.png` | 2,689,240 | 1672 × 941; static PNG |
| `game/images/scene/chpt1/4.png` | 3,095,886 | 1672 × 941; static PNG |
| `game/images/scene/chpt1/5.png` | 2,316,716 | 1672 × 941; static PNG |
| `game/images/scene/chpt1/6.png` | 2,420,647 | 1672 × 941; static PNG |
| `game/images/scene/chpt1/7.png` | 2,302,309 | 1672 × 941; static PNG |
| `game/images/scene/chpt1/8.png` | 2,313,381 | 1672 × 941; static PNG |
| `game/images/scene/chpt1/9.png` | 1,160,586 | 1090 × 628; static PNG |
| `game/images/scene/chpt2/1.png` | 2,846,103 | 1672 × 941; static PNG |
| `game/images/scene/chpt2/10.png` | 3,342,425 | 1672 × 941; static PNG |
| `game/images/scene/chpt2/11.png` | 2,811,589 | 1671 × 941; static PNG |
| `game/images/scene/chpt2/12.png` | 2,433,885 | 1672 × 941; static PNG |
| `game/images/scene/chpt2/2.png` | 2,173,761 | 1672 × 941; static PNG |
| `game/images/scene/chpt2/3.png` | 2,150,001 | 1672 × 941; static PNG |
| `game/images/scene/chpt2/4.png` | 3,029,123 | 1448 × 1086; static PNG |
| `game/images/scene/chpt2/5.png` | 2,388,161 | 1672 × 941; static PNG |
| `game/images/scene/chpt2/6.png` | 2,925,712 | 1672 × 941; static PNG |
| `game/images/scene/chpt2/7.png` | 2,297,591 | 1671 × 941; static PNG |
| `game/images/scene/chpt2/8.png` | 2,225,906 | 1671 × 941; static PNG |
| `game/images/scene/chpt2/9.png` | 3,059,731 | 1672 × 941; static PNG |
| `game/images/scene/chpt3/1.png` | 1,618,991 | 1121 × 632; static PNG |
| `game/images/scene/chpt3/10.png` | 1,804,603 | 1260 × 724; static PNG |
| `game/images/scene/chpt3/11.png` | 1,990,519 | 1261 × 706; static PNG |
| `game/images/scene/chpt3/12.png` | 1,778,817 | 1262 × 713; static PNG |
| `game/images/scene/chpt3/13.png` | 1,879,229 | 1263 × 705; static PNG |
| `game/images/scene/chpt3/14.png` | 1,900,486 | 1258 × 708; static PNG |
| `game/images/scene/chpt3/15.png` | 1,606,367 | 1266 × 709; static PNG |
| `game/images/scene/chpt3/2.png` | 1,756,942 | 1264 × 707; static PNG |
| `game/images/scene/chpt3/3.png` | 1,647,520 | 1248 × 708; static PNG |
| `game/images/scene/chpt3/4.png` | 1,785,791 | 1284 × 707; static PNG |
| `game/images/scene/chpt3/5.png` | 1,810,963 | 1265 × 703; static PNG |
| `game/images/scene/chpt3/6.png` | 1,886,335 | 1260 × 704; static PNG |
| `game/images/scene/chpt3/7.png` | 1,817,107 | 1262 × 710; static PNG |
| `game/images/scene/chpt3/8.png` | 1,770,465 | 1257 × 707; static PNG |
| `game/images/scene/chpt3/9.png` | 1,769,734 | 1264 × 707; static PNG |
| `game/images/scene/chpt4/1.png` | 1,541,920 | 1262 × 706; static PNG |
| `game/images/scene/chpt4/2.png` | 2,297,591 | 1671 × 941; static PNG |
| `game/images/scene/chpt4/3.png` | 2,225,906 | 1671 × 941; static PNG |
| `game/images/scene/chpt4/4.png` | 2,358,130 | 1536 × 1024; static PNG |
| `game/images/scene/chpt4/5.png` | 2,297,591 | 1671 × 941; static PNG |
| `game/images/scene/chpt4/6.png` | 2,190,882 | 1670 × 941; static PNG |
| `game/images/scene/chpt4/7.png` | 2,297,591 | 1671 × 941; static PNG |
| `game/images/scene/chpt5/1.png` | 2,864,150 | 1672 × 941; static PNG |
| `game/images/scene/chpt5/2.png` | 2,694,713 | 1672 × 941; static PNG |
| `game/images/scene/chpt5/3.png` | 1,880,338 | 1535 × 1024; static PNG |
| `game/images/scene/chpt5/4.png` | 2,348,688 | 1672 × 941; static PNG |
| `game/images/scene/chpt5/5.png` | 2,348,688 | 1672 × 941; static PNG |
| `game/images/scene/chpt5/6.png` | 2,428,017 | 1671 × 941; static PNG |
| `game/images/scene/chpt5/7.png` | 2,916,711 | 1672 × 941; static PNG |
| `game/images/scene/chpt5/8.png` | 2,297,591 | 1671 × 941; static PNG |
| `game/images/scene/chpt6/1.png` | 2,026,348 | 1672 × 941; static PNG |
| `game/images/scene/chpt6/2.png` | 2,150,001 | 1672 × 941; static PNG |
| `game/images/scene/chpt6/3.png` | 2,101,661 | 1672 × 941; static PNG |
| `game/images/scene/chpt6/4.png` | 2,150,001 | 1672 × 941; static PNG |
| `game/images/scene/chpt6/5.png` | 1,905,615 | 1672 × 941; static PNG |
| `game/images/scene/chpt6/6.png` | 2,071,331 | 1672 × 941; static PNG |
| `game/images/scene/chpt6/7.png` | 2,179,658 | 1672 × 941; static PNG |
| `game/images/scene/chpt6/8.png` | 2,035,321 | 1672 × 941; static PNG |
| `game/images/scene/chpt6/9.png` | 2,179,658 | 1672 × 941; static PNG |
| `game/images/scene/chpt7/1.png` | 2,327,081 | 1672 × 941; static PNG |
| `game/images/scene/chpt7/2.png` | 2,640,329 | 1671 × 941; static PNG |
| `game/images/scene/chpt7/3.png` | 2,190,882 | 1670 × 941; static PNG |
| `game/images/scene/chpt7/4.png` | 2,225,906 | 1671 × 941; static PNG |
| `game/images/scene/chpt7/5.png` | 3,286,376 | 1672 × 941; static PNG |
| `game/images/scene/chpt7/6.png` | 3,059,731 | 1672 × 941; static PNG |
| `game/images/scene/chpt7/7.png` | 2,297,591 | 1671 × 941; static PNG |
| `game/images/scene/chpt7/8.png` | 2,358,130 | 1536 × 1024; static PNG |
| `game/images/scene/chpt7/9.png` | 2,424,711 | 1672 × 941; static PNG |
| `game/images/scene/chpt8/1.png` | 2,468,983 | 1671 × 941; static PNG |
| `game/images/scene/chpt8/10.png` | 1,811,824 | 1672 × 941; static PNG |
| `game/images/scene/chpt8/11.png` | 2,312,984 | 1672 × 941; static PNG |
| `game/images/scene/chpt8/12.png` | 1,956,414 | 1670 × 941; static PNG |
| `game/images/scene/chpt8/13.png` | 2,312,984 | 1672 × 941; static PNG |
| `game/images/scene/chpt8/14.png` | 2,072,621 | 1672 × 941; static PNG |
| `game/images/scene/chpt8/15.png` | 2,240,885 | 1671 × 941; static PNG |
| `game/images/scene/chpt8/16.png` | 2,312,984 | 1672 × 941; static PNG |
| `game/images/scene/chpt8/17.png` | 1,811,824 | 1672 × 941; static PNG |
| `game/images/scene/chpt8/18.png` | 1,694,325 | 1672 × 941; static PNG |
| `game/images/scene/chpt8/19.png` | 2,312,984 | 1672 × 941; static PNG |
| `game/images/scene/chpt8/2.png` | 2,297,591 | 1671 × 941; static PNG |
| `game/images/scene/chpt8/20.png` | 1,956,414 | 1670 × 941; static PNG |
| `game/images/scene/chpt8/21.png` | 1,583,719 | 1671 × 941; static PNG |
| `game/images/scene/chpt8/3.png` | 2,225,906 | 1671 × 941; static PNG |
| `game/images/scene/chpt8/4.png` | 2,018,478 | 1671 × 941; static PNG |
| `game/images/scene/chpt8/5.png` | 2,190,882 | 1670 × 941; static PNG |
| `game/images/scene/chpt8/6.png` | 2,358,130 | 1536 × 1024; static PNG |
| `game/images/scene/chpt8/7.png` | 2,225,906 | 1671 × 941; static PNG |
| `game/images/scene/chpt8/8.png` | 2,161,249 | 1672 × 941; static PNG |
| `game/images/scene/chpt8/9.png` | 2,297,591 | 1671 × 941; static PNG |
| `game/images/scene/chpt9/1.png` | 2,081,698 | 1671 × 941; static PNG |
| `game/images/scene/chpt9/2.png` | 2,172,847 | 1670 × 941; static PNG |
| `game/images/scene/chpt9/3.png` | 2,124,953 | 1672 × 941; static PNG |
| `game/images/scene/chpt9/4.png` | 2,100,155 | 1672 × 941; static PNG |
| `game/images/scene/start/1.png` | 2,269,704 | 1671 × 941; static PNG |
| `game/images/scene/start/2.png` | 2,391,897 | 1672 × 941; static PNG |
| `game/images/scene/start/3.png` | 2,688,530 | 1672 × 941; static PNG |
| `game/images/scene/start/4.png` | 2,424,711 | 1672 × 941; static PNG |
| `game/images/scene/start/5.png` | 2,722,870 | 1672 × 941; static PNG |
| `game/images/scene/start/6.png` | 2,343,538 | 1672 × 941; static PNG |
| `game/images/scene/start/7.png` | 2,276,263 | 1671 × 941; static PNG |
| `game/images/scene/start/8.png` | 2,468,983 | 1671 × 941; static PNG |
| `game/images/scene/start/9.png` | 6,108 | 1920 × 1080; static PNG |
### game/audio

| File | Bytes | Dimensions / note |
| --- | ---: | --- |
| `game/audio/bg-music/ancient.mp3` | 7,128,179 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/bg-music/Beyond+the+Horizon.mp3` | 2,675,242 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/bg-music/Beyond+the+Red+Horizon.mp3` | 5,482,255 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/bg-music/dont-leave-me.mp3` | 4,296,923 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/bg-music/storm.mp3` | 6,497,060 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/bg-music/sunrise.mp3` | 4,734,108 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/bg-music/The+Quiet+Between+Stars.mp3` | 5,593,433 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt1/voice1.mp3` | 47,739 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt1/voice2.mp3` | 89,000 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt1/voice3.mp3` | 25,622 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt1/voice4.mp3` | 86,968 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt1/voice5.mp3` | 40,238 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt1/voice6.mp3` | 64,562 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt1/voice7.mp3` | 98,414 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt1/voice8.mp3` | 58,838 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt1/voice9.mp3` | 96,923 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt2/1.mp3` | 53,493 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt2/10.mp3` | 48,512 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt2/2.mp3` | 40,824 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt2/3.mp3` | 79,915 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt2/4.mp3` | 56,674 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt2/5.mp3` | 57,847 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt2/6.mp3` | 87,191 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt2/7.mp3` | 63,140 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt2/8.mp3` | 64,661 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt2/9.mp3` | 72,893 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt3/voice1.mp3` | 73,106 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt3/voice2.mp3` | 48,479 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt3/voice3.mp3` | 83,150 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt3/voice4.mp3` | 98,451 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt3/voice5.mp3` | 40,962 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt3/voice6.mp3` | 90,354 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt4/voice1.mp3` | 108,540 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt4/voice2.mp3` | 92,838 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt5/voice1.mp3` | 112,668 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt5/voice2.mp3` | 41,496 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt5/voice3.mp3` | 74,340 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt5/voice4.mp3` | 50,732 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt5/voice5.mp3` | 63,134 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt5/voice6.mp3` | 64,128 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt5/voice7.mp3` | 59,682 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt5/voice8.mp3` | 61,971 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt6/voice1.mp3` | 69,403 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt6/voice2.mp3` | 68,530 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt6/voice3.mp3` | 66,222 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt6/voice4.mp3` | 43,425 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt6/voice5.mp3` | 43,025 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt6/voice6.mp3` | 83,789 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt7/voice1.mp3` | 52,946 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt7/voice2.mp3` | 80,108 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt7/voice3.mp3` | 121,571 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt7/voice4.mp3` | 88,085 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt7/voice5.mp3` | 52,862 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt7/voice6.mp3` | 51,728 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt7/voice7.mp3` | 60,983 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt8/voice1.mp3` | 105,284 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt8/voice2.mp3` | 70,658 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt8/voice3.mp3` | 66,212 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt8/voice4.mp3` | 22,268 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt8/voice5.mp3` | 90,707 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt8/voice6.mp3` | 63,155 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt8/voice7.mp3` | 47,432 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt8/voice8.mp3` | 27,287 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt9/voice1.mp3` | 48,521 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt9/voice2.mp3` | 33,185 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt9/voice3.mp3` | 63,638 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt9/voice4.mp3` | 57,122 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/chpt9/voice5.mp3` | 84,521 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/epilogue/voice1.mp3` | 78,659 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/epilogue/voice2.mp3` | 134,207 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/epilogue/voice3.mp3` | 140,309 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/epilogue/voice4.mp3` | 60,257 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/epilogue/voice5.mp3` | 23,204 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/epilogue/voice6.mp3` | 93,146 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/epilogue/voice7.mp3` | 79,172 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/start/voice1.mp3` | 50,053 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/start/voice10.mp3` | 35,978 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/start/voice2.mp3` | 51,825 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/start/voice3.mp3` | 33,734 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/start/voice4.mp3` | 28,452 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/start/voice5.mp3` | 35,285 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/start/voice6.mp3` | 58,348 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/start/voice7.mp3` | 57,862 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/start/voice8.mp3` | 36,970 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/narrator/start/voice9.mp3` | 36,607 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
| `game/audio/sfx/Keyboard-Sound.mp3` | 198,076 | MP3; recognized MPEG frame header; sound quality UNVERIFIED |
### game/fonts

| File | Bytes | Dimensions / note |
| --- | ---: | --- |
| `game/fonts/font-sources.json` | 2,651 | Typography documentation / provenance |
| `game/fonts/README.md` | 2,801 | Typography documentation / provenance |
| `game/fonts/SourceSans3-Bold.ttf` | 428,176 | Bundled static TTF; manifest checksum verified |
| `game/fonts/SourceSans3-BoldIt.ttf` | 318,700 | Bundled static TTF; manifest checksum verified |
| `game/fonts/SourceSans3-It.ttf` | 315,812 | Bundled static TTF; manifest checksum verified |
| `game/fonts/SourceSans3-OFL.txt` | 4,486 | SIL OFL 1.1 notice; manifest checksum verified |
| `game/fonts/SourceSans3-Regular.ttf` | 431,196 | Bundled static TTF; manifest checksum verified |
| `game/fonts/SourceSans3-Semibold.ttf` | 425,904 | Bundled static TTF; manifest checksum verified |
| `game/fonts/SpaceGrotesk-Bold.ttf` | 116,056 | Bundled static TTF; manifest checksum verified |
| `game/fonts/SpaceGrotesk-Medium.ttf` | 116,664 | Bundled static TTF; manifest checksum verified |
| `game/fonts/SpaceGrotesk-OFL.txt` | 4,495 | SIL OFL 1.1 notice; manifest checksum verified |
### game/gui

| File | Bytes | Dimensions / note |
| --- | ---: | --- |
| `game/gui/bar/bottom.png` | 838 | 38 × 525; static PNG |
| `game/gui/bar/left.png` | 522 | 525 × 38; static PNG |
| `game/gui/bar/right.png` | 522 | 525 × 38; static PNG |
| `game/gui/bar/top.png` | 838 | 38 × 525; static PNG |
| `game/gui/bubble.png` | 6,886 | 200 × 155; static PNG |
| `game/gui/button/check_foreground.png` | 104 | 27 × 49; static PNG |
| `game/gui/button/check_selected_foreground.png` | 158 | 27 × 49; static PNG |
| `game/gui/button/choice_hover_background.png` | 1,751 | 1185 × 52; static PNG |
| `game/gui/button/choice_idle_background.png` | 1,777 | 1185 × 52; static PNG |
| `game/gui/button/hover_background.png` | 465 | 450 × 49; static PNG |
| `game/gui/button/idle_background.png` | 465 | 450 × 49; static PNG |
| `game/gui/button/quick_hover_background.png` | 198 | 150 × 45; static PNG |
| `game/gui/button/quick_idle_background.png` | 198 | 150 × 45; static PNG |
| `game/gui/button/radio_foreground.png` | 104 | 27 × 49; static PNG |
| `game/gui/button/radio_selected_foreground.png` | 158 | 27 × 49; static PNG |
| `game/gui/button/slot_hover_background.png` | 3,054 | 414 × 309; static PNG |
| `game/gui/button/slot_idle_background.png` | 2,989 | 414 × 309; static PNG |
| `game/gui/frame.png` | 7,255 | 900 × 375; static PNG |
| `game/gui/game_menu.png` | 38,669 | 1920 × 1080; static PNG |
| `game/gui/main_menu.png` | 38,669 | 1920 × 1080; static PNG |
| `game/gui/namebox.png` | 503 | 450 × 54; static PNG |
| `game/gui/notify.png` | 1,889 | 1383 × 64; static PNG |
| `game/gui/nvl.png` | 40,383 | 1920 × 1080; static PNG |
| `game/gui/overlay/confirm.png` | 38,668 | 1920 × 1080; static PNG |
| `game/gui/overlay/game_menu.png` | 39,462 | 1920 × 1080; static PNG |
| `game/gui/overlay/main_menu.png` | 39,525 | 1920 × 1080; static PNG |
| `game/gui/phone/bar/bottom.png` | 838 | 38 × 525; static PNG |
| `game/gui/phone/bar/left.png` | 522 | 525 × 38; static PNG |
| `game/gui/phone/bar/right.png` | 522 | 525 × 38; static PNG |
| `game/gui/phone/bar/top.png` | 838 | 38 × 525; static PNG |
| `game/gui/phone/button/check_foreground.png` | 111 | 27 × 64; static PNG |
| `game/gui/phone/button/check_selected_foreground.png` | 176 | 27 × 64; static PNG |
| `game/gui/phone/button/choice_hover_background.png` | 1,751 | 1185 × 52; static PNG |
| `game/gui/phone/button/choice_idle_background.png` | 1,777 | 1185 × 52; static PNG |
| `game/gui/phone/button/hover_background.png` | 583 | 450 × 64; static PNG |
| `game/gui/phone/button/idle_background.png` | 583 | 450 × 64; static PNG |
| `game/gui/phone/button/radio_foreground.png` | 111 | 27 × 64; static PNG |
| `game/gui/phone/button/radio_selected_foreground.png` | 176 | 27 × 64; static PNG |
| `game/gui/phone/button/slot_hover_background.png` | 3,054 | 414 × 309; static PNG |
| `game/gui/phone/button/slot_idle_background.png` | 2,989 | 414 × 309; static PNG |
| `game/gui/phone/nvl.png` | 38,668 | 1920 × 1080; static PNG |
| `game/gui/phone/overlay/game_menu.png` | 39,477 | 1920 × 1080; static PNG |
| `game/gui/phone/overlay/main_menu.png` | 39,624 | 1920 × 1080; static PNG |
| `game/gui/phone/scrollbar/horizontal_hover_bar.png` | 462 | 1050 × 18; static PNG |
| `game/gui/phone/scrollbar/horizontal_hover_thumb.png` | 465 | 1050 × 18; static PNG |
| `game/gui/phone/scrollbar/horizontal_idle_bar.png` | 464 | 1050 × 18; static PNG |
| `game/gui/phone/scrollbar/horizontal_idle_thumb.png` | 464 | 1050 × 18; static PNG |
| `game/gui/phone/scrollbar/vertical_hover_bar.png` | 803 | 18 × 1050; static PNG |
| `game/gui/phone/scrollbar/vertical_hover_thumb.png` | 805 | 18 × 1050; static PNG |
| `game/gui/phone/scrollbar/vertical_idle_bar.png` | 804 | 18 × 1050; static PNG |
| `game/gui/phone/scrollbar/vertical_idle_thumb.png` | 804 | 18 × 1050; static PNG |
| `game/gui/phone/slider/horizontal_hover_bar.png` | 702 | 525 × 54; static PNG |
| `game/gui/phone/slider/horizontal_hover_thumb.png` | 141 | 22 × 54; static PNG |
| `game/gui/phone/slider/horizontal_idle_bar.png` | 703 | 525 × 54; static PNG |
| `game/gui/phone/slider/horizontal_idle_thumb.png` | 140 | 22 × 54; static PNG |
| `game/gui/phone/slider/vertical_hover_bar.png` | 1,371 | 54 × 525; static PNG |
| `game/gui/phone/slider/vertical_hover_thumb.png` | 146 | 54 × 22; static PNG |
| `game/gui/phone/slider/vertical_idle_bar.png` | 1,373 | 54 × 525; static PNG |
| `game/gui/phone/slider/vertical_idle_thumb.png` | 145 | 54 × 22; static PNG |
| `game/gui/phone/textbox.png` | 13,292 | 1920 × 360; static PNG |
| `game/gui/scrollbar/horizontal_hover_bar.png` | 462 | 1050 × 18; static PNG |
| `game/gui/scrollbar/horizontal_hover_thumb.png` | 465 | 1050 × 18; static PNG |
| `game/gui/scrollbar/horizontal_idle_bar.png` | 464 | 1050 × 18; static PNG |
| `game/gui/scrollbar/horizontal_idle_thumb.png` | 464 | 1050 × 18; static PNG |
| `game/gui/scrollbar/vertical_hover_bar.png` | 803 | 18 × 1050; static PNG |
| `game/gui/scrollbar/vertical_hover_thumb.png` | 805 | 18 × 1050; static PNG |
| `game/gui/scrollbar/vertical_idle_bar.png` | 804 | 18 × 1050; static PNG |
| `game/gui/scrollbar/vertical_idle_thumb.png` | 804 | 18 × 1050; static PNG |
| `game/gui/skip.png` | 721 | 360 × 64; static PNG |
| `game/gui/slider/horizontal_hover_bar.png` | 521 | 525 × 38; static PNG |
| `game/gui/slider/horizontal_hover_thumb.png` | 114 | 15 × 38; static PNG |
| `game/gui/slider/horizontal_idle_bar.png` | 522 | 525 × 38; static PNG |
| `game/gui/slider/horizontal_idle_thumb.png` | 114 | 15 × 38; static PNG |
| `game/gui/slider/vertical_hover_bar.png` | 836 | 38 × 525; static PNG |
| `game/gui/slider/vertical_hover_thumb.png` | 111 | 38 × 15; static PNG |
| `game/gui/slider/vertical_idle_bar.png` | 838 | 38 × 525; static PNG |
| `game/gui/slider/vertical_idle_thumb.png` | 111 | 38 × 15; static PNG |
| `game/gui/textbox.png` | 10,916 | 1920 × 277; static PNG |
| `game/gui/thoughtbubble.png` | 4,215 | 200 × 133; static PNG |
| `game/gui/window_icon.png` | 18,037 | 250 × 250; static PNG |

Documentation snapshot only: README.md and GAME_POLISH_CHECKLIST.md created, this context replaced. Only those three Markdown files are authorized outputs; source, media, saves, branches and commits remain unchanged.
