# Chapter 6

label chapter06:

    scene dorothysApartment with fade
    show dorothyPlaceholder at center

    "It’s morning and you find yourself being woken up 
    by loud banging on your door. 
    You go to check it out and find two police men waiting by the door."

    policeman1 "Morning"

    dorothy "Morning.  Cany I help you??"

    policeman1 "Yes we need you to come with us 
    to the police station for questioning."

    dorothy "What's this about?"

    policeman2 "We just need you to come with us.
    We can do this the easy way or the hard way.
    It's up to you."

menu chapter6Choice1:

    "Slam the door in their faces":
        "You try to close the door quickly but the closer policeman 
        holds the door open as if he knew what you were thinking"

        jump chapter6Result1

    "Go willingly":
        jump chapter6Result1

label chapter6Result1:

    jump end