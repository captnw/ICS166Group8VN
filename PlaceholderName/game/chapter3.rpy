# Chapter 3

# define a character here, once defined, these
# are shared with all .rpy scripts
define bartender = Character("Bartender", color="#bfbfbf") 

# placeholder character portraits
image ScarecrowPlaceholder = Placeholder("boy")
image dorothyPlaceholder = Placeholder("girl")

# placeholder bg
image randomStreet = Placeholder("bg")
image outsideMunchkinBar = Placeholder("bg")
image insideMunchkinBar = Placeholder("bg")

label chapter03:

    # running audio cue here

    # street bg here

    "You find yourselves on a busy, well-lit street. It begins to rain softly."

    # dorthy portrait show

    dorothy "{i}pant{/i} {i}pant{/i} ...I think we're safe now"

    # scarecrow portrait show here, dorthy portrait moves to left side, while
    # scarecrow portrait's move to right side

    scarecrow "{i}pant{/i} ...They won’t be able to find us on this street anyways. We can spot them before they see us, and by the time they’ve reached us, we’ll just blend into the crowd."

    dorothy "You sound like you know a thing or two about running away from other people."

    scarecrow "Well, if you ever become an expert detective like myself, then you’ll learn to pick up a few skills of the trade."

    dorothy "Of course! All legitimate detectives would sneak into police stations and steal evidence, instead of just asking someone for the evidence. If only there was some form of bureaucracy in place to facilitate this transfer of information."

    scarecrow "LOOK, you don’t understand how jealous this district’s police force are of my amazing detective skills. They’re probably afraid of me getting all the credit for all the cases I will solve if they let me get my hands on the evidence."

    dorothy "Does this mean you haven’t solved a single case yet?"

    scarecrow "Well … I would have, but they didn’t let me examine the evidence we gathered for any cases yet. Say, what did the Tin Man hand you earlier?"

    dorothy "I’m not sure what to make of it. We can examine it later, is there any place where we can find shelter? I’m not familiar with this part of town."

    scarecrow "I was thinking we head to my place, but I’d like to make a quick stop at the Munchkin’s bar and grille for a quick snack."

    dorothy "Lead the way."

    # transition here
    # show inside bar bg

    "You've stepped inside the bar to find out that despite being open, the bar seemed almost empty. The tables are all laid out, the room is well-lit, and there is a bartender cleaning glassware in the corner of the room."

    scarecrow "And we’re finally here!"

    dorothy "Can’t we just head straight to your place? I’d like to examine the photo as soon as possible."

    scarecrow "I just need some grub, you can’t think on an empty stomach, Dorothy."

    dorothy "I guess I’ll order something as well … wait do you see that bartender?"

    scarecrow "You mean that big, animal looking fellow?"

    dorothy "Yeah, he was at the crime scene that other day."

    scarecrow "Dorothy, there were a lot of onlookers at that crime scene."

    dorothy "I mean he was there when it happened! I was walking through that path earlier that evening and I found him sweeping the streets."

    scarecrow "Let’s go up to him and ask some questions about what happened."

menu chapter03Choice:
    "What should I say...?"

    "You can’t just walk up to people and ask something like that.":
        jump chapter03A

    "Sounds like a good idea.":
        jump chapter03B

