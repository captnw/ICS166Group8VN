# Chapter 4
# define a character here, once defined, these
# are shared with all .rpy scripts
define bartender = Character("Bartender", color="#bfbfbf") 

# placeholder character portraits
#image ScarecrowPlaceholder = Placeholder("boy")
#image dorothyPlaceholder = Placeholder("girl")
#image tinmanPlaceholder = Placeholder("boy")

label chapter04:
    
    "Chapter 4: W. W. WEST'S MANSION"
    $ hasCh4Happened = True

    # outsideMansion bg
    scene outsideMansion at truecenter :
        zoom 1.55
    with fade

    # scarecrow portrait show
    show ScarecrowPlaceholder at left
    with dissolve

    scarecrow "Wow, I had a feeling she'd be rich but not {b}THIS{/b} rich."

    # dorothy portrait show
    show dorothyPlaceholder at right
    with dissolve

    dorothy "Yea whatever, hopefully she doesn't have a security system."

    scarecrow "So hopefully she's rich AND stu-"

    "Dorothy pulls Scarecrow behind a bush"

    dorothy "Wait shut up, look. {i}points to Tin Man, who is kneeling outside a mansion window{/i} What the heck is that guy doing? Is, is that Tin Man?"

    scarecrow "Maybe he's the the security system"

    dorothy "{i}With a dumbfounded expression{/i} I don't think so. He's saying something."

menu chapter04Choice:

    "Let's try to get closer so we can hear him.":
        jump chapter04A

    "Let's tell him to get out of here, he's obviously just being a creep.":
        jump chapter04B

label chapter04A:
    
    "They sneak over to another bush that's closer to Tin Man"

    hide ScarecrowPlaceholder
    hide dorothyPlaceholder

    #tin man portrait show
    show tinmanPlaceholder at center
    with dissolve

    tinman "Oh W. W. West how I long for your love. Why is it that you ignore my letters, and that when you do read them you cry and throw them away?"

    scarecrow "Ah, it seems he is not the security system, but rather the INsecurity system"

    dorothy "Haha real funny, anyway he's literally like stalkinging her right now, this is defitely illegal."

    scarecrow "Yea, but aren't we kind of doing the same thing?"

    dorothy "Yeesss, but we aren't stalking her, we're just gonna snoop through her house and maybe steal some of her stuff for evidence."

    scarecrow "That kinda sounds worse than stalking."

menu chapter04AChoice:

    "Yea okay fine why don't we go make friends with our fellow criminal then?":
        jump chapter04AA

    "Whatever lets get him out of here.":
        jump chapter04B


label chapter04AA:

    scarecrow "Really? Okay."

    "Scarecrow gets up and walks over to the Tin Man"

    show ScarecrowPlaceholder at left

    scarecrow "Hey Tin Man, are you watching W. W. West too?"

    "Tin Man is taken aback and a bit spooked"

    tinman "Oh ah I uh um uh... {b}AHEM{/b} I was just watching her, for the investigation!"

    scarecrow "Ohh so you were talking to the Wiz about that stuff earlier. Man that's messed up, I'm sorry ge's not accepting your love letters."

    tinman "Wait, what? No, (he heard that?) okay fine, I have a perilous infatuation with the beautiful W. W. West."

    "Dorothy gets out from the bush and walks over to where Scarecrow and Tin Man are."

    show dorothyPlaceholder at right

    tinman "Wait you're here too? Hold on what are you guys doing here?"

    scarecrow "Oh, we're gonna break into-"

    dorothy "We saw you over here and heard your plight and want to help you!"

    tinman "Really?"

    scarecrow "Really?"

    dorothy "Uh yup! Why don't we, um, go on over to the front door and ask if we could get some tea?"

    tinman "Oh no, I could never."

    "A doorbell is heard, Scarecrow is already at the door, ringing the bell"

    scarecrow "Oh hi ma'am, would you like to talk to the guy standing outside your window talking to himself?"

    # W. W. West portrait show
    hide tinmanPlaceholder
    show wwWestPlaceholder at center 
    with dissolve 

    wwwest "The what? Who?"

    "Tin Man and Dorothy dash over to the front door."

    hide ScarecrowPlaceholder 
    show tinmanPlaceholder at left
    with dissolve 

    tinman "{i}Out of breath{/i} Hello madam! I was wondering if you uh, um, uhhhhhh..."

    dorothy "We were wondering if we could borrow some sugar?"

    wwwest "All three of you?"

    dorothy "Yup."

    wwwest "{i}sigh{/i} yeah okay let me go get some ready in a bag for you, you can come in if you want."

    hide tinmanPlaceholder 
    show ScarecrowPlaceholder at left
    with dissolve 

    scarecrow "Sweet! We don’t even have to sneak in now!"

    wwwest "What?"

    dorothy "Oh he uh, um, {b}SUGAR{/b}!"

    "Scarecrow and Dorothy dash into the house with Tin Man trailing behind, W.W. West walks in behind them shaking her head."

    # insideMansion bg
    scene insideMansion at truecenter :
        zoom 1.6
    with fade

    show wwWestPlaceholder at center 
    with dissolve

    wwwest "You can just have a seat over there while I go find the sugar."

    hide wwWestPlaceholder
    with dissolve

    "The three sit on the couch."

    show tinmanPlaceholder at right
    with dissolve

    tinman "{i}sigh{/i} now she’s probably going to hate me more than she already does."

    show dorothyPlaceholder at center
    with dissolve

    dorothy "What do you mean?"

    tinman "Ever since I saw her at the police station I’ve been madly in love, and I’ve sent her letters expressing these feelings, but she just throws them out with tears in her eyes. She doesn’t even open them!"

