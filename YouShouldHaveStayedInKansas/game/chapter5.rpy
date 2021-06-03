# Chapter 5

label chapter05:

    scene scarecrowApartment
    with dissolve

    "CHAPTER 5: Scarecrow's Apartment - night"

    play music "audio/forest.mp3" loop fadein 2.0 volume 0.5

    "Papers and Newspaper clippings are scattered everywhere. There is stuff written on the walls, connected together with string."

    "On the bookshelf is an assortment of books and jars full of...something. Food? Experiments? Food that became an experiment after it spoiled? Who knows."

    "The door slams open, and you and Scarecrow enter the scene, Scarecrow looking more energetic than anyone has ever seen him."

    "You look around the room in a mix of wonder and disgust."

    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "Make yourself at home!"

    show ScarecrowPlaceholder at left
    show dorothyPlaceholder at right
    with dissolve

    dorothy "Uh..."

    "You eye the mess around your feet."

    scarecrow "Good choice!"

    "He grabs an old-looking chalkboard and writes {u}EVIDENCE{/u} at the top"

    scarecrow "So! What do we know?"

    hide ScarecrowPlaceholder
    show dorothyPlaceholder at center
    with dissolve

label CH5choice1:
menu evidenceMenu:
    "This menu depends on what you have managed to collect and what you haven’t. This will reappear until you decide to \"Move on\" from talking about the evidence."

    "Pick photo of Red Shoes" if hasCollectedRedShoesPhoto:
        jump CH5choiceA

    "Pick Lion's Testimony" if hasListenedToLionsTestimony:
        jump CH5choiceB

    "Pick Camera" if hasCollectedCamera:
        jump CH5choiceC

    "Pick Tape" if didYouGiveScarecrowTape:
        jump CH5choiceD

    "Pick Note" if hasCollectedTinManNote:
        jump CH5choiceE

    "Move on":
        jump CH5moveON

label CH5choiceA:

    hide dorothyPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "Ah, the photo at the W.W. West's mansion! She seemed to have stolen it from the evidence room, suspicious, isn’t it?"

    hide ScarecrowPlaceholder
    show dorothyPlaceholder at center
    with dissolve

menu chA01:
    "What will be your response?"

    "I mean, we’ve also stolen stuff from the evidence room…":
        hide dorothyPlaceholder
        show ScarecrowPlaceholder
        with dissolve

        scarecrow "Details!"

        jump CH5chA01cont

    "Suspicious! Yep, super suspicious!":
        hide dorothyPlaceholder
        show ScarecrowPlaceholder
        with dissolve

        scarecrow "ISN'T IT?"

        jump CH5chA01cont

label CH5chA01cont:
    scarecrow "But what is the significance of these shoes...and why were they missing from the crime scene?"

    hide ScarecrowPlaceholder
    show dorothyPlaceholder
    with dissolve

menu chA02:
    "What will be your response?"

    "These shoes could be the reason why she died.":

        hide dorothyPlaceholder
        show ScarecrowPlaceholder
        with dissolve

        scarecrow "A motive? Those do look like very fancy shoes...and the photo clearly shows a secret compartment."

        scarecrow "Maybe there was something important hidden in those shoes!"

        hide ScarecrowPlaceholder
        show dorothyPlaceholder
        with dissolve

        dorothy "Yeah, and the murderer took them off her cooling corpse!"

        hide dorothyPlaceholder
        show ScarecrowPlaceholder
        with dissolve

        scarecrow "{i}sounding delighted{\i} How morbid!"

        if hasListenedInOnWitchCh4:
            hide ScarecrowPlaceholder
            show dorothyPlaceholder
            with dissolve

            dorothy "The shoes are also a family heirloom."
        
        hide ScarecrowPlaceholder
        show dorothyPlaceholder at center
        with dissolve

        jump CH5choice1

    "Maybe they’re a red herring, haha get it?":
        hide dorothyPlaceholder
        show ScarecrowPlaceholder
        with dissolve

        scarecrow "That was horrible…(sniff) I’m so proud…"

        hide ScarecrowPlaceholder
        show dorothyPlaceholder at center
        with dissolve

        jump CH5choice1