label chapter03B:

    "You and Scarecrow walk up to the bartender, who is currently occupied with cleaning glassware"

    scarecrow "Excuse me, can I ask you a question?"

    "The bartender turns around, he's a giant lion-looking fellow that is wearing brown suspenders."

    "You can tell that he's struggling to clean the glassware since he can't quite reach inside the cups with his giant paws"

    bartender "can i help you with something?"

    scarecrow "Hi, where were you when the wicked witch of the east die-"

    dorothy "*This is probably way too direct, he should try to be a bit more subtle with his questioning*"

    dorothy "I think what my friend here was trying to say is that we’re independent detectives employed by the Wicked Witch of the West to find out about the circumstances about her sister’s death."

    scarecrow "*I see what you're trying to do, nice thinking Dorothy!*"

    scarecrow "Right, and we were informed by various sources that you may have been around the scene when it occurred, so could you please tell us what happened on that night?"

    bartender "i’ve already explained what i know to the local police department, can’t you just ask them for my account?"

    scarecrow "Uh … they’re currently busy at the moment, this type of information would be vital for-"

    bartender "i’ve told you, i’ve already explained it to some other people, i-"

    dorothy "Look here mister, if you don’t want any trouble, just say what you know and we’ll both go on our merry ways. "

    bartender "(whispering) i forgot, i’m sorry, i tend to forget things when it all seems to be really intense, like right now!"

    dorothy "What did you say? SPEAK UP. We need answers right now!"

    "You flip over a table and kick over a chair to indimidate the bartender further."

    scarecrow "Dorothy, what are you doing!?"

    dorothy "Scarecrow, we’re not going to get answers at this rate until he realizes that there’ll be consequences."

    dorothy "Still don’t remember, huh?"

    bartender "i’m sorry, i’m sorRY, i’m..i-i’m...I’M-"

    dorothy "Maybe you need some encouragement, if you don’t spill the beans I’m going to kick you in the -"

    bartender "...REALLY PISSED OFF."

    dorothy "Wha-"

    bartender "YOU COME INTO MY SHOP. I TREAT YOU POLITELY AND THEN YOU ASK TOO MANY QUESTIONS ABOUT SOMETHING I DON'T WANT TO TALK ABOUT AND THEN YOU BREAK MY FURNITURE." 

    scarecrow "This is just a big misunderstanding … you see we-"

    "The bartender quickly puts the mug down and slams his hands on the counter"

    bartender "YOU BUFFOONS NEED TO GET OUT OF MY SHOP, RIGHT NOW."

    scarecrow "Wait before we go … could I order some fish and chips."

    bartender "NO, I NEVER WANT TO SEE YOU NOR HER EVER AGAIN. GET OUT, BEFORE I GIVE YOU SOMETHING ELSE TO THINK ABOUT."

    "You and Scarecrow left the store immediately just as the bartender was climbing over the counter"

    "You both run until the store is out of view."

    scarecrow "Nice going Dorothy."

    dorothy "I didn’t think he had it in him ..."

    dorothy "But besides that, you don’t understand that we need to get to the bottom of this crime case. It’s been a few days and we still don’t know who the killer is."

    dorothy "It’s a bit unfortunate, but if people won’t cooperate with us, we’ll have to take matters into our own hands."

    scarecrow "I suppose you’re right … Still, I felt like we could have handled that better."

    dorothy "Whatever, let’s just head on over to your place."

    jump chapter05 # go to chapter 5

label chapter03A:

    dorothy "I think we should be a bit more subtle … let’s just order some grub and we’ll let him do the talking."

    scarecrow "What do you mean?"

    dorothy "You’ll see what I mean."

    "Scarecrow waves to the bartender."

    scarecrow "BARTENDER, I’D LIKE TO ORDER SOMETHING."

    bartender "you don’t have to shout, I’m right here."

    scarecrow "I’d like some pie and mash, {i}ooh{/i} and a bottle of liquor on the side."

    bartender "Coming right up!"

    # fade to black

    "Several bottles and plates later..."

    # fade back in
    
    scarecrow "Yep, that hit the spot."

    bartender "Wow, that was a lot of food. Can you pay the bill for that?"

    scarecrow "I uh… "

    scarecrow "(Dorthy! Can you cover for my meal, I forgot to bring cash)"

    dorothy "(What? No, I didn’t eat a single thing … but we can always dash.)"

    dorothy "We got the bill covered. Were you there for that crime scene that other day?"

    bartender "You mean the one where there was a dead lady with a smashed head on the street?"

    bartender "I think her name was - the Wicked Witch of the West. I didn’t like her that much, but nobody deserves a fate like that, not even her."

    scarecrow "{i}munch munch{/i} You didn’t like her?"

    bartender "It’s a bit personal, so I won’t talk about that."

    bartender "But something you might be interested in is, get this, that I saw her in the evening before her death."

    dorothy "What? Did you talk to her as well?"

    bartender "No of course not, I’m aware of her reputation around these parts, I didn’t want to get in her way."

    scarecrow "{i}munch{/i} Do tell us more! {i}sips{/i}"

    bartender "I was there at that time because I was working my second job - as a janitor - and I was sweeping the same places I’ve always been sweeping."

    bartender "When suddenly I’ve heard a commotion in the alley nearby."

    bartender "I’ve rushed over to check and see what is going on, and I saw the witch arguing with another person."

    bartender "I could have sworn I’ve heard that person yell “I need those shoes!” to which she responded “No, you can’t have them!”"

    bartender "Then I’ve heard yelling and sounds of a struggle, so I’ve started climbing over the fence to help."

    bartender "It was at that point when the stranger’s eyes met mine, and I felt a chill go down my spine."

    bartender "The eyes seemed crazed yet filled with intent, that every action the stranger has planned everything they’ve done so far."

    bartender "I felt … I knew that if I tried to intervene there would be two casualties that day instead of one … so I ran away."

    bartender "I showed up the next day, I wanted to believe despite everything that it was going to be another normal day, that she got away."

    bartender "Reality confirmed my fears when I saw the crowd, and I’ve discovered what you both probably saw at that crime scene that fateful day."

    scarecrow "What did the stranger look like?"

    bartender "Tall fellow wearing a coat with crazed eyes. The alley was dimly lit so I couldn’t catch any of his other features, but I’m pretty sure the voice I heard was a male’s voice."

    dorothy "So instead of helping you just ran away? Did you try getting help?"

    bartender "I had nobody else to contact but the police, and I’m not on good terms with them…"

