# Chapter 5

label chapter05:
    "CHAPTER 5: Scarecrow's Apartment - night"

    "Papers and Newspaper clippings are scattered everywhere. There is stuff written on the walls, connected together with string."

    "On the bookshelf is an assortment of books and jars full of...something. Food? Experiments? Food that became an experiment after it spoiled? Who knows."

    "The door slams open, and you and Scarecrow enter the scene, Scarecrow looking more energetic than anyone has ever seen him."

    "You look around the room in a mix of wonder and disgust."

    scarecrow "Make yourself at home!"

    dorothy "Uh..."

    "You eye the mess around your feet."

    scarecrow "Good choice!"

    "He grabs an old-looking chalkboard and writes {u}EVIDENCE{/u} at the top"

    scarecrow "So! What do we know?"

label .choice1:
menu evidenceMenu:
    "This menu depends on what you have managed to collect and what you haven’t. This will reappear until you decide to \"Move on\" from talking about the evidence."

    "Pick photo of Red Shoes" if hasCollectedRedShoesPhoto:
        jump .choiceA

    "Pick Lion's Testimony" if hasListenedToLionsTestimony:
        jump .choiceB

    "Pick Camera" if hasCollectedCamera:
        jump .choiceC

    "Pick Tape" if hasCollectedTape:
        jump .choiceD

    "Pick Note" if hasCollectedTinManNote:
        jump .choiceE

    "Move on":
        jump .moveON

label .choiceA:
    scarecrow "Ah, the photo at the W.W. West's mansion! She seemed to have stolen it from the evidence room, suspicious, isn’t it?"

menu .chA01:
    "What will be your response?"

    "I mean, we’ve also stolen stuff from the evidence room…":
        scarecrow "Details!"

        jump .chA01cont

    "Suspicious! Yep, super suspicious!":
        scarecrow "ISN'T IT?"

        jump .chA01cont

label .chA01cont:
    scarecrow "But what is the significance of these shoes...and why were they missing from the crime scene?"

menu .chA02:
    "What will be your response?"

    "These shoes could be the reason why she died.":
        scarecrow "A motive? Those do look like very fancy shoes...and the photo clearly shows a secret compartment."

        scarecrow "Maybe there was something important hidden in those shoes!"

        dorothy "Yeah, and the murderer took them off her cooling corpse!"

        scarecrow "{i}sounding delighted{\i} How morbid!"

        if hasListenedInOnWitchCh4:
            dorothy "The red shoes are a family heirloom."
            #IFFFF ---->>> If Dorothy listens in on the witch in ch4: She also mentioned them being a family heirloom.
        
        jump .choice1

    "Maybe they’re a red herring, haha get it?":
        scarecrow "That was horrible…(sniff) I’m so proud…"

        jump .choice1

label .choiceB:

    scarecrow "The lion said there was someone in a heated argument with the victim before the murder. They said...huh, I can’t remember."

    if hasCollectedRedShoes:
        dorothy "They wanted the shoes."

        scarecrow "Right! The shoes from the photo! The ones missing from the crime scene!"
    else:
        dorothy "Something about...shoes?"

        scarecrow "Shoes...now why would that stranger say anything about shoes?"

    scarecrow "The Lion seemed very convinced that the one arguing with the witch before her death was the murderer. "
    
    scarecrow "Unless HE’s the murderer and trying to pin it on someone else."
    
    "You both look at each other."

    dorothy "Nah!"
    
    scarecrow "No way!" # dorothy and scarecrow says this together

    dorothy "So the mysterious stranger with the scary eyes did it? Helpful."

    scarecrow "Well, how many people in London have scary eyes?"

    dorothy "{i}Glares{\i}"

    scarecrow "{i}jokingly{\i} Actually, who says you’re not the murderer?"

    "{i}awkward silence{\i}"

    scarecrow "Anyway!"

    jump .choice1

label .choiceC:
    scarecrow "Ah, the camera found at the crime scene! The CLUE TO EVERYTHING!"

    dorothy "Is it?"

    scarecrow "I don’t know, might be!"

    scarecrow "The question remains...whose camera is it? I can take fingerprints, see if they’re in any database…"

    dorothy "Maybe it’s just some innocent passerby’s, who didn’t want to get roped into any of this. Maybe they lost it at the worst opportune moment, and are regretting they ever came to this city, and wondering if they’re gonna be the number one suspect through sheer dumb luck."

    scarecrow "That’s...a very specific hypothetical."

    dorothy "Well, what do you think?!"

    scarecrow "I think…"

    if doYouSuspectYourself:
        scarecrow "That this camera might be the murder weapon."
    else:
        scarecrow "That this camera probably doesn’t matter."

    jump .choice1

label .choiceD:
    scarecrow "This tape we got from the evidence room..."

    scarecrow "It was probably in the camera we found. Though I guess the tape doesn’t matter as much as what’s on it, doesn’t it?"

    scarecrow "We need to develop it!"

    dorothy "Yes, I guess we do."

    scarecrow "It will take me tonight, so we’ll find out in the morning. I do hope it’s something relevant. I’m glad you found it, Dorothy."

    if doYouSuspectYourself:
        dorothy "sure."
    else:
        dorothy "We need to find out what’s on that tape!"

    jump .choice1

label .choiceE:
    scarecrow "The note the Tin Man gave us...seemingly for free."

    dorothy "Yeah, that was weird."

    #I did not insert the word in the note yet
    scarecrow "Anyway! It said something about (insert the words the note contains). The handwriting might give away the author."

    dorothy "I mean...what are we gonna do, ask everyone in London to write their names?"

    scarecrow "An admirable effort! But we’re definitely not doing that!"

    jump .choice1

