# MER-B The Last Signal

# Character declarations

define narrator = Character("Narrator", color="#FF0000", callback=merb_keyboard_voice)
define oppy = Character("Opportunity", color="#CBE8FF", callback=merb_keyboard_voice)
define earth = Character("Earth", color="#86D7FF", callback=merb_keyboard_voice)
define mission = Character("Mission Control", color="#F9D57B", callback=merb_keyboard_voice)

define config.rollback_enabled = True

image opening_1 = Transform("images/scene/start/1.png", xysize=(1920, 1080))
image opening_2 = Transform("images/scene/start/2.png", xysize=(1920, 1080))
image opening_3 = Transform("images/scene/start/3.png", xysize=(1920, 1080))
image opening_4 = Transform("images/scene/start/4.png", xysize=(1920, 1080))
image opening_5 = Transform("images/scene/start/5.png", xysize=(1920, 1080))
image opening_6 = Transform("images/scene/start/6.png", xysize=(1920, 1080))
image opening_7 = Transform("images/scene/start/7.png", xysize=(1920, 1080))
image opening_8 = Transform("images/scene/start/8.png", xysize=(1920, 1080))
image opening_9 = Transform("images/scene/start/9.png", xysize=(1920, 1080))

image chapter1_1 = Transform("images/scene/chpt1/1.png", xysize=(1920, 1080))
image chapter1_2 = Transform("images/scene/chpt1/2.png", xysize=(1920, 1080))
image chapter1_3 = Transform("images/scene/chpt1/3.png", xysize=(1920, 1080))
image chapter1_4 = Transform("images/scene/chpt1/4.png", xysize=(1920, 1080))
image chapter1_5 = Transform("images/scene/chpt1/5.png", xysize=(1920, 1080))
image chapter1_6 = Transform("images/scene/chpt1/6.png", xysize=(1920, 1080))
image chapter1_7 = Transform("images/scene/chpt1/7.png", xysize=(1920, 1080))
image chapter1_8 = Transform("images/scene/chpt1/8.png", xysize=(1920, 1080))
image chapter1_9 = Transform("images/scene/chpt1/9.png", xysize=(1920, 1080))
image chapter1_10 = Transform("images/scene/chpt1/10.png", xysize=(1920, 1080))
image chapter1_11 = Transform("images/scene/chpt1/11.png", xysize=(1920, 1080))
image chapter1_12 = Transform("images/scene/chpt1/12.png", xysize=(1920, 1080))
image chapter1_13 = Transform("images/scene/chpt1/13.png", xysize=(1920, 1080))
image chapter1_14 = Transform("images/scene/chpt1/14.png", xysize=(1920, 1080))
image chapter1_15 = Transform("images/scene/chpt1/15.png", xysize=(1920, 1080))
image chapter1_16 = Transform("images/scene/chpt1/16.png", xysize=(1920, 1080))

image chapter2_1 = Transform("images/scene/chpt2/1.png", xysize=(1920, 1080))
image chapter2_2 = Transform("images/scene/chpt2/2.png", xysize=(1920, 1080))
image chapter2_3 = Transform("images/scene/chpt2/3.png", xysize=(1920, 1080))
image chapter2_4 = Transform("images/scene/chpt2/4.png", xysize=(1920, 1080))
image chapter2_5 = Transform("images/scene/chpt2/5.png", xysize=(1920, 1080))
image chapter2_6 = Transform("images/scene/chpt2/6.png", xysize=(1920, 1080))
image chapter2_7 = Transform("images/scene/chpt2/7.png", xysize=(1920, 1080))
image chapter2_8 = Transform("images/scene/chpt2/8.png", xysize=(1920, 1080))
image chapter2_9 = Transform("images/scene/chpt2/9.png", xysize=(1920, 1080))
image chapter2_10 = Transform("images/scene/chpt2/10.png", xysize=(1920, 1080))
image chapter2_11 = Transform("images/scene/chpt2/11.png", xysize=(1920, 1080))
image chapter2_12 = Transform("images/scene/chpt2/12.png", xysize=(1920, 1080))

