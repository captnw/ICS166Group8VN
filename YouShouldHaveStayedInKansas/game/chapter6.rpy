# Chapter 6

label chapter06:

    scene dorothysApartment at truecenter with fade :
        zoom 1.5
    show dorothyPlaceholder at center

    "It’s morning and you find yourself being woken up by loud banging on your door. You go to check it out and find two police men waiting by the door."

    show policeman1Placeholder at left with dissolve

    policeman1 "Morning"

    dorothy "Morning. Can I help you??"

    policeman1 "Yes we need you to come with us to the police station for questioning."

    dorothy "What's this about?"

    hide policeman1Placeholder with dissolve
    show policeman2Placeholder at left with dissolve

    policeman2 "We just need you to come with us. We can do this the easy way or the hard way. It's up to you."

    hide policeman2Placeholder

menu chapter6Choice1:

    "Slam the door in their faces":
        show policeman2Placeholder at left with dissolve

        "You try to close the door quickly but the closer policeman holds the door open as if he knew what you were thinking"

        policeman2 "Nice try, but let's go"

        jump chapter6Result1

    "Go willingly":
        jump chapter6Result1

label chapter6Result1:

    dorothy "Alright, alright, let's go"

    scene black with fade

    if (doYouSuspectYourself):
        "You don’t really know what is going on and can’t help but fear for the worst as you are taken to the police station."
    else:
        "Even after everything you have learned, you still can’t help but feel uneasy about the drive to the police station."

    scene outsidePoliceStation at truecenter with fade :
        zoom 1.5
    show dorothyPlaceholder at right
    show policeman1Placeholder at left

    dorothy "What is going on here? You all have been quiet during the ride here, if you just wanted to ask me questions, just say so right now."

    policeman1 "The lead investigator will be with you in just a moment, right this way."

    "The police officers lead you into a dimly lit room that you’ve stolen evidence from, the interrogation room."

    scene policeQuestioningRoom at truecenter with fade :
        zoom 1.5
    show dorothy at right

    "You wait for what seems like an eternity"

    dorothy "Can we get this over with already?"

    show wizPlaceholder at left with dissolve

    wiz "HEY KIDDO, HOW ARE YOU DOING?"

    dorothy "Uh, doing fine until your goons woke me up and brought me here."

    wiz "IS THAT SO? I JUST WANTED TO BRING YOU BACK HERE, I KNOW YOU MISSED THIS PLACE AND YOU WANTED TO BE HERE?"

    dorothy "What are you even talking about?"

    wiz "DON’T PLAY DUMB WITH ME, ONE OF OUR POLICE OFFICERS SAW YOU AND SCARECROW LEAVING THE STATION THE OTHER DAY, THE SAME DAY WHICH OUR MAJOR PIECES OF EVIDENCE HAD GONE MISSING."

    dorothy "..."

    wiz "REALLY? WE CAUGHT YOU RED HANDED AND YOU’RE NOT EVEN GOING TO TRY AND DEFEND YOURSELF?"

menu chapter06Choice1:
    # IS THIS CORRECT?
    "I don’t think I’m the one that should be defending myself" if hasCollectedRedShoesPhoto and hasListenedToLionsTestimony and hasCollectedCamera and didYouGiveScarecrowTape and hasCollectedTinManNote and hasListenedInOnWitchCh4 and hasCh4Happened and not doYouSuspectYourself:
         jump chapter06Result1_1

    "We were just looking for the murderer.":
        jump chapter06Result1_2

    "Other than that, you have nothing else on me.":
        jump chapter06Result1_3