menu chapter04AAChoice:

    "Do you write your name on them?":
        jump chapter04AAA

    "Do you mail them to her from the police station?":
        jump chapter04AAA

label chapter04AAA:

    tinman "Yea, and I stamp them with the police station seal just to make sure she knows it’s coming from a safe source."

    dorothy "{i}dumfounded{/i} She probably thinks they’re letters from the police station about her sister’s murder."

    tinman "Oh, yeah huh. Wow I really didn’t think about that."

    dorothy "Obviously."

    show ScarecrowPlaceholder at left 
    with dissolve

    scarecrow "How many love letters have you even sent, it’s been like, a day."

    tinman "{i}glaring at Scarecrow{/i} Love cannot wait for the mourning of loss! She’s gotta move on somehow, I thought maybe I could help her, and that maybe she could help me."

    dorothy "Help you how?"

    tinman "I too have dealt with loss, I still do, and I’ve dealt with it for too long. I’m tired of feeling the way I do, I want to move past it, and I’m sure she does too. We need to go on living."

    dorothy "Yeah okay whatever but it’s literally only been like a day since her sister died you need to chill out."

    tinman "Perhaps you're right."

    scarecrow "Maybe you should go and apologize to her or explain the letters or something."

    tinman "You know what? I think I will. Thank you, you two, I knew my heart was right about you both."

    hide tinmanPlaceholder 
    with dissolve

    "Tin Man walks away into another room where the W.W. West is."

    hide dorothyPlaceholder
    show dorothyPlaceholder at right
    with dissolve

    dorothy "Scarecrow you’re a genius! Now we can look around while she’s distracted."

    scarecrow "Oh, uh yea that’s definitely why I told him to do that yup."

    dorothy "Okay, I’ll stay down here to keep an eye out for when they come back, you sneak upstairs and see if you can find anything of interest."

    scarecrow "Aye aye captain!"

    dorothy "What?"

    hide ScarecrowPlaceholder 
    with dissolve

    "Scarecrow darts upstairs."

menu chapter04AABChoice:

    "Go eavesdrop on Tin Man and W. W. West's conversation.":
        jump chapter04AAB

    "Stay where you are and play it safe.":
        jump chapter04AAC

label chapter04AAB:

    "Dorothy sneaks over to eavesdrop on Tin Man and W. W. West's conversation."

    hide dorothyPlaceholder
    show tinmanPlaceholder at center 
    show wwWestPlaceholder at right 
    with dissolve 

    $ hasListenedInOnWitchCh4 = True

    tinman "I'm also sorry about the love- uh I mean forensic letters, I suppose we sent those out a bit too early."

    wwwest "Yea, you think? Anyway, did you guys find her shoes yet? Those were a very important family heirloom."

    tinman "Shoes? Why was your sister wearing family heirloom shoes?"

    wwwest "To keep them safe and in sight, their just very important shoes okay? All the more reason you guys need to find them! As if it wasn’t enough for my sister to be killed, our family heirloom goes missing too! {i}begins crying{/i}"

    tinman "Don't worry mam, we'll find them, I promise you. Right now why don't we just get back to finding that sugar?"

    wwwest "{i}sniffles{/i} okay, yeah you're right."

    jump chapter04AAC 