label CH5choiceB:

    hide dorothyPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "The lion said there was someone in a heated argument with the victim before the murder. The lion said he heard...huh, I can’t remember."

    if hasCollectedRedShoesPhoto:
        hide ScarecrowPlaceholder
        show dorothyPlaceholder at center
        with dissolve

        dorothy "That they wanted the shoes."

        hide dorothyPlaceholder
        show ScarecrowPlaceholder at center
        with dissolve

        scarecrow "Right! The shoes from the photo! The ones missing from the crime scene!"
    else:
        hide ScarecrowPlaceholder
        show dorothyPlaceholder at center
        with dissolve

        dorothy "Something about...shoes?"

        hide dorothyPlaceholder
        show ScarecrowPlaceholder at center
        with dissolve

        scarecrow "Shoes...now why would that stranger say anything about shoes?"

    hide dorothyPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "The Lion seemed very convinced that the one arguing with the witch before her death was the murderer. "
    
    scarecrow "Unless HE’s the murderer and trying to pin it on someone else."
    
    "You both look at each other."

    hide ScarecrowPlaceholder
    show dorothyPlaceholder at center
    with dissolve

    dorothy "Nah!"
    
    hide dorothyPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve
    
    scarecrow "No way!" # dorothy and scarecrow says this together but I don't want to do more work

    hide ScarecrowPlaceholder
    show dorothyPlaceholder at center
    with dissolve

    dorothy "So the mysterious stranger with the scary eyes did it? Helpful."

    hide dorothyPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "Well, how many people in London have scary eyes?"

    hide ScarecrowPlaceholder
    show dorothyPlaceholder at center
    with dissolve

    dorothy "{i}Glares{\i}"

    hide dorothyPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "{i}jokingly{\i} Actually, who says you’re not the murderer?"

    hide ScarecrowPlaceholder

    "{i}awkward silence{\i}"

    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "Anyway!"

    hide ScarecrowPlaceholder
    show dorothyPlaceholder at center
    with dissolve

    jump CH5choice1

label CH5choiceC:
    hide dorothyPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "Ah, the camera found at the crime scene! The CLUE TO EVERYTHING!"

    hide ScarecrowPlaceholder
    show dorothyPlaceholder at center
    with dissolve

    dorothy "Is it?"

    hide dorothyPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "I don’t know, might be!"

    scarecrow "The question remains...whose camera is it? I can take fingerprints, see if they’re in any database…"

    hide ScarecrowPlaceholder
    show dorothySad at center
    with dissolve

    dorothy "Maybe it’s just some innocent passerby’s, who didn’t want to get roped into any of this."
    dorothy "Maybe they lost it at the worst opportune moment, and are regretting they ever came to this city..."
    dorothy "...and they're wondering if they’re gonna be the number one suspect through sheer dumb luck."

    hide dorothySad
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "That’s...a very specific hypothetical."

    hide ScarecrowPlaceholder
    show dorothyPlaceholder at center
    with dissolve

    dorothy "Well, what do you think?!"

    hide dorothyPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "I think…"

    if doYouSuspectYourself:
        scarecrow "That this camera might be the murder weapon."
    else:
        scarecrow "That this camera probably doesn’t matter."

    hide ScarecrowPlaceholder
    show dorothyPlaceholder at center
    with dissolve

    jump CH5choice1

label CH5choiceD:
    hide dorothyPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "This tape we got from the evidence room..."

    scarecrow "It was probably in the camera we found. Though I guess the tape doesn’t matter as much as what’s on it, doesn’t it?"

    scarecrow "We need to develop it!"

    hide ScarecrowPlaceholder
    if doYouSuspectYourself:
        show dorothySad at center
    else:
        show dorothyPlaceholder at center
    with dissolve

    dorothy "Yes, I guess we do."

    show ScarecrowPlaceholder at left
    with dissolve

    scarecrow "It will take me tonight, so we’ll find out in the morning. I do hope it’s something relevant. I’m glad you found it, Dorothy."

    hide ScarecrowPlaceholder

    if doYouSuspectYourself:
        dorothy "sure."
    else:
        dorothy "We need to find out what’s on that tape!"

    jump CH5choice1