menu chapter03AChoice:
    "What should I say...?"

    "Po-lice? Sounds more like POOR-lice, because they have poor ties with their community. Hahah, I’ll see myself out.":
        jump chapter03AA

    "How do we know you’re telling the truth?":
        jump chapter03AB

label chapter03AB:

    bartender "Well … you gotta believe me, I was just working as a janitor and I’ve told you all I’ve heard and seen."

    scarecrow "Yeah Dorthy, his story checks out to me, besides don’t you have a janitor badge or something. {i}sip{/i}"

    bartender "Yes, here it is {i}presents badge{/i}."

    dorothy "But you still {b}ran away{/b}."

    bartender "Out of fear! I couldn’t stand that stranger's eyes!"

    dorothy "You {b}didn’t contact anyone.{/b}"

    bartender "There wasn’t anyone I could rely on!"

    scarecrow "Uh Dorthy, why don’t we order something for you-"

    dorothy "...and you even admitted that you {b}disliked the wicked witch of the west{/b}."

    bartender "THAT’S A PERSONAL MATTER!"

    dorothy "How can we be sure that you’re not an accomplice or even the murderer?!"

    bartender "This is why I hate know-it-alls like you! I just tell you what I’ve observed, and yet you want more from me!"

    bartender "You want to know everything, but here’s the problem - I DON’T KNOW EVERYTHING, I JUST KNOW WHAT I KNOW, YOU’RE JUST TRYING TO OBTAIN BLOOD FROM A STONE, LADY."

    dorothy "Look, we just want to discover the truth-"

    bartender "I GAVE YOU THE TRUTH, I’M NOT GONNA SIT HERE AND ANSWER ANY MORE OF YOUR DUMB QUESTIONS IF YOU’RE NOT GONNA LISTEN."
    
    scarecrow "Please forgive my friend, I think we just got off on the wrong foot-"

    bartender "WHAT’S MORE, YOUR STRAW-LOOKING FRIEND OVER HERE STILL HAVE AN UNPAID BILL AFTER EATING 5 PLATES OF FOOD."

    scarecrow "Dorothy?! What should we do!?"

    dorothy "*We’re clearly not getting any more answers from this person, might as well leave.*"

    dorothy "About the payment, why don’t you ask your mum? HA-HA-HA"

    "The bartender starts rolling up both of his sleeves."

    dorothy "Time to leave."

    "Dorthy grabs Scarecrow and they both run out of the store."

    scarecrow "Nice … comeback?"

    dorothy "Yeah just thought of it on the spur of the moment."

    dorothy "But besides that, you don’t understand that we need to get to the bottom of this crime case. "

    dorothy "This bartender guy’s story is shabby at best, there were so many times he could have reached out to someone else but he just didn’t."

    scarecrow "Still, we haven’t examined the evidence yet, so we can’t exactly jump to conclusions..."

    scarecrow "But, I felt like we could have handled that better on our part."

    dorothy "Whatever, let’s just head on over to your place."

    jump chapter05 # go to chapter 5