image chapter3_1 = Transform("images/scene/chpt3/1.png", xysize=(1920, 1080))
image chapter3_2 = Transform("images/scene/chpt3/2.png", xysize=(1920, 1080))
image chapter3_3 = Transform("images/scene/chpt3/3.png", xysize=(1920, 1080))
image chapter3_4 = Transform("images/scene/chpt3/4.png", xysize=(1920, 1080))
image chapter3_5 = Transform("images/scene/chpt3/5.png", xysize=(1920, 1080))
image chapter3_6 = Transform("images/scene/chpt3/6.png", xysize=(1920, 1080))
image chapter3_7 = Transform("images/scene/chpt3/7.png", xysize=(1920, 1080))
image chapter3_8 = Transform("images/scene/chpt3/8.png", xysize=(1920, 1080))
image chapter3_9 = Transform("images/scene/chpt3/9.png", xysize=(1920, 1080))
image chapter3_10 = Transform("images/scene/chpt3/10.png", xysize=(1920, 1080))
image chapter3_11 = Transform("images/scene/chpt3/11.png", xysize=(1920, 1080))
image chapter3_12 = Transform("images/scene/chpt3/12.png", xysize=(1920, 1080))
image chapter3_13 = Transform("images/scene/chpt3/13.png", xysize=(1920, 1080))
image chapter3_14 = Transform("images/scene/chpt3/14.png", xysize=(1920, 1080))
image chapter3_15 = Transform("images/scene/chpt3/15.png", xysize=(1920, 1080))
image chapter4_1 = Transform("images/scene/chpt4/1.png", xysize=(1920, 1080))
image chapter4_2 = Transform("images/scene/chpt4/2.png", xysize=(1920, 1080))
image chapter4_3 = Transform("images/scene/chpt4/3.png", xysize=(1920, 1080))
image chapter4_4 = Transform("images/scene/chpt4/4.png", xysize=(1920, 1080))
image chapter4_5 = Transform("images/scene/chpt4/5.png", xysize=(1920, 1080))
image chapter4_6 = Transform("images/scene/chpt4/6.png", xysize=(1920, 1080))
image chapter4_7 = Transform("images/scene/chpt4/7.png", xysize=(1920, 1080))
image chapter5_1 = Transform("images/scene/chpt5/1.png", xysize=(1920, 1080))
image chapter5_2 = Transform("images/scene/chpt5/2.png", xysize=(1920, 1080))
image chapter5_3 = Transform("images/scene/chpt5/3.png", xysize=(1920, 1080))
image chapter5_4 = Transform("images/scene/chpt5/4.png", xysize=(1920, 1080))
image chapter5_5 = Transform("images/scene/chpt5/5.png", xysize=(1920, 1080))
image chapter5_6 = Transform("images/scene/chpt5/6.png", xysize=(1920, 1080))
image chapter5_7 = Transform("images/scene/chpt5/7.png", xysize=(1920, 1080))
image chapter5_8 = Transform("images/scene/chpt5/8.png", xysize=(1920, 1080))
image chapter6_1 = Transform("images/scene/chpt6/1.png", xysize=(1920, 1080))
image chapter6_2 = Transform("images/scene/chpt6/2.png", xysize=(1920, 1080))
image chapter6_3 = Transform("images/scene/chpt6/3.png", xysize=(1920, 1080))
image chapter6_4 = Transform("images/scene/chpt6/4.png", xysize=(1920, 1080))
image chapter6_5 = Transform("images/scene/chpt6/5.png", xysize=(1920, 1080))
image chapter6_6 = Transform("images/scene/chpt6/6.png", xysize=(1920, 1080))
image chapter6_7 = Transform("images/scene/chpt6/7.png", xysize=(1920, 1080))
image chapter6_8 = Transform("images/scene/chpt6/8.png", xysize=(1920, 1080))
image chapter6_9 = Transform("images/scene/chpt6/9.png", xysize=(1920, 1080))
image chapter7_1 = Transform("images/scene/chpt7/1.png", xysize=(1920, 1080))
image chapter7_2 = Transform("images/scene/chpt7/2.png", xysize=(1920, 1080))
image chapter7_3 = Transform("images/scene/chpt7/3.png", xysize=(1920, 1080))
image chapter7_4 = Transform("images/scene/chpt7/4.png", xysize=(1920, 1080))
image chapter7_5 = Transform("images/scene/chpt7/5.png", xysize=(1920, 1080))
image chapter7_6 = Transform("images/scene/chpt7/6.png", xysize=(1920, 1080))
image chapter7_7 = Transform("images/scene/chpt7/7.png", xysize=(1920, 1080))
image chapter7_8 = Transform("images/scene/chpt7/8.png", xysize=(1920, 1080))
image chapter7_9 = Transform("images/scene/chpt7/9.png", xysize=(1920, 1080))
image chapter8_1 = Transform("images/scene/chpt8/1.png", xysize=(1920, 1080))
image chapter8_2 = Transform("images/scene/chpt8/2.png", xysize=(1920, 1080))
image chapter8_3 = Transform("images/scene/chpt8/3.png", xysize=(1920, 1080))
image chapter8_4 = Transform("images/scene/chpt8/4.png", xysize=(1920, 1080))
image chapter8_5 = Transform("images/scene/chpt8/5.png", xysize=(1920, 1080))
image chapter8_6 = Transform("images/scene/chpt8/6.png", xysize=(1920, 1080))
image chapter8_7 = Transform("images/scene/chpt8/7.png", xysize=(1920, 1080))
image chapter8_8 = Transform("images/scene/chpt8/8.png", xysize=(1920, 1080))
image chapter8_9 = Transform("images/scene/chpt8/9.png", xysize=(1920, 1080))
image chapter8_10 = Transform("images/scene/chpt8/10.png", xysize=(1920, 1080))
image chapter8_11 = Transform("images/scene/chpt8/11.png", xysize=(1920, 1080))
image chapter8_12 = Transform("images/scene/chpt8/12.png", xysize=(1920, 1080))
image chapter8_13 = Transform("images/scene/chpt8/13.png", xysize=(1920, 1080))
image chapter8_14 = Transform("images/scene/chpt8/14.png", xysize=(1920, 1080))
image chapter8_15 = Transform("images/scene/chpt8/15.png", xysize=(1920, 1080))
image chapter8_16 = Transform("images/scene/chpt8/16.png", xysize=(1920, 1080))
image chapter8_17 = Transform("images/scene/chpt8/17.png", xysize=(1920, 1080))
image chapter8_18 = Transform("images/scene/chpt8/18.png", xysize=(1920, 1080))
image chapter8_19 = Transform("images/scene/chpt8/19.png", xysize=(1920, 1080))
image chapter8_20 = Transform("images/scene/chpt8/20.png", xysize=(1920, 1080))
image chapter8_21 = Transform("images/scene/chpt8/21.png", xysize=(1920, 1080))
image chapter9_1 = Transform("images/scene/chpt9/1.png", xysize=(1920, 1080))
image chapter9_2 = Transform("images/scene/chpt9/2.png", xysize=(1920, 1080))
image chapter9_3 = Transform("images/scene/chpt9/3.png", xysize=(1920, 1080))
image chapter9_4 = Transform("images/scene/chpt9/4.png", xysize=(1920, 1080))

