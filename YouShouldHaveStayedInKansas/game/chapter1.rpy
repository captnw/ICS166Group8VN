# Chapter 1

# define a character here, once defined, these
# are shared with all .rpy scripts
define WWWest1 = Character("Wicked Witch of the West", color="#27c277")
define WWWest = Character("W. W. West", color="#27c277")
define wiz = Character("Lead Investigator", color="#d959d0")
define Unknown = Character("MAN IN BIG COAT AND HAT", color="#d959d0")
define randomDude = Character("RANDOM PERSON", color="#ecff80")
define investigator = Character("\"Investigator\"", color="#9999ff")


label chapter01:

    "CHAPTER 1: WITHIN THE CROWD"

    play music "audio/distrust.mp3" loop fadein 3.0 volume 0.5

    scene crimeScene
    with fade

    #description of scene here
    #placeholder of random street
    "You find yourself within the crowd horrified by the dead woman lying down in the middle of everyone."
    "Your camera only inches away from the motionless body and your own body begins to fail as you breath harshly, unable to move from your position."

    show wizBlurred
    with dissolve

    "Then you see a group of police officers coming in with a man in a big coat and hat leading the way."
    "His voice is loud, direct, and terrifying, and he’s telling people to move out of the way."

    Unknown "ALRIGHT EVERYONE MOVE OUT OF THE WAY!"
    Unknown "OFFICERS WE NEED TO MAKE A PERIMETER AROUND THIS AREA AND I WILL TAKE CARE OF LOOKING AROUND FOR CLUES AND EVIDENCE."
    
    hide wizBlurred
    show MaleStranger at right
    with dissolve

    randomDude "That’s the Lead Inspector. Many call him “The Wiz” because he catches the culprit every time with his brilliance."

    "Upon hearing this you grow even more pale to the point where you can also be suspected as a fresh corpse."

    hide MaleStranger

    "Due to this you slightly stumble on yourself and see a man within the crowd looking just as terrified as yourself."

    show dorothyPlaceholder at center
    with dissolve

    #choice 1
menu chapter01Choice01:
    "You finally gather yourself together and make a choice."

    "Sneak away":
        hide dorothyPlaceholder
        "You try to sneak away but end up tripping on yourself. Someone grabs you as you are falling."
        jump chp01Choice01Cont

    "Continue to blend in with the crowd":
        hide dorothyPlaceholder
        "You try blending in with the crowd, but are grabbed by someone."
        jump chp01Choice01Cont

    "Make a run for it":
        hide dorothyPlaceholder
        "You turn around quickly and try to run away, but end up tripping on someone's foot and as you are about to fall someone else grabs your arm."
        jump chp01Choice01Cont

label chp01Choice01Cont:

    show ScarecrowPlaceholder
    with dissolve

    "And this person just starts to scan you up and down."

    investigator "Hello there civilian. I am one of the investigators on this case and you look suspicious."

    "There is silence for a second, but within that second you break into a cold sweat and wonder if this is it if this was going to be your final moments."

    investigator "{i}Breaks the silence immediately{/i} Now I will be asking you a couple questions and I want straight answers." 
    investigator "Got it? GOT IT? Good!"

    investigator "Where were you yesterday?! What’s your favorite color?! What were you doing before the incident?!"

    investigator "What do you normally like to eat?! Who can testify for you?! How many fingers do I have behind my back?!"

    "As this goes on, you no longer feel unease. In fact you feel very confused about what was going on. But before you can even get a word out “The Wiz” decides to pop in."

    hide ScarecrowPlaceholder
    show wizPlaceholder
    with dissolve

    wiz "WHAT ARE YOU DOING HERE “SCARECROW”?!" 
    wiz "SNOOPING AROUND CRIME SCENES AGAIN HUH? LEAVE IT TO THE PROFESSIONALS KID."
    wiz "I APOLOGIZE, YOUNG LADY, IF THIS AMATUER BOTHERED YOU AT ALL."

    hide wizPlaceholder
    show dorothyPlaceholder
    with dissolve

    #choice 2
menu chapter01Choice02:
    "How will you respond?"

    "Tell the lead investigator that he was not a bother at all":
        dorothy "{i}annoyed{/i} Actually, he was not a bother at all."

        "But the lead investigator doesn’t care and just moves on."
        jump chp01Choice02Cont

    "Sarcastically accepts the apology":
        dorothy "{i}sarcastically{/i} I most gracely accept such a sincere apology."
        jump chp01Choice02Cont

    "Stay silent":
        "You decide to stay silent, but don’t like how Scarecrow was being treated by the Lead Investigator aka “The Wiz” even if he is an ametuar and weird."
        jump chp01Choice02Cont

