# Chapter 6

label chapter06:

    scene dorothysApartment at truecenter :
        zoom 1.5
    show dorothyPlaceholder at center
    with fade

    "It’s morning and you find yourself being woken up 
    by loud banging on your door. 
    You go to check it out and find two police men waiting by the door."

    show policeman1Placeholder at left

    policeman1 "Morning"

    dorothy "Morning.  Cany I help you??"

    policeman1 "Yes we need you to come with us 
    to the police station for questioning."

    dorothy "What's this about?"

    hide policeman1Placeholder
    show policeman2Placeholder at left

    policeman2 "We just need you to come with us.
    We can do this the easy way or the hard way.
    It's up to you."

    hide policeman2Placeholder

menu chapter6Choice1:

    "Slam the door in their faces":
        show policeman2Placeholder at left

        "You try to close the door quickly but the closer policeman 
        holds the door open as if he knew what you were thinking"

        policeman2 "Nice try, but let's go"

        jump chapter6Result1

    "Go willingly":
        jump chapter6Result1

label chapter6Result1:
    
    hide policeman2Placeholder

    dorothy "Alright, alright, let's go"

    hide dorothyPlaceholder

    if (doYouSuspectYourself):
        "You don’t really know what is going on 
        and can’t help but fear for the worst 
        as you are taken to the police station."
    else:
        "Even after everything you have learned,
        you still can’t help but feel uneasy 
        about the drive to the police station."

    jump end