image epilogue_1 = Transform("images/scene/epilogue/1.png", xysize=(1920, 1080))
image epilogue_2 = Transform("images/scene/epilogue/2.png", xysize=(1920, 1080))
image epilogue_3 = Transform("images/scene/epilogue/3.png", xysize=(1920, 1080))
image epilogue_4 = Transform("images/scene/epilogue/4.png", xysize=(1920, 1080))
image epilogue_5 = Transform("images/scene/epilogue/5.png", xysize=(1920, 1080))
image epilogue_6 = Transform("images/scene/epilogue/6.png", xysize=(1920, 1080))
image epilogue_7 = Transform("images/scene/epilogue/7.png", xysize=(1920, 1080))


# Opening-only presentation. The opaque, modal screen covers overlays without
# changing global quick-menu state, Say Screen styles, or chapter cards.
transform merb_opening_title_reveal:
    alpha 0.0
    zoom 0.99
    linear 1.2 alpha 1.0 zoom 1.0
    pause 2.2
    linear 0.8 alpha 0.0

screen merb_opening_title():
    modal True
    zorder 200

    add Solid("#010309")
    # A subtle gradient made from static native displayables; no new assets.
    for band in range(48):
        add Solid(Color("#010309").interpolate(Color("#081526"), band / 47.0)):
            xpos 0
            ypos int(config.screen_height * band / 48.0)
            xsize config.screen_width
            ysize int(config.screen_height / 48.0) + 1

    text "MER-B: The Last Signal":
        font "fonts/SpaceGrotesk-Medium.ttf"
        size 104
        color "#e7f0fa"
        xalign 0.5
        yalign 0.5
        textalign 0.5
        xmaximum config.screen_width - 160
        slow_cps False
        at merb_opening_title_reveal

    # Native manual dismissal/skip remain available; Auto does not drive this.
    timer (0.05 if renpy.is_skipping() else 4.4) action Return()
    key "dismiss" action Return()
    key "skip" action Return()
    key "toggle_skip" action Return()
    key "fast_skip" action Return()
    key "game_menu" action ShowMenu()


# Label parameters are dynamically scoped by Ren'Py: the player's existing
# quick_menu value is restored automatically on return, including rollback.
label merb_show_opening_title(quick_menu=False):
    window hide
    $ merb_keyboard_clear()
    scene expression Solid("#010309")
    with fade
    call screen merb_opening_title
    window auto
    return


