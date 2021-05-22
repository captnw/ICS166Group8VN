# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define dorothy = Character("Dorothy", color="#ff3300")
define scarecrow = Character("Scarecrow", color="#9999ff")
define tinman = Character("Tin Man", color="#99cc00")
define lion = Character("Lion", color="#ffcc00")
define wwwest = Character("W. W. West", color="#ffcc00")
define wiz = Character("The Wiz", color="#ffcc00")
define stranger = Character("Stranger", color="#888888")

# placeholder character portraits
image ScarecrowPlaceholder = Placeholder("boy")
image dorothyPlaceholder = Placeholder("girl")
image lionPlaceholder = Placeholder("boy")
image tinmanPlaceholder = Placeholder("boy")

image wizPlaceholder = Placeholder("boy")
image wwWestPlaceholder = Placeholder("girl")

image MaleStranger = Placeholder("boy")
image FemaleStranger = Placeholder("girl")

image randomStreet = Placeholder("bg")
image policeQuestioningRoom = Placeholder("bg")

# prologue 
image outsideBigBen = "london street.jpg"
image insideBigBen = Placeholder("bg")

image londonPhoto1 = "london photo bridge.jpg"
image londonPhoto2 = "london photo bridge.jpg"
image londonPhoto3 = "london photo bridge.jpg"

# chapter 1
image crimeScene = Placeholder("bg")

image wizBlurred = Placeholder("boy") # the wizard but just his shadow/outline

# chapter2
image outsidePoliceStation = Placeholder("bg")

image RandomPoliceOfficer = Placeholder("girl")

# chapter 3
image bartenderPlaceholder = Placeholder("boy")

image outsideMunchkinBar = Placeholder("bg")
image insideMunchkinBar = Placeholder("bg")

# chapter 4
image outsideMansion = Placeholder("bg")
image insideMansion = Placeholder("bg")

# chapter 5
image scarecrowApartment = Placeholder("bg")
image londonBridge = Placeholder("bg")

# Runs python at initilization time, before the Game loads
init python:
    
    # Evidence variables (what have you collected)
    # AKA you and Scarecrow will discuss this
    hasCollectedRedShoesPhoto = False
    hasListenedToLionsTestimony = False
    hasCollectedCamera = False
    didYouGiveScarecrowTape = False # undeveloped tape in evidence room, ch.2
    hasCollectedTinManNote = False

    # Misc variables (mainly used for dialogue in chapter 5)
    hasListenedInOnWitchCh4 = False # eavesdropped on Witch's and Tinman's conversation
    hasCh4Happened = False # did you go to ch4
    doYouSuspectYourself = True # true until you've listened to the lion's testimony

# The game starts here.
label start:

    # outsideBigBen bg
    scene outsideBigBen :
        zoom 1.5

    show dorothyPlaceholder at center
    "Your name is Dorothy and you are simply ecstatic 
    to go to Big Ben today to capture more of your favorite photos 
    of London’s charming cityscape!"
    
    dorothy "Oh, this is the perfect day for taking photos of London! We so rarely get sunny days like this."

    "You inhale a huge breath of fresh air and lift your arms all the way over your head so your skin can drink in the warm sun."

    "You decide to start waving at someone you have never seen before."
    show dorothyPlaceholder at right

    dorothy "Hi there!"
    hide dorothyPlaceholder

    # lion portrait show
    show lionPlaceholder at left

    lion "GAAAH! Oh... ah, hello!"

    hide lionPlaceholder

    show dorothyPlaceholder at right

    dorothy "Beautiful day, isn’t it?!"

    "You can’t help but notice how lion-like the janitor looks with his scruffy, red-orange hair."

    dorothy "Good day, officers!"

    hide dorothyPlaceholder

    # tinman portrait show
    show tinmanPlaceholder at left

    tinman "Good day."

    hide tinmanPlaceholder
    # wiz portrait show 
    show wizPlaceholder at center

    wiz "Good day young lady! Where are you off to?"

    hide wizPlaceholder

    show dorothyPlaceholder at right

    dorothy "I’m off to Big Ben, so I can see the whole sky!"

    "You notice that the man there next to the investigator looks rather grumpy. What will you do?"
    show dorothyPlaceholder at center

menu chapter00Choice:
    
    "Stop to cheer him up.":
        jump chapter00A

    "Yell something encouraging as you skip away.":
        jump chapter00B
    
    "Move on, he’ll cheer up on his own":
        jump chapter00C

label chapter00A:

    show dorothyPlaceholder at right
    
    "You turn around with a twinkle in your eye and start skipping and waving towards the grumpy man."

    dorothy "Excuse me, sir?! It's such a beautiful day!  Why the long…"

    "You’re still a few feet away when suddenly your vision is crowded with the color green! 
    A strange man in a green shirt has just cut in front of you!"

    jump chapter00D

label chapter00B:
    show dorothyPlaceholder at right
    
    "You turn your head back to smile at the officers."

    dorothy "Hey! I’ll bet you’d look more handsome if you smiled!"

    "You have no time to imagine it though, because a strange-looking man in a green shirt has suddenly started addressing you!"

    jump chapter00D