label chapter06Result1_1:
    wiz "WHAT DO YOU MEAN?"

    dorothy "You’re the murderer."

    wiz "THAT’S A BOLD ACCUSATION, BUT I’LL HUMOUR YOU, I’LL ANSWER YOUR DUMB QUESTIONS."

    dorothy "\"Bottom of heirloom hold down\""

    wiz "I DON’T KNOW HOW YOU’VE OBTAINED THAT, BUT THAT’S MY NOTE FROM MY PRIVATE OFFICE. THAT’S NOT REALLY ENOUGH TO EVEN IMPLICATE ME."

    dorothy "Well, it’s related to the Witch sisters you see."

    dorothy "I’ve overheard you interrogating the Wicked Witch of the West on the importance of these red shoes."

    wiz "THAT’S JUST STANDARD PROCEDURE, WE PRESUMED THAT THE SHOES WERE A POSSIBLE MOTIVE FOR THE MURDER."

    dorothy "Since the red shoes were part of a family heirloom, and the sisters were related by blood, you could say that the red shoes are part of the Wicked Witch of the West’s family heirloom."

    dorothy "And isn’t the handwriting on that note, your writing?"

    wiz "EVEN IF IT IS {i}puts away the document{/i} in front of him*, I’M NOT SURE WHERE YOU’RE GOING WITH THIS."

    dorothy "It’s the instructions to open the secret compartment within the red shoes, and that allows one to access something very important to you and the witch sisters."

    dorothy "But why would YOU know anything about the precious heirloom?"

    wiz "..."

    dorothy "You confronted the Wicked Witch of the East about the red shoes, suspecting that it must have been valuable in some way."

    dorothy "She wouldn’t yield of course, so you intimidated her."

    dorothy "But intimidation didn’t work, so you used violence, and you’ve obtained the knowledge on how to access the heirloom in the red shoes."

    dorothy "You couldn’t leave any witnesses, so you killed her to cover it up."

    dorothy "You were deciding on how to cover this up, when my camera apparently falls from the sky and lands somewhere nearby."

    dorothy "You take advantage of this, and you take the camera and smash it into the deceased victim’s head a few times so that it may seem as the murder weapon."

    dorothy "Your murder weapon, the camera, was perfect because you would have framed it on me, the camera’s owner."

    dorothy "If that didn’t work, you could have framed the victim’s sister and use the shoes as the motive for the killing."

    dorothy "You thought you had an airtight plan, but I figured you all out!"

    "You glare at the Wizard, and the Wizard glances at you, and takes off his hat. You can now see that a shriveled, old man lies before you with fear in his eyes."

    wiz "you can’t tell anyone about this."

    dorothy "Why not? You already killed a person, ruined her sister’s life, what’s to stop you from ruining one more? You crazy old man."

    wiz "do you even know how much that heirloom is worth?"

    dorothy "No, I didn’t even look at the heirloom."

    wiz "it’s a rare jewelry that’s worth $1.5 million pounds"

    dorothy "Wait, how would you know this, the heirloom was still in the shoe?"

    wiz "I took the heirloom from the shoe temporarily and got it appraised at a place overnight, the same night you tried to break into the police station."

    wiz "look Dorothy, you and I are similar-"

    dorothy "Don't even compare yourself to me."

    wiz "alright, at the end of the day there is still money involved."

    wiz "I’ll let you take half of the value of the jewelry once it’s sold, and I’ll leave you and all of your friends alone."

    dorothy "... in return for what?"

    wiz "I want the Wicked Witch of the West to go to jail, so neither of us would have to go. Then I’ll leave town, wire you the money, and then we’ll both never speak of this incident ever again."

menu chapter06Choice1_1:
    "Take a share of the offered treasure":
        jump chapter06Choice1_1_1

    "Don't take the treasure":
        jump chapter06Choice1_1_2

label chapter06Choice1_1_1:
    dorothy "Alright"

    wiz "so what's it going to be?"

    dorothy "I will go along with your plan for the money"

    # IS THIS CORRECT?
    if didYouGiveScarecrowTape:
        dorothy "But you have to give scarecrow a chance at the academy"

        wiz "why do you bother with him?? he can’t do anything right."

        dorothy "That's just because you never gave him a chance, but he is extremely smart and has amazing instincts"

        wiz "very well, i will do as you say"

    wiz "so remember you will have the money once that woman is in jail."

    dorothy "Fine"

    wiz "{i}sinisterly{/i} GOOD"

    scene black with fade

    "Couple days later you hear the witch goes to jail, but that there was an accomplice with her and that the police are still tracking them down."

    "You find that very weird, but decide not to worry about it and just think about what you will do with the money you will get."

    scene dorothysApartment at truecenter with fade :
        zoom 1.5
    show dorothyPlaceholder

    "You hear knocking at your door and when you open it you are grabbed by the police."

    show policeman1Placeholder at left with dissolve

    policeman1 "You are being taken on to custody for the murder of W.W. WEST"

    dorothy "{i}frantically{/i} I don’t understand!! I didn’t do anything!!"

    policeman1 "Yeah sure save it for the judge!!"

    scene outsidePoliceStation at truecenter :
        zoom 1.5
    show dorothyPlaceholder at left with dissolve
    show wizPlaceholder at right with dissolve

    "As you are being taken to the police car, you see the Wizard smiling sinisterly towards you and walking away."

    dorothy "Nooooo! It wasn’t me!! It was the Wizard!! Wait! You have to believe ME!!"

    "But no one listened. All you got were cold stares as you were being taken in."

    scene black with fade

    "You and the Wicked Witch of the West were tried for the murder of the Wicked Witch of the East. You were both found guilty and sentenced to 20-30 years in prison."

    "BAD END - FOOLED BY THE MONEY"

    jump end