label start:
    play music "audio/bg-music/The+Quiet+Between+Stars.mp3" fadein 2.0 loop volume merb_bgm_volume
    call merb_show_opening_title from merb_opening_title_return

    scene opening_1
    with dissolve

    voice "audio/narrator/start/voice1.mp3"
    narrator "Far away from everything we have ever called home..."
    voice "audio/narrator/start/voice2.mp3"
    narrator "On a world where no human has ever walked..."
    voice "audio/narrator/start/voice3.mp3"
    narrator "There is a little explorer."

    scene opening_2
    with dissolve

    voice "audio/narrator/start/voice4.mp3"
    narrator "It has six wheels."
    voice "audio/narrator/start/voice5.mp3"
    narrator "Two cameras that look almost like eyes."
    voice "audio/narrator/start/voice6.mp3"
    narrator "And a pair of solar panels that drink in the sunlight."

    scene opening_3
    with dissolve

    voice "audio/narrator/start/voice7.mp3"
    narrator "For nearly fifteen years, it has wandered across this world."

    scene opening_4
    with dissolve

    voice "audio/narrator/start/voice8.mp3"
    narrator "But today, the sunlight is fading."

    scene opening_5
    with dissolve

    oppy "That's strange..."
    oppy "It's getting dark already?"

    scene opening_6
    with dissolve

    oppy "Earth?"
    oppy "I think there's something wrong with the weather."

    scene opening_7
    with dissolve

    oppy "It's okay."
    oppy "We've been through storms before."
    oppy "I'll just save some power."
    oppy "And when the Sun comes back..."

    scene opening_8
    with dissolve

    narrator "...we can go exploring again."

    scene opening_9
    with dissolve

    voice "audio/narrator/start/voice9.mp3"
    narrator "But to understand this moment..."

    voice "audio/narrator/start/voice10.mp3"
    narrator "We must go back to where it all began."

    stop music fadeout 2.0
    call chapter_1
    call chapter_2
    call chapter_3
    call chapter_4
    call chapter_5
    call chapter_6
    call chapter_7
    call chapter_8
    call chapter_9
    call epilogue

    return


# A saved default keeps menus/loads on a chapter card cinematic as well.
default _merb_chapter_intro_active = False

label merb_chapter_intro(card_image):
    $ _merb_chapter_intro_active = True
    $ merb_keyboard_clear()
    stop voice
    $ renpy.stop_skipping()
    window hide

    scene black
    show expression Transform(card_image, xysize=(config.screen_width, config.screen_height), fit="contain", xalign=0.5, yalign=0.5) as merb_chapter_card
    with Fade(0.4, 0.0, 0.6)

    # No say/centered statement, auto-forward timer, or timed pause.
    call screen merb_chapter_intro_wait

    scene black
    with Dissolve(0.4)
    $ _merb_chapter_intro_active = False
    window auto
    return


label chapter_1:
    play music "audio/bg-music/Beyond+the+Horizon.mp3" fadein 2.0 loop volume merb_bgm_volume
    call merb_chapter_intro("images/ch/Slide1.PNG") from merb_chapter_intro_1

    scene chapter1_1
    with dissolve
    pause 3.0

    scene chapter1_2
    with dissolve
    voice "audio/narrator/chpt1/voice1.mp3"
    narrator "There was once a little robot. Its name was Opportunity."

    scene chapter1_3
    with dissolve
    voice "audio/narrator/chpt1/voice2.mp3"
    narrator "Its official designation was Mars Exploration Rover-B. But the people who built it had a shorter name."

    scene chapter1_4
    with dissolve
    voice "audio/narrator/chpt1/voice3.mp3"
    narrator "They called it Oppy."

    scene chapter1_5
    with dissolve
    voice "audio/narrator/chpt1/voice4.mp3"
    narrator "Opportunity wasn't built to fight. It wasn't built to conquer. It was built to answer a question."

    scene chapter1_6
    with dissolve
    voice "audio/narrator/chpt1/voice5.mp3"
    narrator "Long ago, was Mars a world of water?"
    voice "audio/narrator/chpt1/voice6.mp3"
    narrator "Could this cold, dusty planet once have been a place where life might survive?"

    scene chapter1_7
    with dissolve
    voice "audio/narrator/chpt1/voice7.mp3"
    narrator "To find out, humans built two explorers. Spirit... And Opportunity. They were twins, sent to opposite sides of Mars."

    scene chapter1_8
    with dissolve
    oppy "So... that's Mars?"

    scene chapter1_9
    with dissolve
    oppy "It looks pretty far away."

    scene chapter1_10
    with dissolve
    earth "It is. More than a hundred million kilometers away when you arrive."

    scene chapter1_11
    with dissolve
    oppy "That's a long way to travel. What will I find there?"

    scene chapter1_12
    with dissolve
    earth "We don't know yet. That's why we're sending you."

    scene chapter1_13
    with dissolve
    oppy "Oh. So... I'm supposed to find something nobody has seen before?"
    earth "Exactly."

    scene chapter1_14
    with dissolve
    oppy "Then I'll look really carefully. I promise."

    scene chapter1_15
    with dissolve
    voice "audio/narrator/chpt1/voice8.mp3"
    narrator "Opportunity was designed for a mission lasting just 90 Martian days."
    oppy "Ninety days? What happens after that?"
    earth "We'll see how far you can go."
    oppy "Then I'd better make every day count!"

    scene chapter1_16
    with dissolve
    voice "audio/narrator/chpt1/voice9.mp3"
    narrator "On July 7, 2003, Opportunity left Earth. It would never return. But its journey was only beginning."
    stop music fadeout 2.0
    return


