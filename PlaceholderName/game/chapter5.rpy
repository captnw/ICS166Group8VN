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

    "He grabs an old-looking chalkboard and writes EVIDENCE at the top"

    scarecrow "So! What do we know?"

label choice1:
menu evidenceMenu:
    "This menu depends on what you have managed to collect and what you haven’t. This will reappear until you decide to \"Move on\" from talking about the evidence."

    "Pick Red Shoes":
        jump choiceA

    "Pick Lion's Testimony":
        jump choiceB

    "Pick Camera":
        jump choiceC

    "Pick Tape":
        jump choiceD

    "Pick Note":
        jump choiceE

    "Move on":
        jump moveON




label choiceA:
    scarecrow "Ah, the photo at the W.W. West's mansion! She seemed to have stolen it from the evidence room, suspicious, isn’t it?"

menu chA01:
    "What will be your response?"

    "I mean, we’ve also stolen stuff from the evidence room…":
        jump chA01a

    "Suspicious! Yep, super suspicious!":
        jump chA01b

label chA01a:
    dorothy "I mean, we’ve also stolen stuff from the evidence room…"

    scarecrow "Details!"
    jump chA01cont

label chA01b:
    dorothy "Suspicious! Yep, super suspicious!"

    scarecrow "ISN'T IT?"

label chA01cont:

    scarecrow "But what is the significance of these shoes...and why were they missing from the crime scene?"

menu chA02:
    "What will be your response?"

    "These shoes could be the reason why she died.":
        jump chA02a

    "Maybe they’re a red herring, haha get it?":
        jump chA02b

label chA02a:
    dorothy "These shoes could be the reason why she died."

    scarecrow "A motive? Those do look like very fancy shoes...and the photo clearly shows a secret compartment."

    scarecrow "Maybe there was something important hidden in those shoes!"

    dorothy "Yeah, and the murderer took them off her cooling corpse!"

    scarecrow "{i}sounding delighted{\i} How morbid!"

    #IFFFF ---->>> If Dorothy listens in on the witch in ch4: She also mentioned them being a family heirloom.
    
    jump chA02cont

label chA02b:
    dorothy "Maybe they’re a red herring, haha get it?"

    scarecrow "That was horrible…(sniff) I’m so proud…"

label chA02cont:

    jump choice1







label choiceB:

    scarecrow "The lion said there was someone in a heated argument with the victim before the murder. They said...huh, I can’t remember."

    #IFFFFFF-->>>(if red shoes picked up) They wanted the shoes
    dorothy "They wanted the shoes."

    scarecrow "Right! The shoes from the photo! The ones missing from the crime scene!"
    # ELSE -->>>(if red shoes are not picked up) Something about...shoes?

    dorothy "Something about...shoes?"

    scarecrow "Shoes...now why would that stranger say anything about shoes?"

    scarecrow "The Lion seemed very convinced that the one arguing with the witch before her death was the murderer. "
    
    scarecrow "Unless HE’s the murderer and trying to pin it on someone else."
    
    "You both look at each other."

    dorothy + scarecrow "Nah!"

    dorothy "So the mysterious stranger with the scary eyes did it? Helpful."

    scarecrow "Well, how many people in London have scary eyes?"

    dorothy "{i}Glares{\i}"

    scarecrow "{i}jokingly{\i} Actually, who says you’re not the murderer?"

    "{i}awkward silence{\i}"

    scarecrow "Anyway!"

    jump choice1






label choiceC:
    scarecrow "Ah, the camera found at the crime scene! The CLUE TO EVERYTHING!"

    dorothy "Is it?"

    scarecrow "I don’t know, might be!"

    scarecrow "The question remains...whose camera is it? I can take fingerprints, see if they’re in any database…"

    dorothy "Maybe it’s just some innocent passerby’s, who didn’t want to get roped into any of this. Maybe they lost it at the worst opportune moment, and are regretting they ever came to this city, and wondering if they’re gonna be the number one suspect through sheer dumb luck."

    scarecrow "That’s...a very specific hypothetical."

    dorothy "Well, what do you think?!"

    scarecrow "I think…"

    #IFFFFF---->>> (if Dorothy suspects herself) That this camera might be the murder weapon.
    scarecrow "That this camera might be the murder weapon."

    #ELSEEE---->>> (if Dorothy knows she’s innocent) That this camera probably doesn’t matter.
    scarecrow "That this camera probably doesn’t matter."

    jump choice1





label choiceD:
    scarecrow "This tape we got from the evidence room..."

    scarecrow "It was probably in the camera we found. Though I guess the tape doesn’t matter as much as what’s on it, doesn’t it?"

    scarecrow "We need to develop it!"

    dorothy "Yes, I guess we do."

    scarecrow "It will take me tonight, so we’ll find out in the morning. I do hope it’s something relevant. I’m glad you found it, Dorothy."

    #IFFFFF---->>> (if she thinks she’s the murderer) sure.
    dorothy "sure."

    #ELSEEE---->>> (if she thinks she’s innocent) We need to find out what’s on that tape!
    dorothy "We need to find out what’s on that tape!"

    jump choice1


label choiceE:
    scarecrow "The note the Tin Man gave us...seemingly for free."

    dorothy "Yeah, that was weird."

    #I did not insert the word in the note yet
    scarecrow "Anyway! It said something about (insert the words the note contains). The handwriting might give away the author."

    dorothy "I mean...what are we gonna do, ask everyone in London to write their names?"

    scarecrow "An admirable effort! But we’re definitely not doing that!"

    jump choice1


label moveON:
    jump chapter06