label chapter03AA:

    scarecrow "I like bad jokes, but that was just terri-"

    bartender "HAHAHAHAHAHAH."

    bartender "Sorry bad jokes just get to me, ha-ha."

    scarecrow "Well besides the bad joke, I’m glad that you’ve made it out fine."

    dorothy "Yeah, and even though the information isn’t particularly THAT useful, it was interesting."

    bartender "And you two aren’t bad know-it-alls yourself, even though you aren’t police detectives."

    scarecrow "Huh, what gave it away? Didn't you believe that we were detectives?"

    bartender "At first I was thoroughly convinced because I’m not sure who else would just show up to this empty bar during the middle of a skeleton shift."

    bartender "But you downed several meals, and your lady friend made a terrible - albeit strong attempt - at a joke. So now I’m not sure who you all are..."

    bartender "But now I don’t mind that you’re asking questions, it’s just that it's different when it's the police asking them."

    bartender "Everything’s serious with those police officers, can’t relax around them. Even if you tell them, they’ll always ask for me."

    bartender "I feel that’s enough talk about crimes and questioning for one evening. Say, why don’t I tell you my backstory instead?"

    scarecrow "Sure! Tell us right away!"

menu chapter03AAChoiceJoke:
    "Should I listen to the bartender's story?"

    "Yes":
        jump chapter03AAContinued

    "Yes, but with more enthusiasm.":
        jump chapter03AAContinued


label chapter03AAContinued:

    dorothy "Uh I think I have to listen anyways because I don’t have a choice-"

    bartender "Before my jobs as a bartender and janitor, I was a well known circus performer going by the stage name 'The daring Lion'. You two can just call me {b}Lion{/b}."

    lion "I’ve always done majestic and seemingly dangerous acrobatics. I’ve walked across tightropes, jumped through wheels of fire, while always doing it with a grace."

    lion "Mind you the acrobatics weren’t that dangerous, everything was planned for and it was mostly safe. A trick you can do only once isn’t really that impressive."

    lion "It was more about the performance, the style and grace, if you got that down, you sold the act. It may be common knowledge nowadays, but back then the audience that everything happening in the circus was an incredible, amazing act."

    lion "Then the magic was lost, people found out how it was done. We tried to deny it at first, but eventually the loss of revenue made the circus owner take out all the safety precautions to promote 'genuine acrobatics'."

    lion "The people did come back, but now all the circus performers are facing real dangers, one mistake can lead to a loss of life."

    lion "I was faced with a decision, to stay and perform for the circus, or to leave."

    scarecrow "Couldn’t you have gone to the authorities that were responsible for safety regulations?"

    lion "It really didn’t occur to me at the time, many of us working there weren’t familiar with our worker rights and what or what isn’t acceptable. All circus owners are in cahoots together and like to keep it this way, so if anyone spoke out or threatened to bring in the authorities, they’d be blacklisted from the industry."
    
    dorothy "...So the authorities weren’t capable of handling this issue?"

    lion "It wasn’t that they can’t clean up the mess, but that they had other problems at hand. It took several incidents and a nationwide protest before we were able to close down the industry for good."

    lion "But before all of that happened, I already left that profession for several years … I couldn’t stand it anymore."

    lion "I became a janitor soon after setting foot in London, and now I’ve been a bartender for several months now."

    lion "My only regret is not standing up for myself and the other performers. We should have closed there and then when we lifted the safety precautions."

    dorothy "I’m not sure if you’re aware of this, but the circuses are still operating."

    lion "The ones that you’ve attended are abiding by the new regulations there were drafted after the many incidents of the previous industry occured."

    lion "Which reminds me, I’ve only found that my circus closed after several months, and by then it was too late for me to reunite with any of my fellow performers. I’ve attended several circuses for years now, but I’m still not able to find my fellow colleagues."

    scarecrow "Surely, you must have reconnected with one of them?"

    lion "To this day, I don’t know where they are. I just hope they’re doing fine."

    lion "… Thank you for listening to my story. I really do appreciate it."

    lion "While the information I gave you may not be that helpful, why don’t you try stopping by the Wicked Witch of the East’s mansion and asking her some questions, maybe she’ll know more about what happened on that day."

    dorothy "We were thinking about that too, but we don’t know where she lives."

    lion "Her address is at…"

    dorothy "{i}writes it down{/i} Thanks for her address."

    lion "If you two were locals, you would have known this, everyone is at least aware of other people in this community. Addresses are common knowledge."

    dorothy "Wait, Scarecrow, shouldn’t you know this?"

    scarecrow "I live in a cave."

    dorothy "Thanks for all your help!"

    lion "My pleasure, I hope you two find out the truth."

    "You and Scarecrow walk out of the bar."

    scarecrow "Wait, we forgot to pay the bill."

    dorothy "Eh, if Lion really wants us to pay it, we’ll just pay it later. The more important thing is that we need to head to the Wicked Witch of the West’s house!"

    scarecrow "Alright, we got a lead. Let’s go!"

    jump chapter04 # go to chapter 4