label chapter_2:
    play music "audio/bg-music/Beyond+the+Red+Horizon.mp3" fadein 2.0 loop volume merb_bgm_volume
    call merb_chapter_intro("images/ch/Slide2.PNG") from merb_chapter_intro_2

    scene chapter2_1
    with dissolve
    voice "audio/narrator/chpt2/1.mp3"
    narrator "After nearly seven months in space, Opportunity reached Mars."
    voice "audio/narrator/chpt2/2.mp3"
    narrator "Landing was dangerous. There was no runway."
    voice "audio/narrator/chpt2/3.mp3"
    narrator "No one waiting below. Just a thin atmosphere, a parachute, rockets, and giant airbags."

    scene chapter2_2
    with dissolve
    oppy "Um... Earth?"

    scene chapter2_3
    with dissolve
    earth "We're here."

    scene chapter2_4
    with dissolve
    oppy "I think I'm falling!"

    scene chapter2_5
    with dissolve
    voice "audio/narrator/chpt2/4.mp3"
    narrator "The rover bounced across the surface before finally coming to rest."

    scene chapter2_6
    with dissolve
    oppy "...Did I make it?"
    voice "audio/narrator/chpt2/5.mp3"
    narrator "The lander petals opened. Opportunity saw Eagle Crater for the first time."

    scene chapter2_7
    with dissolve
    voice "audio/narrator/chpt2/6.mp3"
    narrator "All around it stretched a world of dust, rocks, and distant horizons. A world no human had ever touched."
    oppy "Oh... It's beautiful."

    scene chapter2_8
    with dissolve
    oppy "Hello, Mars. My name is Opportunity. I hope you don't mind if I look around."
    earth "We received your pictures. And they're wonderful."
    oppy "Really?"
    earth "Really. Welcome to Mars, Oppy."

    scene chapter2_9
    with dissolve
    narrator "The player chooses what Opportunity investigates first:"
    menu:
        "Look at the horizon.":
            voice "audio/narrator/chpt2/7.mp3"
            narrator "Opportunity takes a panoramic image and prepares to study the terrain."
        "Examine the rocks.":
            scene chapter2_10
            with dissolve
            voice "audio/narrator/chpt2/8.mp3"
            narrator "Opportunity inspects the exposed bedrock and begins the search for ancient water."
        "Look at the ground.":
            scene chapter2_11
            with dissolve
            voice "audio/narrator/chpt2/9.mp3"
            narrator "Opportunity studies the soil and the small round objects scattered across the landscape."

    scene chapter2_12
    with dissolve
    oppy "There's so much here! Where do I even begin?"
    earth "One step at a time."
    oppy "I have six wheels. Does that mean I can take six steps?"
    voice "audio/narrator/chpt2/10.mp3"
    narrator "And just like that, the little explorer began its journey."
    stop music fadeout 2.0
    return


label chapter_3:
    play music "audio/bg-music/ancient.mp3" fadein 2.0 loop volume merb_bgm_volume
    call merb_chapter_intro("images/ch/Slide3.PNG") from merb_chapter_intro_3

    scene chapter3_1
    with dissolve
    voice "audio/narrator/chpt3/voice1.mp3"
    narrator "Opportunity examined layered rock and discovered small round stones scattered across the ground."

    scene chapter3_2
    with dissolve
    oppy "Earth? I've found something strange."

    scene chapter3_3
    with dissolve
    earth "What have you got?"

    scene chapter3_4
    with dissolve
    oppy "Little round stones. They're everywhere! They look like tiny blueberries!"

    scene chapter3_5
    with dissolve
    voice "audio/narrator/chpt3/voice2.mp3"
    narrator "The scientists nicknamed them blueberries. They were not fruit."
    voice "audio/narrator/chpt3/voice3.mp3"
    narrator "They were small spheres containing hematite, an iron mineral formed in environments involving water."

    scene chapter3_6
    with dissolve
    voice "audio/narrator/chpt3/voice4.mp3"
    narrator "Opportunity's instruments studied minerals and sedimentary rock. Together, these clues revealed a world of ancient water."

    scene chapter3_7
    with dissolve
    oppy "Wait... Mars wasn't always like this?"

    scene chapter3_8
    with dissolve
    earth "No. Long ago, water affected these rocks."

    scene chapter3_9
    with dissolve
    oppy "Water? Like the oceans on Earth?"

    scene chapter3_10
    with dissolve
    earth "Not necessarily oceans here. But this place preserves evidence of ancient water."

    scene chapter3_11
    with dissolve
    oppy "So these rocks... They're telling us a story?"

    scene chapter3_12
    with dissolve
    earth "They are. And you're helping us read it."

    scene chapter3_13
    with dissolve
    oppy "Then I'll remember every little detail. Every rock. Every mark. Every clue."

    scene chapter3_14
    with dissolve
    voice "audio/narrator/chpt3/voice5.mp3"
    narrator "Opportunity did not discover living Martians."
    voice "audio/narrator/chpt3/voice6.mp3"
    narrator "It did not prove life had existed there. But it helped show that ancient Mars had environments shaped by liquid water."

    scene chapter3_15
    with dissolve
    oppy "Maybe I won't find anyone here. But I can help Earth learn who—or what—might have been here long ago."

    stop music fadeout 2.0
    return