label chapter06Choice1_1_2:
    dorothy "No"

    wiz "what!!?"

    dorothy "NOOO! I am pretty sure I said it clearly for you to understand!!"

    wiz "why not!!??  don’t you want the money!!?"

    dorothy "Of COURSE, but not enough to let you get away with what you have done!!"

    wiz "wha-"

    dorothy "Because of you I thought I had done an unspeakable thing!! Because of you I had to use the kindness of Scarecrow to clear my name!!"

    dorothy "Because of you I had to worry about how much time I had left!! And YOU killed someone!! YOU DID IT!! It was you the whole time!!"

    wiz "Be quiet!!! I did what had to be done! she did not hand over the shoes when i told her too!! she forced my hand!!  I had to kill her!!"

    dorothy "You are just pathetic!! Acting like you are some grand person when in reality you are just a small old man!!"

    wiz "SILENCE!!!"

    dorothy "{i}shocked{/i}"

    wiz "FINE, I WON’T FORCE YOU TO TAKE THE MONEY. I WAS NEVER GOING TO GIVE YOU A CENT ANYWAYS. EITHER WAY I WILL PIN EVERYTHING ON YOU AND I WILL MAKE SURE YOU SPEND THE REST OF YOUR LIFE BEHIND BARS."

    dorothy "You can’t do that! I have proof that you did it!"

    wiz "DO YOU REALLY THINK ANYONE WILL BELIEVE YOU OVER ME!!?"

    wiz "HAHAHAHAHA!!!"

    wiz "I AM “THE WIZ”. YOU ARE JUST A LITTLE GIRL."

    wiz "NO ONE WILL QUESTION ME."

    "All you can do is watch in horror as the wizard says this because he was right. Who would believe you? You found out who it was, but in the end you are still going to be the one to take the blame."

    "Just as you were panicking, the door creaks open and you see Scarecrow playfully swinging on the door. You can also see Tin Man just outside and a few others that you can’t quite make out."

    dorothy "Scarecrow?"

    wiz "WHAT ARE YOU DOING HERE!!? TIN MAN GET THIS BOY OUT OF MY SIGHT!"

    tinman "I don't think I will"

    wiz "WHAT?!?"

    wiz "HOW DARE YOU!?"

    wwwest "NO, HOW DARE YOU!!?  YOU MURDERER!!"

    wiz "WHAT!!!?"

    "You see Scarecrow make his way inside the questioning room with a pipe on his lips blowing bubbles. And then you see everyone else come in as well."

    "There's Tin Man, WW West, Lion, and some other police officers."

    wiz "WHAT IS GOING ON HERE?!!?"

    scarecrow "Funny you should ask. Let me explain."

    scarecrow "{i}Deep Breath{\i}"

    scarecrow "Sooooo!! Me and Dorothy were working this case:"

    scarecrow "Stole some evidence,"

    scarecrow "Got some people chatting,"

    scarecrow "Broke into some property,"

    scarecrow "Stole more evidence,"

    scarecrow "Talked about said evidence,"

    scarecrow "Then I developed some key evidence,"

    scarecrow "And said \"OH!\""

    scarecrow "Which is why I called everyone here on this fine day!!"

    wiz "WHAT?"

    dorothy "What?"

    tinman "{i}sigh{\i} He explained it the same way to us at the beginning, but he will get to the point of it all, just hear him out."

    wwwest "Just get on with it, Scarecrow."

    lion "Yes, get on with it. I don't like being here."

    scarecrow "I have to build suspense."

    "He puffs on his bubble pipe some more."

    scarecrow "Every bit of evidence we gathered did not really make sense until the final piece which is now in my hand."

    scarecrow "This photo that I developed last night. As you can see, it is a little blurry due to the velocity and impact of the camera. But you can clearly see a coat that is none other than that of the LEAD INVESTIGATOR!!!"

    wiz "ANYONE CAN BE WEARING A COAT-"

    scarecrow "You're right, but no one in their right mind would want to copy the exact coat you always seem to wear."

    wiz "But I always wear a hat and this person is not-"

    scarecrow "Also a valid point. Unless we take off yours. Then we may or may not see the similarities."

    wiz "I WILL NOT UNDRESS JUST FOR YOUR AMUSEMENT!! SOMEONE TAKE THIS BUFFOON AWAY FROM ME!!"

    scarecrow "Very well, but then we have the note Tin Man gave us. Your note."

    wiz "WHAT NOTE?!"

    scarecrow "The one about the shoes do you not remember??"

    wiz "THAT WAS NOT ME!!"

    scarecrow "But it is your exact writing. And it has writing about red shoes, the same ones the WW East wore when whe was murdered."

    wiz "SHE WAS NOT WEARING ANY SHOES WHEN WE FOUND HER BODY-"

    scarecrow "Key word when you found the body. The motive was always the shoes because they had something worth more than her life. Right?"

    wiz "WHAT NO!!?"

    scarecrow "WW West you wanted them found because they were a family heirloom right??"

    wwwest "Yes."

    scarecrow "But the shoes themselves were just a disguise for something much bigger. Right?"

    wwwest "Right."

    scarecrow "A rich family's fortune, correct?"

    wwwest "Yes."

    scarecrow "And no one should have known about it, correct?"

    wwwest "Yes, it was supposed to be a secret passed on to the next heir. My sister."

    scarecrow "So why did the note that you wrote have so much detail on the shoe? Anyone else that saw this note would be very confused unless they knew about the family heirloom, correct Tin Man?"

    tinman "Yes. That is exactly what happened when I first saw it, which is why I gave it to you two."

    scarecrow "Indeed you did and it was not until we went to the Mansion that we found more about this heirloom."

    wiz "WHAT NO"

    scarecrow "Yes the camera was Dorothy's but she was not the murderer, it was you."

    wiz "THAT IS OUTRAGEOUS!! IT WASN'T ME!! THIS IS WRONG"
    # panicked look??

    lion "That's the voice!! That's the voice I heard!! You were the man with those eyes!!"

    scarecrow "Take him away, boys."
    # points at police officers, then wizard

    wiz "No! I am the lead investigator!! You can't do this to me!"

    "As the lead investigator's hat is blown away by a gust of wind, the wizard is revealed to be a small, insignificant, little man."

    "He looks around frantically as he is escorted away by the police officers."

    dorothy "Wow Scarecrow. You really are amazing."

    scarecrow "Was there ever a doubt?!"

    scene black with fade

    "A few days later after the trial you see the newspaper flooding with the WIZARD's face and headlines saying \"Former Lead Investigator charged with murder sentencing him to life in jail\"."

    dorothy "Wow, that was too crazy!! Next time I think I will just stay in Kansas."

    "GOOD END - MURDERER GOES TO JAIL"

    jump end