label CH5choiceE:
    hide dorothyPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "The note the Tin Man gave us...seemingly for free."

    hide ScarecrowPlaceholder
    show dorothyPlaceholder at center
    with dissolve

    dorothy "Yeah, that was weird."

    hide dorothyPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "Anyway! It said something like 'bottom, heirloom, hold down'. The handwriting might give away the author."

    hide ScarecrowPlaceholder
    show dorothyPlaceholder at center
    with dissolve

    dorothy "I mean...what are we gonna do, ask everyone in London to write their names?"

    hide dorothyPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "An admirable effort! But we’re definitely not doing that!"

    hide ScarecrowPlaceholder
    show dorothyPlaceholder at center
    with dissolve

    jump CH5choice1

label CH5moveON:

    if doYouSuspectYourself:
        hide dorothyPlaceholder
        show dorothySad
        dorothy "..."

        hide dorothySad
        show ScarecrowSad at center
        with dissolve

        stop music fadeout 1.0
        scarecrow "Hey, listen…I know it seems pointless, you know?"

        hide ScarecrowSad
        show dorothySad at center
        with dissolve

        dorothy "..."

        hide dorothySad
        show ScarecrowSad at center
        with dissolve

        scarecrow "I used to think I couldn’t figure out anything. I was...kind of the idiot, you know?"
    else:
        dorothy "Man, this is a lot of evidence."

        hide dorothyPlaceholder
        show ScarecrowPlaceholder at center
        with dissolve

        scarecrow "Yeah. But that’s good! We’re getting somewhere!"

        hide ScarecrowPlaceholder
        show dorothyPlaceholder at center
        with dissolve

        dorothy "Hey, Scarecrow?"

        hide dorothyPlaceholder
        show ScarecrowPlaceholder at center
        with dissolve

        scarecrow "What’s up?"

        hide ScarecrowPlaceholder
        show dorothyPlaceholder at center
        with dissolve

        dorothy "If you had to pick...between helping a friend and finding the truth, what would you pick?"

        hide dorothyPlaceholder
        show ScarecrowPlaceholder at center
        with dissolve

        scarecrow "The truth, obviously."

        hide ScarecrowPlaceholder
        show dorothySad at center
        with dissolve

        dorothy "Right."

        hide dorothySad
        show ScarecrowPlaceholder at center
        with dissolve

        scarecrow "That is a very strange question, Dorothy."

        hide ScarecrowPlaceholder
        show dorothyPlaceholder at center
        with dissolve

        dorothy "Yeah?"

        hide dorothyPlaceholder
        show ScarecrowPlaceholder at center
        with dissolve

        scarecrow "I mean, if two people are friends, hypothetically speaking, they would not hinder each other from the truth, wouldn’t they?"
        scarecrow "Friends don’t lie to each other."

        hide ScarecrowPlaceholder
        show dorothySad at center
        with dissolve

        "You are both silent for a moment."
        "You want to tell Scarecrow you were at the tower that day, that it was your camera, but something’s holding you back. Fear, probably."
        "You don’t know anyone in this city."
        "You didn’t know anyone until today."

        hide dorothySad
        show ScarecrowPlaceholder at center
        with dissolve

        stop music fadeout 1.0
        scarecrow "I’M NOT A REAL DETECTIVE!"

        scarecrow "Few, that felt good to get off my chest."

        hide ScarecrowPlaceholder
        show ScarecrowSad at center

        scarecrow "I wanted to be! But I used to think I couldn’t figure out anything. I was...kind of the idiot, you know?"
    
    play music "audio/peacefulsong.mp3" loop fadein 2.0 volume 0.5

    scarecrow "In school, and after, I...wasn’t really good at a lot of things."
    scarecrow "Every chance I got, he rejected me from the academy because I always got in the way with my silly ideas."
    scarecrow "Scarecrow the brainless, that’s what they all called me."
    scarecrow "Before I met you, I thought of, y’know, giving up. I wasn’t good at anything, why would I think I’d be good at this? {i}he gestures at the chalkboard{/i}"
    scarecrow "But then, you showed up, and you seemed so eager to figure it out with me, I thought maybe...I wasn’t all that bad after all."
    scarecrow "If this one kid follows me, maybe I’m actually good. At being a detective."
    scarecrow "So. Thanks, I guess. It’s been...really fun."

    hide ScarecrowSad
    show dorothyPlaceholder at center
    with dissolve