label chapter_4:
    play music "audio/bg-music/sunrise.mp3" fadein 2.0 loop volume merb_bgm_volume
    call merb_chapter_intro("images/ch/Slide4.PNG") from merb_chapter_intro_4

    scene chapter4_1
    with dissolve
    voice "audio/narrator/chpt4/voice1.mp3"
    narrator "Time passed. Opportunity explored rocks and studied the landscape. Then one day, its original 90-sol mission came to an end."

    scene chapter4_2
    with dissolve
    oppy "Earth?"

    scene chapter4_3
    with dissolve
    earth "Yes, Oppy?"
    oppy "I think... I've finished my mission."

    scene chapter4_4
    with dissolve
    oppy "I did everything I could. Does that mean... I have to stop now?"

    scene chapter4_5
    with dissolve
    earth "Your systems are still working. And there is still so much to explore."

    scene chapter4_6
    with dissolve
    oppy "Wait... You mean I can keep going?"
    earth "Yes."

    scene chapter4_7
    with dissolve
    oppy "Really?!"
    earth "Really."
    oppy "Then... Just one more sunrise?"
    earth "One more sunrise."
    voice "audio/narrator/chpt4/voice2.mp3"
    narrator "It was supposed to be the end of a 90-day mission. Instead, it became the beginning of an extraordinary adventure."
    stop music fadeout 2.0
    return


label chapter_5:
    play music "audio/bg-music/dont-leave-me.mp3" fadein 2.0 loop volume merb_bgm_volume
    call merb_chapter_intro("images/ch/Slide5.PNG") from merb_chapter_intro_5

    scene chapter5_1
    with dissolve
    voice "audio/narrator/chpt5/voice1.mp3"
    narrator "Mars was beautiful. But Mars was also unforgiving. In April 2005, Opportunity drove into soft sand and sank."

    scene chapter5_2
    with dissolve
    oppy "Okay... Let's try moving forward."
    voice "audio/narrator/chpt5/voice2.mp3"
    narrator "The wheels spun. The rover barely moved."
    oppy "That's not good."

    scene chapter5_3
    with dissolve
    oppy "Earth? I think I need some help."
    voice "audio/narrator/chpt5/voice3.mp3"
    narrator "On Earth, engineers tested possible solutions using rover models and simulated Martian sand."
    voice "audio/narrator/chpt5/voice4.mp3"
    narrator "Every movement had to be planned carefully."

    menu:
        "Drive forward slowly.":
            scene chapter5_4
            with dissolve
            voice "audio/narrator/chpt5/voice5.mp3"
            narrator "Opportunity tries a careful recovery. The rover inches forward, then stops."
        "Back up and re-angle.":
            scene chapter5_5
            with dissolve
            voice "audio/narrator/chpt5/voice6.mp3"
            narrator "The rover shifts its weight and tries a safer angle. The sand groans beneath it."
        "Wait and scan the ground.":
            scene chapter5_6
            with dissolve
            voice "audio/narrator/chpt5/voice7.mp3"
            narrator "Opportunity gathers data and waits for Mission Control to find the best route."

    scene chapter5_7
    with dissolve
    voice "audio/narrator/chpt5/voice8.mp3"
    narrator "After more than five weeks of careful work, Opportunity escaped the sand."

    scene chapter5_8
    with dissolve
    oppy "I thought that sand was going to keep me forever!"
    earth "There's still a lot of Mars left to see."
    oppy "Then we'd better keep going. But maybe no more giant sand traps?"
    stop music fadeout 2.0
    return