label chapter06Result1_2:
    wiz "REALLY? DID YOU FIND OUT WHO IT WAS?"

    wiz "WAIT, WAIT. I DON'T CARE."

    dorothy "I wasn't going to tell you anyways."

    wiz "WHATEVER. LET ME TELL YOU HOW IT'S GOING TO GO."

    jump chapter06PathB

label chapter06Result1_3:
    wiz "WRONG. YOU STILL HAVE THE EVIDENCE YOU STOLE FROM OUR POLICE STATION."

    wiz "AS A RESULT OF YOU STEALING OUR EVIDENCE, YOU'VE TRESPASSED IN THE STATION AND YOU'VE DELAYED THE INVESTIGATION."

    wiz "IN SHORT, YOU'VE WASTED MY TIME."

    dorothy "Well I don't have the evidence on me right now."

    wiz "I KNOW, I'VE SENT MY OFFICERS TO SCARECROW'S APARTMENT."

    wiz "WE'VE RECLAIMED THE EVIDENCE, AND I COULDN'T BELIEVE WHAT I SAW."

    wiz " LET ME SHARE WITH YOU WHAT'S GONNA HAPPEN NOW."

    jump chapter06PathB

label chapter06PathB:
    wiz "I THINK YOU MIGHT BE INVOLVED IN THE MURDER OF A WICKED WITCH OF THE WEST."

    dorothy "Really? And how are you going to prove it?"

    wiz "TAKE A NICE GLIMPSE OF THIS PHOTO."

    "The photo is your selfie."

    dorothy "You're gonna have to do better than that?"

    wiz "DID YOU KNOW WHERE THAT SELFIE CAME FROM? YOUR CAMERA/ THE SAME CAMERA THAT WAS USED AS THE MURDER WEAPON."

    dorothy "Hmph."

    wiz "SO WHY DID YOU DO IT?"

    dorothy "I... I din't do it."

    wiz "THE EVIDENCE SAYS OTHERWISE. WHY ARE YOU MAKING THIS SO HARD FOR YOURSELF?"

    wiz "IF YOU ADMIT THAT YOU DID IT AND COOPERATE WITH US, YOU MAY RECEIVE A LIGHTER SENTENCE."

