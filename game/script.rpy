# MER-B The Last Signal

# Character declarations

define narrator = Character("Narrator", color="#E8E1D3", callback=merb_keyboard_voice)
define oppy = Character("Opportunity", color="#CBE8FF", callback=merb_keyboard_voice)
define earth = Character("Earth", color="#86D7FF", callback=merb_keyboard_voice)
define mission = Character("Mission Control", color="#F9D57B", callback=merb_keyboard_voice)

define config.rollback_enabled = False

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


label start:
    play music "audio/bg-music/The+Quiet+Between+Stars.mp3" fadein 2.0 loop
    scene expression Solid("#03070d")
    with fade

    centered "{size=+22}MER-B: The Last Signal{/size}"

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


label chapter_1:
    play music "audio/bg-music/Beyond+the+Horizon.mp3" fadein 2.0 loop
    scene expression Solid("#15202d")
    with fade
    centered "{size=+18}CHAPTER 1{/size}\nA LITTLE ROBOT WITH A BIG DREAM"

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
    play music "audio/bg-music/Beyond+the+Red+Horizon.mp3" fadein 2.0 loop
    scene expression Solid("#8b452d")
    with fade
    centered "{size=+18}CHAPTER 2{/size}\nHELLO, MARS"

    scene chapter2_1
    with dissolve
    narrator "After nearly seven months in space, Opportunity reached Mars. Landing was dangerous. There was no runway. No one waiting below. Just a thin atmosphere, a parachute, rockets, and giant airbags."

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
    narrator "The rover bounced across the surface before finally coming to rest."

    scene chapter2_6
    with dissolve
    oppy "...Did I make it?"
    narrator "The lander petals opened. Opportunity saw Eagle Crater for the first time."

    scene chapter2_7
    with dissolve
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
            narrator "Opportunity takes a panoramic image and prepares to study the terrain."
        "Examine the rocks.":
            scene chapter2_10
            with dissolve
            narrator "Opportunity inspects the exposed bedrock and begins the search for ancient water."
        "Look at the ground.":
            scene chapter2_11
            with dissolve
            narrator "Opportunity studies the soil and the small round objects scattered across the landscape."

    scene chapter2_12
    with dissolve
    oppy "There's so much here! Where do I even begin?"
    earth "One step at a time."
    oppy "I have six wheels. Does that mean I can take six steps?"
    narrator "And just like that, the little explorer began its journey."
    stop music fadeout 2.0
    return


label chapter_3:
    scene expression Solid("#6f3828")
    with fade
    centered "{size=+18}CHAPTER 3{/size}\nTHE MEMORY OF WATER"

    scene chapter3_1
    with dissolve
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
    narrator "The scientists nicknamed them blueberries. They were not fruit. They were small spheres containing hematite, an iron mineral formed in environments involving water."

    scene chapter3_6
    with dissolve
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
    narrator "Opportunity did not discover living Martians. It did not prove life had existed there. But it helped show that ancient Mars had environments shaped by liquid water."

    scene chapter3_15
    with dissolve
    oppy "Maybe I won't find anyone here. But I can help Earth learn who—or what—might have been here long ago."

    return


label chapter_4:
    scene expression Solid("#3d4e5c")
    with fade
    centered "{size=+18}CHAPTER 4{/size}\nTHE NINETIETH SUNRISE"

    scene chapter4_1
    with dissolve
    narrator "Time passed. Opportunity explored rocks and studied the landscape. Then one day, its original 90-sol mission came to an end."

    oppy "Earth?"
    earth "Yes, Oppy?"
    oppy "I think... I've finished my mission."
    oppy "I did everything I could. Does that mean... I have to stop now?"
    earth "Your systems are still working. And there is still so much to explore."
    oppy "Wait... You mean I can keep going?"
    earth "Yes."
    oppy "Really?!"
    earth "Really."
    oppy "Then... Just one more sunrise?"
    earth "One more sunrise."
    narrator "It was supposed to be the end of a 90-day mission. Instead, it became the beginning of an extraordinary adventure."
    return


label chapter_5:
    scene expression Solid("#553d2c")
    with fade
    centered "{size=+18}CHAPTER 5{/size}\nPLEASE DON'T LEAVE ME HERE"

    narrator "Mars was beautiful. But Mars was also unforgiving. In April 2005, Opportunity drove into soft sand and sank."
    oppy "Okay... Let's try moving forward."
    narrator "The wheels spun. The rover barely moved."
    oppy "That's not good."
    oppy "Earth? I think I need some help."
    narrator "On Earth, engineers tested possible solutions using rover models and simulated Martian sand. Every movement had to be planned carefully."

    menu:
        "Drive forward slowly.":
            narrator "Opportunity tries a careful recovery. The rover inches forward, then stops."
        "Back up and re-angle.":
            narrator "The rover shifts its weight and tries a safer angle. The sand groans beneath it."
        "Wait and scan the ground.":
            narrator "Opportunity gathers data and waits for Mission Control to find the best route."

    narrator "After more than five weeks of careful work, Opportunity escaped the sand."
    oppy "I thought that sand was going to keep me forever!"
    earth "There's still a lot of Mars left to see."
    oppy "Then we'd better keep going. But maybe no more giant sand traps?"
    return