label chapter_6:
    play music "audio/bg-music/storm.mp3" fadein 2.0 loop volume merb_bgm_volume
    call merb_chapter_intro("images/ch/Slide6.PNG") from merb_chapter_intro_6

    scene chapter6_1
    with dissolve
    voice "audio/narrator/chpt6/voice1.mp3"
    narrator "By 2007, Opportunity had traveled across the planet for more than three years."
    voice "audio/narrator/chpt6/voice2.mp3"
    narrator "Then the sky began to darken. A planet-wide dust storm spread across Mars."

    scene chapter6_2
    with dissolve
    oppy "Earth? Where did the sunlight go?"

    scene chapter6_3
    with dissolve
    earth "A major dust storm is blocking the Sun. We need to conserve your power."

    scene chapter6_4
    with dissolve
    oppy "Does that mean no exploring today?"

    scene chapter6_5
    with dissolve
    earth "Not today."

    scene chapter6_6
    with dissolve
    oppy "All right. I can wait."
    voice "audio/narrator/chpt6/voice3.mp3"
    narrator "The rover suspended its scientific activities. Its power dropped dangerously low."
    voice "audio/narrator/chpt6/voice4.mp3"
    narrator "For weeks, the team waited for the skies to clear."
    voice "audio/narrator/chpt6/voice5.mp3"
    narrator "Then a faint beam of sunlight broke through the dust."

    scene chapter6_7
    with dissolve
    oppy "Oh! There you are! I knew you'd come back, Sun."

    scene chapter6_8
    with dissolve
    earth "We've got more exploring to do, Oppy."

    scene chapter6_9
    with dissolve
    oppy "Just one more sunrise?"
    earth "One more sunrise."
    voice "audio/narrator/chpt6/voice6.mp3"
    narrator "Opportunity survived. And that memory of survival became part of its extraordinary story."
    stop music fadeout 2.0
    return


label chapter_7:
    play music "audio/bg-music/chapter7.mp3" fadein 2.0 loop volume merb_bgm_volume
    call merb_chapter_intro("images/ch/Slide7.PNG") from merb_chapter_intro_7

    scene chapter7_1
    with dissolve
    voice "audio/narrator/chpt7/voice1.mp3"
    narrator "The days became months. The months became years."
    voice "audio/narrator/chpt7/voice2.mp3"
    narrator "Opportunity crossed immense plains, studied crater walls, and followed the geological history of Mars."

    scene chapter7_2
    with dissolve
    voice "audio/narrator/chpt7/voice3.mp3"
    narrator "In 2011, it arrived at the rim of Endeavour Crater and found white veins of gypsum and clay minerals, evidence of ancient environments with water."

    scene chapter7_3
    with dissolve
    oppy "Earth? I think Mars is telling us an even bigger story."

    scene chapter7_4
    with dissolve
    earth "It is. And you found another piece of it."

    scene chapter7_5
    with dissolve
    oppy "Do you think people will remember all these places?"
    earth "Your pictures are already helping people understand a world they've never visited."

    scene chapter7_6
    with dissolve
    voice "audio/narrator/chpt7/voice4.mp3"
    narrator "Opportunity became the first rover to travel more than 42 kilometers on another world. And it kept going."

    scene chapter7_8
    with dissolve
    oppy "There's still something beautiful over there. Could we go a little farther?"

    scene chapter7_9
    with dissolve
    earth "We'll find a safe path."

    scene chapter7_7
    with dissolve
    voice "audio/narrator/chpt7/voice5.mp3"
    narrator "Children who were born when Opportunity landed were now teenagers."
    voice "audio/narrator/chpt7/voice6.mp3"
    narrator "Students who followed the mission were becoming scientists and engineers."
    voice "audio/narrator/chpt7/voice7.mp3"
    narrator "The little rover had spent almost an entire generation exploring another world."
    stop music fadeout 2.0
    return


label chapter_8:
    play music "audio/bg-music/chapter8.mp3" fadein 2.0 loop volume merb_bgm_volume
    call merb_chapter_intro("images/ch/Slide8.PNG") from merb_chapter_intro_8

    scene chapter8_1
    with dissolve
    voice "audio/narrator/chpt8/voice1.mp3"
    narrator "By June 2018, Opportunity had traveled 45.16 kilometers on Mars. It was exploring Perseverance Valley."
    voice "audio/narrator/chpt8/voice2.mp3"
    narrator "The name seemed fitting, because no one could have guessed how much perseverance this little machine would show."

    scene chapter8_2
    with dissolve
    oppy "Earth? Look at this place. It's beautiful. I think this might be one of my favorite views."

    scene chapter8_3
    with dissolve
    earth "We have more observations planned here."

    scene chapter8_4
    with dissolve
    oppy "Then let's get started!"
    voice "audio/narrator/chpt8/voice3.mp3"
    narrator "Then a dust cloud rolled across the sky. The sunlight began to fade."

    scene chapter8_5
    with dissolve
    oppy "Earth? My batteries aren't charging the way they should."

    scene chapter8_6
    with dissolve
    earth "A major dust storm is blocking the Sun. We need to conserve power."

    scene chapter8_7
    with dissolve
    oppy "Another storm?"

    scene chapter8_8
    with dissolve
    earth "Yes. A very large one."

    scene chapter8_9
    with dissolve
    oppy "All right. I can wait."

    scene chapter8_10
    with dissolve
    voice "audio/narrator/chpt8/voice4.mp3"
    narrator "The dust grew thicker."
    voice "audio/narrator/chpt8/voice5.mp3"
    narrator "Opportunity's systems were designed to conserve power, but this storm was more severe than the one it had survived in 2007."

    scene chapter8_11
    with dissolve
    oppy "I can't see the Sun anymore."

    scene chapter8_12
    with dissolve
    oppy "It must still be up there. Just hidden."

    scene chapter8_13
    with dissolve
    oppy "I'll take one more picture. Maybe Earth can tell me what the sky looks like."

    scene chapter8_14
    with dissolve
    voice "audio/narrator/chpt8/voice6.mp3"
    narrator "On June 10, 2018, Opportunity sent its final data to Earth."

    scene chapter8_15
    with dissolve
    oppy "Earth? Did you get my picture?"

    scene chapter8_16
    with dissolve
    oppy "I think I should save what power I have left."

    scene chapter8_17
    with dissolve
    oppy "We've done this before. Remember? The sky got dark. We waited. And the Sun came back."

    scene chapter8_18
    with dissolve
    oppy "So I'll wait again."

    scene chapter8_19
    with dissolve
    oppy "There's still so much I haven't seen. So many rocks. So many places to explore."
    oppy "And I still haven't shown Earth everything."

    scene chapter8_20
    with dissolve
    oppy "That's okay. It doesn't all have to happen today."
    oppy "I'll rest for a little while."

    scene chapter8_21
    with dissolve
    oppy "Just one more sunrise..."
    voice "audio/narrator/chpt8/voice7.mp3"
    narrator "...and then we can go a little farther."
    scene black
    with fade
    voice "audio/narrator/chpt8/voice8.mp3"
    narrator "The rover fell silent beneath the dust."
    stop music fadeout 2.0
    return