label chapter00C:
    show dorothyPlaceholder at right
    
    "You keep skipping on your merry way, trying to imagine what the grumpy man might look like if he was more cheerful."

    dorothy "{i}I’ll bet his smile looks rather handsome{/i}"

    "You have no time to imagine it though, because a strange-looking man in a green shirt has suddenly started addressing you!"

    jump chapter00D
    
label chapter00D:

    hide dorothyPlaceholder
    # scarecrow portrait show 

    show ScarecrowPlaceholder at left
    scarecrow "Excuse me, miss, but may I ask you a question?"

    show dorothyPlaceholder at right
    dorothy "Uhm... uh..."

    scarecrow "Those shoes of yours are really quite plain. Haven’t you ever thought of walking about in something more stylish?"

    dorothy "{i}Excuse me?!{/i} These shoes suit me just fine for long walks, thanks!" 

    scarecrow "Well, you know there are those who would {i}kill{/i} for a pricey pair of stylish shoes. Hm…"
    
    "The strange man seems to think deeply about something before smiling"

    scarecrow "I guess that makes you one less person to worry about! Good day, miss!"

    hide ScarecrowPlaceholder
    "You stand for a moment, dumbfounded.  
    After a moment’s thought, you walk on towards Big Ben with a confident stride.
    You are quite proud of the shoes you are wearing and you don’t care who knows it!"
    hide dorothyPlaceholder

    scene insideBigBen
    with fade

    show dorothyPlaceholder

    dorothy "Hmmm... Let's see here..."

    "Your eyes are scanning the cityscape below you.  You're thinking very hard about which part would make the best photo"

    "There's a fountain in the city square that looks lovely in the sunlight!"

    "But then, the buildings on the East Side there are casting long dramatic shadows..."

    "And then there's the river reflecting the sunlight just under that beautiful bridge!"

    dorothy "What to do... what to do..."

    hide dorothyPlaceholder

menu chapter00Choice2:
    
    "Take a picture of the city square with the fountain":
        scene londonPhoto1 at truecenter with fade :
            zoom 1.5

        "You look out on the city square with the shimmering fountain."

        jump chapter00Result2

    "Take a picture of the shadowy buildings on the East Side":
        scene londonPhoto2 at truecenter with fade :
            zoom 1.5

        "You look out on the shadowy buildings on the East Side."
        
        jump chapter00Result2
    
    "Take a picture of the bridge suspended over the river":
        scene londonPhoto3 at truecenter with fade :
            zoom 1.5

        "You look out on the bridge suspended over the river."

        jump chapter00Result2

label chapter00Result2:

    "*Click!" 

    dorothy "Hmm..."

    "You can't be sure how the photo turned out until you spend time to develop them.
    Just by observing the cityscape, you notice one potential problem..."

    dorothy "Aw... it's overcast again..."

    "You can't be sure if the photo you got was sunny or not.  
    The sun might have ducked back behind the clouds right as you took the photo."

    dorothy "Maybe if I wait a moment, the sun will come back out!"

    scene insideBigBen with fade
    show dorothyPlaceholder

    "You're staring intently at the place in the sky where the sun is still hidden..."

    dorothy "Any second now..."

    "You notice a patch of empty sky moving closer and closer to the sun"

    dorothy "This is it!"

    "You point your camera back at your target and get ready to snap the photo"

    dorothy "Almost..."

    dorothy "GAH! Too bright!"

    dorothy "..."

    dorothy "...!"

    dorothy "SHIT!"

    "You watch in disbelief as your camera shrinks into a tiny black speck down below you.
    You just dropped it off the side of Big Ben!"

    dorothy "Oooooooh! That was my {i}best{/i} camera..."

    "You stand for a moment in disbelief, just staring out at the cityscape."

    "That was your best camera, and now you've just thrown it off the side of the tallest building in London!
    How on earth do you plan on {i}paying{/i}..."

    stranger "EEEEEEEK!"

    stranger "AAAARGH!"

    "Your blood runs cold as hideous shrieks start rising up from the street right where your camera fell"

    dorothy "What the hell?!"

    "You look down at the street.  There's quite a commotion building at the base of Big Ben"

    "A horrifying thought occurs to you"

    dorothy "Did my camera... {i}hit someone?{/i}"

    "You feel like you're gonna be sick"

    dorothy "Oh God..."

    "Almost as soon as the words are out of your mouth, 
    you turn around and start flying down the stairs as fast as your running shoes can carry you"

    dorothy "Damn it... DAMN IT!"

    "The dull sounds of sirens echo through the halls of Big Ben.  The trip down the tower seems to take eons"

    dorothy "Please don't be true... please don't be true..."

    "Hyperventilating and trembling all over, you finally reach the city street at the foot of Big Ben..."

    hide dorothyPlaceholder
    scene black with fade

    # Go to chapter1
    jump chapter01