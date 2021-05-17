# Chapter 2

# transcribed as of 5/17/2021, soon to be changed due to script reasons
define popo = Character("Police Officer", color="#FFFFFF") 

label chapter02:

    "CHAPTER 2: SNEAKING INTO THE POLICE STATION"

    scene policeStation
    with fade

    "You and Scarecrow have just successfully snuck into the police station."

    "You both overhear a commotion over in the nearby interrogation room."

    "As you peak behind the corner, you saw the Wicked witch of the west being interrogated by 'the Wiz' and his partner."

    dorothy "{i}whisper{/i} Look over there! There’s  the camera from the crime scene!"

    scarecrow "{i}whisper{/i} What do you think we should do? Should we grab it or should we eavesdrop more?"

menu chapter02Choice:
    "What should I say...?"

    "Let's grab the camera to hide the evidence.":
        jump chapter02A

    "Let's eavesdrop some more, we might get some more information.":
        jump chapter02B

label chapter02A:

    "The Wiz is visibly getting irritated at WWWest’s uncooperative nature."

    tinman "{i}puts hand on the Wiz's shoulder{/i} Let’s take a break."

    tinman "{i}to WWest{/i} We'll talk again in an hour."

    "The Wiz and his partner leaves the room, and WWest is escorted out of the room shortly afterwards."

    scarecrow "{i}whispers urgently{/i} Quick! Now’s our chance to take back your camera!"

    "You both sneak into the interrogation room, and pick up the camera."

    dorothy "{i}holds up camera{/i} Perfect! Now the evidence is in our hands. Let’s get out of here."

    "While you were inspecting the camera, Scarecrow notices something on the Wiz's desk: a tape from the camera."

    "The Scarecrow takes it for himself without your knowledge."

    jump chapter02MainPath

label chapter02B:

    wiz "YOU CAN REMAIN SILENT ALL YOU WANT, BUT THE EARLIER YOU SPEAK UP, THE EASIER IT WILL BE FOR YOU."

    WWWest "..."

    wiz "{i}shows a picture of something you can't see from here{/i} I SEE THAT YOU TOOK A LIKING TO THESE."

    WWWest "..."

    wiz "WHY DID YOU WANT THEM? WHY DID YOU NEED THEM SO MUCH, THAT YOU HAD TO KILL YOUR OWN SISTER FOR THEM?"

    WWWest "{i}glares{/i} I didn't kill my sister."

    wiz "OKAY. LET’S SAY YOU DIDN’T. WHAT WAS THE SIGNIFICANCE OF THEM?"

    WWWest "You wouldn’t understand, even if I explained it."

    wiz "THAT’S IRRELEVANT TO ME. I JUST WANT TO KNOW {b}WHY{/b} THOSE WERE SO IMPORTANT TO YOU."

    WWWest "They weren’t."

    wiz "{i}sigh{/i} I GUESS WE’RE GOING TO HAVE TO TAKE A DIFFERENT APPROACH. SHORTLY AFTER YOUR SISTER WAS MURDERED, A SINGLE CAMERA WAS FOUND AT THE CRIME SCENE. LOOKS LIKE IT WAS SMASHED, AND IS BEYOND REPAIR. DOES THIS LOOK FAMILIAR TO YOU? {i}gestures towards the camera{/i}"

    WWWest "{i}confused{/i} No, I have never seen this camera before."

    wiz "UPON FURTHER INSPECTION, THE INDENTS ON THE CAMERA LINE UP PERFECTLY WITH MANY OF THE VICTIM’S INJURIES. WE HAVE DEDUCED THAT THE CAMERA WAS, IN FACT, THE MURDER WEAPON."

    WWWest "Interesting."

    wiz "HOW INTERESTING, TO USE A CAMERA AS A WEAPON. I’LL ASK YOU ONE MORE TIME. DO YOU RECOGNIZE THIS CAMERA?"

    WWWest "I’ll repeat myself: I’ve never seen that camera before."

    wiz "{i}frustrated{/i} I SEE THAT THIS IS POINTLESS. OKAY, WE’LL TAKE A BREAK."

    "The Wiz and his partner leaves the room, and WWest is escorted out of the room shortly afterwards."

    scarecrow "{i}whispers urgently{/i} Quick! Now’s our chance!"

    "You both sneak into the interrogation room, and pick up the camera."

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

    scarecrow "Thanks Dorothy!"

    # friendship points variable increase here or something

    "You turned around and started walking out the door."

    "As you were walking out, Scarecrow notices something on the Wiz's desk: one of the tapes from the camera."

    "The Scarecrow takes it without your knowledge, and puts it in his pocket."

    scarecrow "Alright! Let's get out of here"

    jump chapter02MainPath