label chapter_6:
    scene expression Solid("#1f2a2f")
    with fade
    centered "{size=+18}CHAPTER 6{/size}\nTHE STORM WE SURVIVED"

    narrator "By 2007, Opportunity had traveled across the planet for more than three years. Then the sky began to darken. A planet-wide dust storm spread across Mars."
    oppy "Earth? Where did the sunlight go?"
    earth "A major dust storm is blocking the Sun. We need to conserve your power."
    oppy "Does that mean no exploring today?"
    earth "Not today."
    oppy "All right. I can wait."
    narrator "The rover suspended its scientific activities. Its power dropped dangerously low. For weeks, the team waited for the skies to clear."
    narrator "Then a faint beam of sunlight broke through the dust."
    oppy "Oh! There you are! I knew you'd come back, Sun."
    earth "We've got more exploring to do, Oppy."
    oppy "Just one more sunrise?"
    earth "One more sunrise."
    narrator "Opportunity survived. And that memory of survival became part of its extraordinary story."
    return


label chapter_7:
    scene expression Solid("#4c2d20")
    with fade
    centered "{size=+18}CHAPTER 7{/size}\nTHE WORLD KEEPS GETTING BIGGER"

    narrator "The days became months. The months became years. Opportunity crossed immense plains, studied crater walls, and followed the geological history of Mars."
    narrator "In 2011, it arrived at the rim of Endeavour Crater and found white veins of gypsum and clay minerals, evidence of ancient environments with water."
    oppy "Earth? I think Mars is telling us an even bigger story."
    earth "It is. And you found another piece of it."
    oppy "Do you think people will remember all these places?"
    earth "Your pictures are already helping people understand a world they've never visited."
    narrator "Opportunity became the first rover to travel more than 42 kilometers on another world. And it kept going."
    oppy "There's still something beautiful over there. Could we go a little farther?"
    earth "We'll find a safe path."
    narrator "Children who were born when Opportunity landed were now teenagers. Students who followed the mission were becoming scientists and engineers. The little rover had spent almost an entire generation exploring another world."
    return


label chapter_8:
    scene expression Solid("#0d0e11")
    with fade
    centered "{size=+18}CHAPTER 8{/size}\nWHEN THE SUN DISAPPEARED"

    narrator "By June 2018, Opportunity had traveled 45.16 kilometers on Mars. It was exploring Perseverance Valley. The name seemed fitting, because no one could have guessed how much perseverance this little machine would show."
    oppy "Earth? Look at this place. It's beautiful. I think this might be one of my favorite views."
    earth "We have more observations planned here."
    oppy "Then let's get started!"
    narrator "Then a dust cloud rolled across the sky. The sunlight began to fade."
    oppy "Earth? My batteries aren't charging the way they should."
    earth "A major dust storm is blocking the Sun. We need to conserve power."
    oppy "Another storm?"
    earth "Yes. A very large one."
    oppy "All right. I can wait."
    narrator "The dust grew thicker. Opportunity's systems were designed to conserve power, but this storm was more severe than the one it had survived in 2007."
    oppy "I can't see the Sun anymore."
    oppy "It must still be up there. Just hidden."
    oppy "I'll take one more picture. Maybe Earth can tell me what the sky looks like."
    narrator "On June 10, 2018, Opportunity sent its final data to Earth."
    oppy "Earth? Did you get my picture?"
    oppy "I think I should save what power I have left."
    oppy "We've done this before. Remember? The sky got dark. We waited. And the Sun came back."
    oppy "So I'll wait again."
    oppy "There's still so much I haven't seen. So many rocks. So many places to explore."
    oppy "And I still haven't shown Earth everything."
    oppy "That's okay. It doesn't all have to happen today."
    oppy "I'll rest for a little while."
    oppy "Just one more sunrise..."
    narrator "...and then we can go a little farther."
    scene black
    with fade
    narrator "The rover fell silent beneath the dust."
    return


label chapter_9:
    scene expression Solid("#141719")
    with fade
    centered "{size=+18}CHAPTER 9{/size}\nEARTH IS STILL CALLING"

    narrator "The next day came. Opportunity did not answer."
    mission "No response."
    narrator "But on Earth, they did not give up. Engineers kept listening and sending commands, hoping to reach their little explorer."
    mission "Sending another command."
    narrator "More than a thousand commands were sent in the effort to restore contact."
    mission "Attempting contact."
    mission "No signal."
    narrator "On February 13, 2019, NASA officially declared Opportunity's mission complete."
    centered "{size=+18}MISSION COMPLETE{/size}\nFEBRUARY 13, 2019"
    return


label epilogue:
    scene expression Solid("#d9c5a9")
    with fade
    centered "{size=+18}EPILOGUE{/size}\nYOU WERE NEVER FORGOTTEN"

    narrator "Opportunity was built to survive 90 Martian days. It explored Mars for nearly fifteen years."
    narrator "It traveled 45.16 kilometers. It studied ancient rocks. It found evidence of water. And it helped us understand that Mars had once been a very different world."
    narrator "It survived freezing nights, difficult terrain, broken components, and storms that nearly ended its journey. Every time it survived, it gave us another chance to discover something new."
    narrator "But there was one thing the little explorer could never do. It could never come home."
    narrator "It was never meant to."
    narrator "We gave it a name. Opportunity. We gave it six wheels. And ninety days. It gave us almost fifteen years."
    narrator "And somewhere on Mars, under the same sky it studied for so long, our little explorer remains."

    centered "{size=+12}To Opportunity — MER-B{/size}\nJanuary 25, 2004 – June 10, 2018\nDesigned for 90 Martian days.\nExplored for almost 15 years.\n45.16 kilometers traveled.\nOne extraordinary journey."

    narrator "Some explorers never return home. But their discoveries bring the universe closer to us."
    return
