# Chapter 2

define popo = Character("Police Officer", color="#FFFFFF") 

label chapter02:

    "CHAPTER 2: SNEAKING INTO THE POLICE STATION"

    play music "audio/forest.mp3" loop fadein 3.0

    scene policeStation at truecenter:
        zoom 1.6
    with fade

    "You and Scarecrow have just successfully snuck into the police station."

    "You both overhear a commotion over in the nearby interrogation room."

    "As you peak behind the corner, you saw the Wicked witch of the west being interrogated by 'the Wiz' and his partner."

    show dorothyPlaceholder
    with dissolve

    dorothy "{i}whisper{/i} Look over there! There’s the camera from the crime scene!"

    hide dorothyPlaceholder
    show ScarecrowPlaceholder
    with dissolve

    scarecrow "{i}whisper{/i} What do you think we should do? Should we grab it or should we eavesdrop more?"

    hide ScarecrowPlaceholder
    show dorothyPlaceholder
    with dissolve

menu chapter02Choice:
    "What should I say...?"

    "Let's grab the camera to hide the evidence.":
        jump chapter02A

    "Let's eavesdrop some more, we might get some more information.":
        jump chapter02B

label chapter02A:

    scene policeQuestioningRoom :
        zoom 1.5
    show wizPlaceholder
    with fade

    "The Wiz is visibly getting irritated at WWWest’s uncooperative nature."

    show wizPlaceholder at left
    show tinmanPlaceholder at right
    with dissolve

    tinman "{i}puts hand on the Wiz's shoulder{/i} Let’s take a break."

    tinman "{i}to WWest{/i} We'll talk again in an hour."

    hide wizPlaceholder
    hide tinmanPlaceholder

    "The Wiz and his partner leaves the room, and WWest is escorted out of the room shortly afterwards."

    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "{i}whispers urgently{/i} Quick! Now’s our chance to take the camera!"

    hide ScarecrowPlaceholder
    show dorothyPlaceholder at center
    with dissolve

    "You both sneak into the interrogation room, and pick up the camera."
    $ hasCollectedCamera = True

    dorothy "{i}holds up camera{/i} Perfect! Now the evidence is in our hands. Let’s get out of here."

    hide dorothyPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve

    "While you were inspecting the camera, Scarecrow notices something on the Wiz's desk: a tape from the camera."

    "The Scarecrow takes it for himself without your knowledge."

    hide ScarecrowPlaceholder at center

    jump chapter02MainPath

label chapter02B:

    scene policeQuestioningRoom :
        zoom 1.5
    with fade

    show wizPlaceholder at center

    wiz "YOU CAN REMAIN SILENT ALL YOU WANT, BUT THE EARLIER YOU SPEAK UP, THE EASIER IT WILL BE FOR YOU."

    show wizPlaceholder at left
    show wwWestAngry at right
    with dissolve

    WWWest "..."

    hide wwWestAngry
    show wizPlaceholder at center
    with dissolve

    wiz "{i}shows a picture of something you can't see from here{/i} I SEE THAT YOU TOOK A LIKING TO THESE."

    show wizPlaceholder at left
    show wwWestAngry at right
    with dissolve

    WWWest "..."

    hide wwWestAngry
    show wizPlaceholder at center
    with dissolve

    wiz "WHY DID YOU WANT THEM? WHY DID YOU NEED THEM SO MUCH, THAT YOU HAD TO KILL YOUR OWN SISTER FOR THEM?"

    hide wizPlaceholder
    show wwWestAngry at center
    with dissolve

    WWWest "{i}glares{/i} I didn't kill my sister."

    hide wwWestAngry
    show wizPlaceholder at center
    with dissolve

    wiz "OKAY. LET’S SAY YOU DIDN’T. WHAT WAS THE SIGNIFICANCE OF THEM?"

    hide wizPlaceholder
    show wwWestAngry at center
    with dissolve

    WWWest "You wouldn’t understand, even if I explained it."

    hide wwWestAngry
    show wizPlaceholder at center
    with dissolve

    wiz "THAT’S IRRELEVANT TO ME. I JUST WANT TO KNOW {b}WHY{/b} THOSE WERE SO IMPORTANT TO YOU."

    hide wizPlaceholder
    show wwWestAngry at center
    with dissolve

    WWWest "They weren’t."

    hide wwWestAngry
    show wizPlaceholder at center
    with dissolve

    wiz "{i}sigh{/i} I GUESS WE’RE GOING TO HAVE TO TAKE A DIFFERENT APPROACH."
    wiz "SHORTLY AFTER YOUR SISTER WAS MURDERED, A SINGLE CAMERA WAS FOUND AT THE CRIME SCENE. LOOKS LIKE IT WAS SMASHED, AND IS BEYOND REPAIR."
    wiz "DOES THIS LOOK FAMILIAR TO YOU? {i}gestures towards the camera{/i}"

    hide wizPlaceholder
    show wwWestAngry at center
    with dissolve

    WWWest "{i}confused{/i} No, I have never seen this camera before."

    hide wwWestAngry
    show wizPlaceholder at center
    with dissolve

    wiz "UPON FURTHER INSPECTION, THE INDENTS ON THE CAMERA LINE UP PERFECTLY WITH MANY OF THE VICTIM’S INJURIES. WE HAVE DEDUCED THAT THE CAMERA WAS, IN FACT, THE MURDER WEAPON."

    hide wizPlaceholder
    show wwWestAngry at center
    with dissolve

    WWWest "Interesting."

    hide wwWestAngry
    show wizPlaceholder at center
    with dissolve

    wiz "HOW INTERESTING, TO USE A CAMERA AS A WEAPON. I’LL ASK YOU ONE MORE TIME. DO YOU RECOGNIZE THIS CAMERA?"

    hide wizPlaceholder
    show wwWestAngry at center
    with dissolve

    WWWest "I’ll repeat myself: I’ve never seen that camera before."

    hide wwWestAngry
    show wizPlaceholder at center
    with dissolve

    wiz "{i}frustrated{/i} I SEE THAT THIS IS POINTLESS. OKAY, WE’LL TAKE A BREAK."

    hide wizPlaceholder

    "The Wiz and his partner leaves the room, and WWest is escorted out of the room shortly afterwards."

    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "{i}whispers urgently{/i} Quick! Now’s our chance!"

    hide ScarecrowPlaceholder

    "You both sneak into the interrogation room, and pick up the camera."
    $ hasCollectedCamera = True

    show dorothyPlaceholder at center
    with dissolve

    dorothy "{i}holds up camera{/i} Perfect! Now the evidence is in our hands. Let’s get out of here."

    "You discover a tape next to the camera. You try to discern what's on the tape before realizing it's not developed yet."
    
    "Once developed, this may clear things up on what happened earlier..."