label chapter02B2:

    "You keep the film to yourself, and you turn around to leave."

    "As you were walking out, Scarecrow notices something on the Wiz's desk: one of the tapes from the camera."

    "The Scarecrow takes it without your knowledge, and puts it in his pocket."

    scarecrow "Alright! Let's get out of here"

    jump chapter02MainPath

label chapter02MainPath:

    "Just as Dorothy and Scarecrow are about to leave, the Wiz's partner from earlier walked in"

    "You check the ID on his shirt - it says 'Tin man'"

    tinman "What are you guys doing here? You know this room is off limits right?"

menu chapter02Choice3:
    "I could have sworn they all left for lunch or something! We need to say something to get out of this situation..."

    "We wanted to ask you some questions about the murder case, and possibly help.":
        jump chapter02BA

    "We were just leaving! Nothing to see here!":
        jump chapter02BB

label chapter02BA:

    "Tin man looks surprised at first, but then he smiles at Dorothy and Scarecrow"

    tinman "Sure thing! Here’s a note that we found at the crime scene. We had a lot of trouble deciphering it, see if you guys can figure something out."

    "You and Scarecrow both look closely at the note, which reads: 'Bottom of heirloom hold down'"

    dorothy "{i}whispers to SCARECROW{/i} Why is this guy giving us evidence? Is he crazy?"

    dorothy "{i}to Tin man{/i} What is this heirloom mentioned in the notes?"

    tinman "I’m not too sure. The investigator believes that there isn’t enough context to make any assumptions yet."

    scarecrow "That’s fair, we don’t know the context of the note, and we also don’t know what the heirloom is."

    tinman "{i}lowers voice{/i} Even though I’m giving you guys the evidence, just a warning, try to stay out of the Wiz’s way."

    dorothy "Is there a particular reason you say that?"

    tinman "To be completely honest with you, I don’t trust him. I think he’s hiding something, but I don’t know what. Also, he won’t like that you guys are involved in the investigation."

    scarecrow "Noted, thank you for the help!"

    tinman "No problem, good luck on your investigation!"

    "You and Scarecrow leave the police station."

    dorothy "Hey wasn't that guy, like, really weird?"

    scarecrow "Nah, he just has a big heart."

    popo "{i}to DOROTHY and SCARECROW{/i} Hey STOP!"

    dorothy "Time to leave! {i}runs away{/i}"

    scarecrow "I should go too. {i}follows Dorothy{/i}"

    popo "Hey Tin man! Who were those people?"

    tinman "..."

    scene black
    with dissolve

    jump chapter03

label chapter02BB:

    "The Tin man gave you a skeptical look"

    tinman "What were you doing here in the first place then?"

    scarecrow "We were just curious about the case. We wanted to see if we could help solve this murder, but we didn’t have any evidence."

    tinman "So you just snuck into the interrogation room?"

    dorothy "I mean, we probably should’ve asked first. Is it still okay if we try to help out?"

    tinman "{i}sigh{/i} I suppose there’s no harm. Here, take a look at this. This is a note that was found at the crime scene."

    "You and Scarecrow both look closely at the note, which reads: 'Bottom of heirloom hold down'"

    dorothy "I can't figure out what this heirloom is, and what the note means."

    tinman "Yeah, we're having trouble with it too. I can't tell you anything else though."

    dorothy "Well, thank you for your time! This was very helpful, and we’ll let you know if we find any new information."

    tinman "Anytime, good luck with your investigation."

    popo "{i}to DOROTHY and SCARECROW{/i} Hey STOP!"

    dorothy "Time to leave! {i}runs away{/i}"

    scarecrow "I should go too. {i}follows Dorothy{/i}"

    popo "Hey Tin man! Who were those people?"

    tinman "..."

    scene black
    with dissolve

    jump chapter03