label chapter_9:
    play music "audio/bg-music/chapter9.mp3" fadein 2.0 loop volume (merb_bgm_volume * 0.3)
    call merb_chapter_intro("images/ch/Slide9.PNG") from merb_chapter_intro_9

    scene chapter9_1
    with dissolve
    voice "audio/narrator/chpt9/voice1.mp3"
    narrator "The next day came. Opportunity did not answer."
    mission "No response."

    scene chapter9_2
    with dissolve
    voice "audio/narrator/chpt9/voice2.mp3"
    narrator "But on Earth, they did not give up."
    voice "audio/narrator/chpt9/voice3.mp3"
    narrator "Engineers kept listening and sending commands, hoping to reach their little explorer."
    mission "Sending another command."

    scene chapter9_3
    with dissolve
    voice "audio/narrator/chpt9/voice4.mp3"
    narrator "More than a thousand commands were sent in the effort to restore contact."

    scene chapter9_4
    with dissolve
    mission "Attempting contact."
    mission "No signal."
    voice "audio/narrator/chpt9/voice5.mp3"
    narrator "On February 13, 2019, NASA officially declared Opportunity's mission complete."
    centered "{size=+18}MISSION COMPLETE{/size}\nFEBRUARY 13, 2019"
    stop music fadeout 2.0
    return


label epilogue:
    scene expression Solid("#d9c5a9")
    with fade
    centered "{size=+18}EPILOGUE{/size}\nYOU WERE NEVER FORGOTTEN"

    scene epilogue_1
    with dissolve
    voice "audio/narrator/epilogue/voice1.mp3"
    narrator "Opportunity was built to survive 90 Martian days. It explored Mars for nearly fifteen years."

    scene epilogue_2
    with dissolve
    voice "audio/narrator/epilogue/voice2.mp3"
    narrator "It traveled 45.16 kilometers. It studied ancient rocks. It found evidence of water. And it helped us understand that Mars had once been a very different world."

    scene epilogue_3
    with dissolve
    voice "audio/narrator/epilogue/voice3.mp3"
    narrator "It survived freezing nights, difficult terrain, broken components, and storms that nearly ended its journey. Every time it survived, it gave us another chance to discover something new."

    scene epilogue_4
    with dissolve
    voice "audio/narrator/epilogue/voice4.mp3"
    narrator "But there was one thing the little explorer could never do. It could never come home."

    scene epilogue_5
    with dissolve
    voice "audio/narrator/epilogue/voice5.mp3"
    narrator "It was never meant to."

    scene epilogue_6
    with dissolve
    voice "audio/narrator/epilogue/voice6.mp3"
    narrator "We gave it a name. Opportunity. We gave it six wheels. And ninety days. It gave us almost fifteen years."

    scene epilogue_7
    with dissolve
    voice "audio/narrator/epilogue/voice7.mp3"
    narrator "And somewhere on Mars, under the same sky it studied for so long, our little explorer remains."

    centered "{size=+12}To Opportunity — MER-B{/size}\nJanuary 25, 2004 – June 10, 2018\nDesigned for 90 Martian days.\nExplored for almost 15 years.\n45.16 kilometers traveled.\nOne extraordinary journey."

    narrator "Some explorers never return home. But their discoveries bring the universe closer to us."
    return