menu chapter02Choice2:
    "Should I give this piece of evidence to Scarecrow?"

    "Give the tape to Scarecrow.":
        jump chapter02B1

    "Keep the tape.":
        jump chapter02B2

label chapter02B1:

    dorothy "{i}to scarecrow{/i} Hey, I found this undeveloped photo, maybe it’ll come into use later."

    "You give him the tape, and he accepts it."

    hide dorothyPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve 

    scarecrow "Thanks Dorothy!"

    $ didYouGiveScarecrowTape = True

    hide ScarecrowPlaceholder

    "You turned around and started walking out the door."

    "As you were walking out, Scarecrow notices something on the Wiz's desk: one of the tapes from the camera."

    show ScarecrowPlaceholder at center
    with dissolve

    "The Scarecrow takes it without your knowledge, and puts it in his pocket."

    scarecrow "Alright! Let's get out of here"

    hide ScarecrowPlaceholder

    jump chapter02MainPath

label chapter02B2:

    "You keep the film to yourself, and you turn around to leave."

    hide dorothyPlaceholder

    "As you were walking out, Scarecrow notices something on the Wiz's desk: one of the tapes from the camera."

    show ScarecrowPlaceholder at center
    with dissolve

    "The Scarecrow takes it without your knowledge, and puts it in his pocket."

    scarecrow "Alright! Let's get out of here"

    hide ScarecrowPlaceholder

    jump chapter02MainPath

label chapter02MainPath:

    scene policeStation at truecenter:
        zoom 1.6
    with fade

    "Just as Dorothy and Scarecrow are about to leave, the Wiz's partner from earlier walked in"

    show tinmanPlaceholder at center
    with dissolve

    "You check the ID on his shirt - it says 'Tin man'"

    tinman "What are you guys doing here? You know this room is off limits right?"

    hide tinmanPlaceholder
    show dorothyPlaceholder at center
    with dissolve

menu chapter02Choice3:
    "I could have sworn they all left for lunch or something! I need to say something to get out of this situation..."

    "We wanted to ask you some questions about the murder case, and possibly help.":
        jump chapter02BA

    "We were just leaving! Nothing to see here!":
        jump chapter02BB