label chp01Choice02Cont:

    stop music fadeout 5.0

    hide dorothyPlaceholder
    show wizPlaceholder
    with dissolve

    wiz "SCARECROW JUST GO HOME, YOU’RE JUST BOTHERING EVERYONE AROUND HERE."

    hide wizPlaceholder
    show ScarecrowPlaceholder
    with dissolve

    scarecrow "yes, sir."

    "You watch as Scarecrow walks away with his head down and decide to follow him in order to try and cheer him up because you want to help him feel better."

    scene randomStreet :
        zoom 1.5
    show ScarecrowPlaceholder at left
    show dorothyPlaceholder at right
    with fade

    play music "audio/sillytheme.mp3" loop fadein 2.0 volume 0.5

    dorothy "Hey, hold on!"
    dorothy "Hey!"
    dorothy "Scarecrow!"

    scarecrow "Yeah."

    dorothy "You shouldn’t let that man get to you."

    hide ScarecrowPlaceholder
    show ScarecrowSad

    scarecrow "But he is not wrong about me."
    scarecrow "I have never been able to help anyone out."

    dorothy "Well, maybe you should just work alone!"

    "For a moment, Scarecrow seems lost in thought at your words. Then his face lights up."

    hide ScarecrowSad
    show ScarecrowPlaceholder
    scarecrow "Hmm... maybe you're right!!"
    scarecrow "I can probably find the murderer of this incident before anyone else too!!"

    hide ScarecrowPlaceholder
    show dorothyPlaceholder at center
    with dissolve

    dorothy "Exactly!!"
    dorothy "...wait"

    "You are happy about helping Scarecrow bounce back, but now you are worried about all the evidence that would be pointing to you."
    "And as you are having these thoughts you watch as Scarecrow is leaving in excitement."

    show dorothyPlaceholder at right
    show ScarecrowPlaceholder at left
    with dissolve

    dorothy "{i}alarmingly{/i} WAIT!"
    dorothy "Um…"
    dorothy "What if I go with you?"
    dorothy "I would love to be there as support."

    scarecrow "But didn’t you just say I should prove myself and that I didn’t need a partner?"

    dorothy "Yeah of course but maybe you just haven’t found the right partner."
    dorothy "And I have always wanted to try being an investigator."

    scarecrow "Hmmmmm..."
    scarecrow "Alright!"

    scarecrow "Let’s crack this case."
    scarecrow "So where to first?"

    dorothy "We should head over to the police station."

    scarecrow "But why would we head there? You know how the lead investigator feels about me."

    dorothy "Forget him, if we’re going to get down to the bottom of this case, we’re going to have to get the evidence ourselves."

    scarecrow "We’ll just get turned away though."

    dorothy "Whoever said anything about asking them?"

    scarecrow "Oh I get ya, let’s head over there now."

    stop music fadeout 1.0

    scene policeQuestioningRoom :  #transition to the police questioning room
        zoom 1.5
    with fade

    play music "audio/forest.mp3" loop fadein 2.0

    "The WW West is in a questioning room. She is being questioned by the Lead Investigator aka “The Wiz” and a forensic officer Tin Man."

    show wizPlaceholder at center
    with dissolve

    wiz "WE UNDERSTAND THAT YOU HAVE SUFFERED A VERY RECENT LOSS, BUT WE JUST WANTED TO KNOW WHERE YOU WERE DURING THE TIME OF YOUR SISTER’S MURDER"

    show wizPlaceholder at left
    show wwWestAngry at right
    with dissolve

    WWWest1 "{i}Silence{/i}"

    wiz "WE KNOW YOUR RELATIONSHIP BETWEEN YOUR SISTER AND YOU WERE A BIT ON THE ROUGH SIDE, BUT DO YOU KNOW ANYONE THAT COULD HAVE HAD A MOTIVE AGAINST HER."

    WWWest "{i}Silence{/i}"

    hide wizPlaceholder
    hide wwWestAngry
    show tinmanPlaceholder at center
    with dissolve

    tinman "{i}whisper{/i} Sir, maybe it’s too soon for this."

    hide tinmanPlaceholder
    show wizPlaceholder at center
    with dissolve

    wiz "{i}ignoring comment{/i} THIS CAMERA WAS FOUND AT THE SCENE OF THE CRIME."

    hide wizPlaceholder
    show wwWestAngry at center
    with dissolve

    "The W. W. West sees the blood on the camera."

    scene black
    with dissolve

    stop music fadeout 2.0

    jump chapter02