menu dorothychoice:
    "Your choice"

    "Say nothing.":
        jump CH5saynothing

    "Comfort Scarecrow.":
        jump CH5comfort

label CH5saynothing:
    
    hide dorothyPlaceholder
    show dorothySad at center
    dorothy "..."

    hide dorothySad
    show ScarecrowSad at center
    with dissolve

    scarecrow "But you don’t look that eager now. Maybe I am the idiot, huh? Running us in circles? I get it."

    "He gestures toward the door."

    scarecrow "You should go home. Your parents are probably looking for you."

    hide ScarecrowSad
    show dorothySad at center
    with dissolve

    dorothy "...Yeah, I guess you’re right."

    "You turn to leave. As you walk out the door, Scarecrow calls out."

    hide dorothySad
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "Wait!"

    "You pause."

    scarecrow "I..."

    scarecrow "Nevermind. Be safe."

    hide ScarecrowPlaceholder
    show dorothyPlaceholder at center
    with dissolve

    dorothy "...I will"

    jump CH5bridgescene

label CH5comfort:
    dorothy "You’re not stupid, you know."

    hide dorothyPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "Thanks."

    hide ScarecrowPlaceholder
    show dorothyPlaceholder at center
    with dissolve

    dorothy "Okay, you make stupid decisions...sometimes. A lot of the time. All the time."

    dorothy "But. You’re good at figuring things out. And better than that, you care. Not a lot of people care as much as you do, you know? About finding the truth."

    hide dorothyPlaceholder
    show ScarecrowSad

    "Scarecrow looks at the board of clues. He fidgets with the chalk."

    hide ScarecrowSad
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "Thanks, I guess. Maybe you're-"

    hide ScarecrowPlaceholder
    show dorothyFunny at center
    with dissolve

    dorothy "I'm right."

    "Scarecrow laughs."

    hide dorothyFunny
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "Maybe I'm not brainless after all."

    scarecrow "I think this story is all coming together. I just need...another night."
    
    if didYouGiveScarecrowTape:
        scarecrow "...plus we need to develop that tape. Give me until tomorrow morning, all right?"

    hide ScarecrowPlaceholder
    show dorothyPlaceholder at center
    with dissolve

    dorothy "Sure. I should be getting home anyway."

    hide dorothyPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "Hey, Dorothy?"

    hide ScarecrowPlaceholder
    show dorothyPlaceholder at center
    with dissolve

    dorothy "Yeah?"

    hide dorothyPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "Be safe."

    hide ScarecrowPlaceholder
    show dorothyPlaceholder at center
    with dissolve

    dorothy "I will."

label CH5bridgescene:

    stop music fadeout 1.0

    scene londonBridge
    with dissolve

    play music "audio/despair syndrome quiet.mp3" loop volume 0.3

    "You stand outside at nighttime. You're crossing the London Bridge when you see a tall, dark figure in your path. The fog is too thick for you to see clearly."

    show dorothyPlaceholder at center
    with dissolve

    dorothy "Hello?"

    hide dorothyPlaceholder
    show wwWestAngry at center
    with dissolve

    wwwest "You."

    "W. W. West steps out of the fog. She looks like she hasn’t slept in days. Her face is full of contempt and suspicion."

    show dorothyPlaceholder at left
    show wwWestAngry at right
    with dissolve

    if hasCh4Happened:
        wwwest "I know you were stalking my house."
    else:
        wwwest "I’ve seen you before"

    dorothy "I..."

    wwwest "I know you wanted to take something from me."

    dorothy "Listen, Scarecrow and I were just-"

    wwwest "It was you, wasn't it? You killed her."

    hide wwWestAngry
    show dorothyPlaceholder at center
    with dissolve