label chapter02BA:

    hide dorothyPlaceholder

    "Tin man looks surprised at first, but then he smiles at Dorothy and Scarecrow"

    show tinmanPlaceholder at center
    with dissolve

    tinman "Sure thing! Here’s a note that we found at the crime scene. We had a lot of trouble deciphering it, see if you guys can figure something out."

    hide tinmanPlaceholder

    "You and Scarecrow both look closely at the note, which reads: 'Bottom of heirloom hold down'"
    $ hasCollectedTinManNote = True

    show dorothyPlaceholder
    with dissolve

    dorothy "{i}whispers to SCARECROW{/i} Why is this guy giving us evidence? Is he crazy?"

    dorothy "{i}to Tin man{/i} What is this heirloom mentioned in the notes?"

    hide dorothyPlaceholder
    show tinmanPlaceholder
    with dissolve

    tinman "I’m not too sure. The investigator believes that there isn’t enough context to make any assumptions yet."

    hide tinmanPlaceholder
    show ScarecrowPlaceholder
    with dissolve

    scarecrow "That’s fair, we don’t know the context of the note, and we also don’t know what the heirloom is."

    hide ScarecrowPlaceholder
    show tinmanPlaceholder
    with dissolve

    tinman "{i}lowers voice{/i} Even though I’m giving you guys the evidence, just a warning, try to stay out of the Wiz’s way."

    hide tinmanPlaceholder
    show dorothyPlaceholder
    with dissolve

    dorothy "Is there a particular reason you say that?"

    hide dorothyPlaceholder
    show tinmanPlaceholder
    with dissolve

    tinman "To be completely honest with you, I don’t trust him."
    tinman "I think he’s hiding something, but I don’t know what."
    tinman "Also, he won’t like that you guys are involved in the investigation."

    hide tinmanPlaceholder
    show ScarecrowPlaceholder
    with dissolve

    scarecrow "Noted, thank you for the help!"

    hide ScarecrowPlaceholder
    show tinmanPlaceholder
    with dissolve

    tinman "No problem, good luck on your investigation!"

    hide tinmanPlaceholder

    "You and Scarecrow leave the police station."

    scene outsidePoliceStation :
        zoom 1.5

    show dorothyPlaceholder at center
    with dissolve

    dorothy "Hey wasn't that guy, like, really weird?"

    show dorothyPlaceholder at center
    show ScarecrowPlaceholder at right
    with dissolve

    scarecrow "Nah, he just has a big heart."

    hide dorothyPlaceholder
    hide ScarecrowPlaceholder
    show RandomPoliceOfficer at center
    with dissolve

    popo "{i}to DOROTHY and SCARECROW{/i} Hey STOP!"
    
    hide RandomPoliceOfficer
    show dorothyPlaceholder at center
    with dissolve

    dorothy "Time to leave! {i}runs away{/i}"

    hide dorothyPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "I should go too. {i}follows Dorothy{/i}"

    hide ScarecrowPlaceholder
    show RandomPoliceOfficer at center
    with dissolve

    popo "Hey Tin man! Who were those people?"

    show RandomPoliceOfficer at left
    show tinmanPlaceholder at right
    with dissolve

    tinman "..."

    stop music fadeout 2.0

    scene black
    with dissolve

    jump chapter03

label chapter02BB:

    hide dorothyPlaceholder

    "The Tin man gave you a skeptical look"

    show tinmanPlaceholder at center
    with dissolve

    tinman "What were you doing here in the first place then?"

    hide tinmanPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "We were just curious about the case. We wanted to see if we could help solve this murder, but we didn’t have any evidence."

    hide ScarecrowPlaceholder
    show tinmanPlaceholder
    with dissolve

    tinman "So you just snuck into the interrogation room?"

    hide tinmanPlaceholder
    show dorothyPlaceholder at center
    with dissolve

    dorothy "I mean, we probably should’ve asked first. Is it still okay if we try to help out?"

    hide dorothyPlaceholder
    show tinmanPlaceholder
    with dissolve

    tinman "{i}sigh{/i} I suppose there’s no harm. Here, take a look at this. This is a note that was found at the crime scene."

    hide tinmanPlaceholder

    "You and Scarecrow both look closely at the note, which reads: 'Bottom of heirloom hold down'"
    $ hasCollectedTinManNote = True

    show dorothyPlaceholder at center
    with dissolve

    dorothy "I can't figure out what this heirloom is, and what the note means."

    hide dorothyPlaceholder
    show tinmanPlaceholder
    with dissolve

    tinman "Yeah, we're having trouble with it too. I can't tell you anything else though."

    hide tinmanPlaceholder
    show dorothyPlaceholder
    with dissolve

    dorothy "Well, thank you for your time! This was very helpful, and we’ll let you know if we find any new information."

    hide dorothyPlaceholder
    show tinmanPlaceholder
    with dissolve

    tinman "Anytime, good luck with your investigation."

    hide tinmanPlaceholder
    show RandomPoliceOfficer at center
    with dissolve

    popo "{i}to DOROTHY and SCARECROW{/i} Hey STOP!"
    
    hide RandomPoliceOfficer
    show dorothyPlaceholder at center
    with dissolve

    dorothy "Time to leave! {i}runs away{/i}"

    hide dorothyPlaceholder
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "I should go too. {i}follows Dorothy{/i}"

    hide ScarecrowPlaceholder
    show RandomPoliceOfficer at center
    with dissolve

    popo "Hey Tin man! Who were those people?"

    show RandomPoliceOfficer at left
    show tinmanPlaceholder at right
    with dissolve

    tinman "..."

    stop music fadeout 2.0

    scene black
    with dissolve

    jump chapter03