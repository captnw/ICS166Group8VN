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

    scene black with fade

    if (doYouSuspectYourself):
        "You don’t really know what is going on 
        and can’t help but fear for the worst 
        as you are taken to the police station."
    else:
        "Even after everything you have learned,
        you still can’t help but feel uneasy 
        about the drive to the police station."

    scene outsidePoliceStation at truecenter with fade :
        zoom 1.5
    show dorothyPlaceholder at right
    show policeman1Placeholder at left

    dorothy "What is going on here? 
    You all have been quiet during the ride here, 
    if you just wanted to ask me questions, just say so right now."

    policeman1 "The lead investigator will be with you in just a moment, 
    right this way."

    "The police officers lead you into a dimly lit room 
    that you’ve stolen evidence from, the interrogation room."

    scene policeQuestioningRoom at truecenter with fade :
        zoom 1.5
    show dorothy at right

    "You wait for what seems like an eternity"

    dorothy "Can we get this over with already?"

    show wizPlaceholder at left
    
    wiz "HEY KIDDO, HOW ARE YOU DOING?"

    dorothy "Uh, doing fine until your goons woke me up 
    and brought me here."

    wiz "IS THAT SO? I JUST WANTED TO BRING YOU BACK HERE, 
    I KNOW YOU MISSED THIS PLACE AND YOU WANTED TO BE HERE?"

    dorothy "What are you even talking about?"

    wiz "DON’T PLAY DUMB WITH ME, ONE OF OUR POLICE OFFICERS 
    SAW YOU AND SCARECROW LEAVING THE STATION THE OTHER DAY, 
    THE SAME DAY WHICH OUR MAJOR PIECES OF EVIDENCE HAD GONE MISSING."

    dorothy "..."

    wiz "REALLY? WE CAUGHT YOU RED HANDED 
    AND YOU’RE NOT EVEN GOING TO TRY AND DEFEND YOURSELF?"

menu chapter06Choice1:
    "I don’t think I’m the one that should be defending myself" if hasCollectedRedShoesPhoto and hasListenedToLionsTestimony and hasCollectedCamera and didYouGiveScarecrowTape and hasCollectedTinManNote and hasListenedInOnWitchCh4 and hasCh4Happened and not doYouSuspectYourself:
         jump chapter06Result1_1

    "We were just looking for the murderer.":
        jump chapter06Result1_2
    
    "Other than that, you have nothing else on me.":
        jump chapter06Result1_3

label chapter06Result1_1:

label chapter06Result1_2:

label chapter06Result1_3:

    jump end