menu bridgescenedialogue:
    "...":
        jump CH5bridgescenecontinued

    "Listen, I know I look super suspicious, but it wasn’t me, I swear-":
        jump CH5bridgescenecontinued

label CH5bridgescenecontinued:
    hide dorothyPlaceholder
    show wwWestAngry at center
    with dissolve

    wwwest "Don’t lie to me! It was you! My sister is dead because of you!"

    hide wwWestAngry
    show dorothyPlaceholder at center
    with dissolve

    dorothy "With what proof?"

    hide dorothyPlaceholder
    show wwWestAngry at center
    with dissolve

    wwwest "The Wizard-"

    hide wwWestAngry
    show dorothyPlaceholder at center
    with dissolve

    dorothy "Do you really trust the Wizard?"

    hide dorothyPlaceholder
    show wwWestAngry at center
    with dissolve

    wwwest "You’ll pay for this, girl, I swear. You will pay for my loss."
    
    hide wwWestAngry

    "A cloud of fog erupts from the air. The witch disappears into it. You are left standing in the cold, alone."

    show dorothyPlaceholder at center
    with dissolve

    dorothy "{i}muttering{\i} 'Be safe, Dorothy', what a dumb thing to promise."

    stop music fadeout 1.0

    scene scarecrowApartment
    with dissolve

    play music "audio/forest.mp3" fadein 2.0

    "Back at Scarecrow’s place, the wannabe detective is cooking up some polaroids." 

    show ScarecrowPlaceholder at center
    with dissolve

    if didYouGiveScarecrowTape:
        "There is one polaroid hanging at Scarecrow's side, drying."

    "He picks the polaroid and brings it to his eyes. He can just make out what it’s depicting. His eyes widen."

    scarecrow "{i}Oh.{\i}"

    if (didYouGiveScarecrowTape) and (hasCollectedRedShoesPhoto) and (hasListenedToLionsTestimony) and (hasCollectedCamera) and (hasCollectedTinManNote):
       
        scene black
        with dissolve

        show ScarecrowPlaceholder at right
        with dissolve

        play sound "audio/telephone ring.mp3" volume 0.3

        "Scarecrow picks up his phone and dials Dorothy's number."

        scarecrow "Dorothy! I have some new important evidence!"

        show dorothyPlaceholder at left
        with dissolve

        dorothy "What, what do you mean, it's 2 A. M. can't you call me later?"

        scarecrow "That photo you gave me, I developed it and it shows someone pushing W. W. West's sister over at the scene of the crime!"

        dorothy "So it wasn't me!"

        scarecrow "Wait, what?"

        dorothy "Oh uh, nothing, can you make out their face?"

        scarecrow "No, not really."

        dorothy "(Hm, wait, the shoes, the note, and now this? The note, “bottom, heirloom, hold down.”, W. W. West called the shoes a family heirloom, and there was obviously something hidden in the bottom of them.)"

        dorothy "(The Wiz seemed very keen on knowing their location, in fact only him and W. W. West even ever mentioned them. It must be one of them, the shoes are the motive! Surely whoever wrote the note is behind the crime. Surely...)"

        scarecrow "Hey? Dorothy? You still there?"

        dorothy "What? Oh yea, okay thanks for the info! We can talk tomorrow!"

        scarecrow "Oh, yea okay sur-"

        "Dorothy hangs up the phone."

        hide ScarecrowPlaceholder 
        with dissolve

        dorothy "If I can just figure out who wrote that note, then surely..."

    stop music fadeout 2.0

    scene black
    with dissolve

    jump chapter06