menu chapter06Choice2:
    "Say nothing":
        jump chapter06Choice2_1

    "Try and kill the wizard":
        jump chapter06Choice2_2

label chapter06Choice2_1:
    dorothy "I'm not cooperating with you."

    wiz "SEE YOU IN COURT, IDIOT."

    scene black with fade

    "Despite fighting earnestly, the courts were rigged in the Wizard's favor. You and the Wicked Witch of the West were tried for the murder of the Wicked Witch of the East. You were both found guilty and sentenced to 20-30 years in prison."

    "BAD END - WRONGLY IMPRISONED"

    jump end

label chapter06Choice2_2:
    dorothy "But I didn't do anything."

    "The Wizard gets right in front of your face and you can see the madness in his eyes."

    wiz "STILL TRYING TO ACT INNOCENT ARE YOU??!"

    dorothy "{i}low voice{\i} I am innocent."

    wiz "WHAT WAS THAT??? SPEAK UP!!"

    dorothy "{i}shouting{\i} I AM INNOCENT!!"

    wiz "SO YOU SAY BUT EVERYTHING POINTS TO YOU!!"

    dorothy "NOOO!!"

    wiz "YES AND IT DOESN'T MATTER WHAT YOU SAY ANYMORE! I WAS TRYING TO GIVE YOU A CHANCE AT A SHORTER SENTENCE BUT IN THE END I SEE YOU PREFER TO PLAY DUMB TO THE VERY END."

    "You see the Wizard slowly turn towards the door, but you quickly lunge at him with your chair hitting him in the back."

    "His gun slips out of his coat and you attempt to grab it, but he was quick to react and shoves you away."

    "*Bang*"

    "You feel a sharp pain on your side and fall to the ground."

    "Blood starts spilling on the floor and you can barely see the Wizard coming closer towards you."

    "He squats down next to you and starts snickering."

    wiz "THIS TURNED OUT BETTER THAN I THOUGHT. NOT ONLY WILL YOU TAKE THE BLAME FOR THE MURDER, BUT YOU WILL NOT EVEN BE ABLE TO CLEAR YOUR NAME. HAHAHA!"

    wiz "AH, WHY THE CONFUSED FACE?! OHHHH, I SEE HAHA I GUESS I SHOULD TELL YOU."

    "He leans closer to your ear and whispers to you:"

    wiz "{i}I killed that witch.{\i}"

    wiz "HaHaHAHAHAHA"

    "You no longer feel any pain. Instead you feel the anger fueling your body and all you can think about is the gun in his hand."

    "You reach for the gun just inches away from you and pull the trigger."

    "*Bang*"

    "The laughter that came from the Wizard stopped, and you look to see the shock in his face as he falls."

    dorothy "Guess what Wizard? You were right. I-"

    dorothy "did murder-"

    dorothy "some- one..."

    scene black with fade

    "You and the Wizard were both found dying by the police officers after the commotion."

    "In your dying thoughts, you thought you could have made some better choices in the events leading up to this one."

    "You both died before an ambulance was able to arrive."

    "BAD END - MURDER SUICIDE"

    jump end