label .moveON:

    if doYouSuspectYourself:
        dorothy "..."

        scarecrow "Hey, listen…I know it seems pointless, you know?"

        dorothy "..."

        scarecrow "I used to think I couldn’t figure out anything. I was...kind of the idiot, you know?"
    else:
        dorothy "Man, this is a lot of evidence."

        scarecrow "Yeah. But that’s good! We’re getting somewhere!"

        dorothy "Hey, Scarecrow?"

        scarecrow "What’s up?"

        dorothy "If you had to pick...between helping a friend and finding the truth, what would you pick?"

        scarecrow "The truth, obviously."

        dorothy "Right."

        scarecrow "That is a very strange question, Dorothy."

        dorothy "Yeah?"

        scarecrow "I mean, if two people are friends, hypothetically speaking, they would not hinder each other from the truth, wouldn’t they?"
        scarecrow "Friends don’t lie to each other."

        "You are both silent for a moment."
        "You want to tell Scarecrow you were at the tower that day, that it was your camera, but something’s holding you back. Fear, probably."
        "You don’t know anyone in this city."
        "You didn’t know anyone until today."

        scarecrow "I’M NOT A REAL DETECTIVE!"

        scarecrow "Few, that felt good to get off my chest."

        scarecrow "I wanted to be! But I used to think I couldn’t figure out anything. I was...kind of the idiot, you know?"
    
    scarecrow "In school, and after, I...wasn’t really good at a lot of things."
    scarecrow "{b}Every chance I got, he rejected me from the academy because I always got in the way with my silly ideas{/b}"
    scarecrow "Scarecrow the brainless, that’s what they all called me."
    scarecrow "Before I met you, I thought of, y’know, giving up. I wasn’t good at anything, why would I think I’d be good at this? {i}he gestures at the chalkboard{/i}"
    scarecrow "But then, you showed up, and you seemed so eager to figure it out with me, I thought maybe...I wasn’t all that bad after all."
    scarecrow "If this one kid follows me, maybe I’m actually good. At being a detective."
    scarecrow "So. Thanks, I guess. It’s been...really fun."

menu dorothychoice:
    "Your choice"

    "Say nothing.":
        jump saynothing

    "Comfort Scarecrow.":
        jump comfort


label saynothing:

    dorothy "..."

    scarecrow "But you don’t look that eager now. Maybe I am the idiot, huh? Running us in circles? I get it."

    "He gestures toward the door."

    scarecrow "You should go home. Your parents are probably looking for you."

    dorothy "...Yeah, I guess you’re right."

    "You turn to leave. As you walk out the door, Scarecrow calls out."

    scarecrow "Wait!"

    "You pause."

    scarecrow "I..."

    scarecrow "Nevermind. Be safe."

    dorothy "...I will"

    jump bridgescene


label comfort:
    dorothy "You’re not stupid, you know."

    scarecrow "Thanks."

    dorothy "Okay, you make stupid decisions...sometimes. A lot of the time. All the time."

    dorothy "But. You’re good at figuring things out. And better than that, you care. Not a lot of people care as much as you do, you know? About finding the truth."

    "Scarecrow looks at the board of clues. He fidgets with the chalk."

    scarecrow "Thanks, I guess. Maybe you're-"

    dorothy "I'm right."

    "Scarecrow laughs."

    scarecrow "Maybe I'm not brainless after all."

    scarecrow "I think this story is all coming together. I just need...another night. (if dorothy gives him the tape) plus we need to develop that tape. Give me until tomorrow morning, all right?"

    dorothy "Sure. I should be getting home anyway."

    scarecrow "Hey, Dorothy?"

    dorothy "Yeah?"

    scarecrow "Be safe."

    dorothy "I will."

    

label bridgescene:

    "You stand outside at nighttime. You're crossing the London Bridge when you see a tall, dark figure in your path. The fog is too thick for you to see clearly."

    dorothy "Hello?"

    wwwest "You."

    "W. W. West steps out of the fog. She looks like she hasn’t slept in days. Her face is full of contempt and suspicion."

    wwwest "I know you wanted to take something from me."

    dorothy "Listen, Scarecrow and I were just-"

    wwwest "It was you, wasn't it? You killed her."

menu bridgescenedialogue:
    "...":
        jump bridgescenecontinued

    "Listen, I know I look super suspicious, but it wasn’t me, I swear-":
        jump bridgescenecontinued

label bridgescenecontinued:
    wwwest "Don’t lie to me! It was you! My sister is dead because of you!"

    dorothy "With what proof?"

    wwwest "The Wizard-"

    dorothy "Do you really trust the Wizard?"

    wwwest "You’ll pay for this, girl, I swear. You will pay for my loss."
    
    "A cloud of fog erupts from the air. The witch disappears into it. You are left standing in the cold, alone."

    dorothy "{i}muttering{\i} 'Be safe, Dorothy', what a dumb thing to promise."

    "Back at Scarecrow’s place, the wannabe detective is cooking up some polaroids." 
    #Depending on if Dorothy gives him the tape or not, there will be one hanging at his side, drying. 
    
    "He picks the polaroid and brings it to his eyes. He can just make out what it’s depicting. His eyes widen."

    scarecrow "{i}Oh.{\i}"

    "FADE TO BLACK"

    jump chapter06