label chapter04AAC:

    hide tinmanPlaceholder 
    show ScarecrowPlaceholder at center
    with dissolve

    scarecrow "{i}Heard from the second story{/i} {b}FOUND IT!{/b}"

    wwwest "{i}shocked{/i} What? Found what!?"
    
    "Scarecrow darts down the stairs."

    show dorothyPlaceholder at left

    dorothy "{i}Wide-eyed{/i} The uh, the sugar! We found it! Thank you!"

    wwwest "Wait what how? It should be right over here, did that voice come from upstairs, was that guy upstairs!?"

    dorothy "Ha ha what? Your sugar room isn’t upstairs? You must be lying because he found it upstairs!"

    wwwest "So he WAS upstairs!?"

    dorothy "{b}THANKS FOR THE SUGAR BYE!{/b}"

    "Dorothy and Scarecrow run out the front door and get away"

    # randomStreet bg
    scene randomStreet at truecenter :
        zoom 1.5
    with fade

    show dorothyPlaceholder at right
    with dissolve

    dorothy "{i}Out of breath{/i} Why the heck did you have to shout that you found it?"

    show ScarecrowPlaceholder at left
    with dissolve 

    scarecrow "Sorry, I was just really excited."

    dorothy "Wait, what is it anyway?"

    scarecrow "Oh, it’s sugar obviously, isn’t that what we were looking for?"

    dorothy "{b}WHAT?{/b}"

    hide ScarecrowPlaceholder
    show ScarecrowFunny at left

    scarecrow "{i}Chuckling{/i} I’m kidding, I’m kidding. I found this developed film, it has a picture of some really pretty red shoes on it. I think the film came from the same camera from the police station actually."
    $ hasCollectedRedShoesPhoto = True

    hide ScarecrowFunny
    show ScarecrowPlaceholder at left
    scarecrow "Seems to be from the scene of the crime, or something, and if you look closely at it seems there’s a secret compartment in the shoes, there’s something shiny peeking out."

    dorothy "{i}Shocked{/i} You notice all that? How?"

    scarecrow "Well, I'm not stupid."

    "Dorothy glares at scarecrow."

    scarecrow "Anyway you wanna head to the store? Since we didn’t get any sugar from the W.W. West?"

    dorothy "I have no words."

    hide ScarecrowPlaceholder
    show ScarecrowFunny

    scarecrow "What do you mean? Do we not need the sugar anymore?"

    "Dorothy grabs Scarecrow and they walk off"

    scene black
    with dissolve

    jump chapter05

label chapter04B:
    
    show tinmanPlaceholder at center
    with dissolve 

    "Dorothy steps out from behind the bush and goes and walks over to Tin Man."

    dorothy "Hey, what do you think you’re doing over here? You stalking W.W. West or something?"

    tinman "What, no I uh I..."

    dorothy "Yea uh huh okay bud, I’m sure the Wiz would like to hear about this."

    tinman "What no don’t I-"

    scarecrow "{i}Yelling from behinf the bush{/i} Yea dweeb!"

    "Scarecrow excitedly looks at Dorothy and gives a thumbs up. Dorothy looks at Scarecrow and puts her finger to her lips, shushing him."

    "Footsteps are heard from within the mansion, and then the door creaks open."

    hide ScarecrowPlaceholder
    hide dorothyPlaceholder
    show dorothyPlaceholder at left

    show wwWestAngry at right 
    with dissolve 

    wwwest "Hello!? What the hell are you people doing on my lawn!? What are you yelling about!? Get out of here before I call the cops!"

    hide tinmanPlaceholder 
    with dissolve 

    "Tin Man runs away immediately"

menu chapter04BChoice:

    "Oh we were just wondering if you had some sugar!":
        jump chapter04BB

    "We were just getting that creep off your lawn!":
        jump chapter04BB

    "We were just wondering if we could look through your house for evidence!":
        jump chapter04BB

label chapter04BB:
    
    wwwest "I don’t care what you’re doing or what you want, get off my lawn!"

    dorothy "Wait, but..."

    wwwest "Alright I’m getting my phone!"

    "Dorothy and Scarecrow run away from the mansion"

    scene black
    with dissolve

    jump chapter05