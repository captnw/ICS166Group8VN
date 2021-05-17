# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define dorothy = Character("Dorothy", color="#ff3300")
define scarecrow = Character("Scarecrow", color="#9999ff")
define tinman = Character("Tin Man", color="#99cc00")
define lion = Character("Lion", color="#ffcc00")
define wwwest = Character("W. W. West", color="#ffcc00")
define wiz = Character("The Wiz", color="#ffcc00")

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
define janitor = Character("Janitor", color="#ffcc00")

image outsideBigBen = Placeholder("bg")

# chapter 1
image crimeScene = Placeholder("bg")

image wizBlurred = Placeholder("boy") # the wizard but just his shadow/outline

# chapter 3
image bartenderPlaceholder = Placeholder("boy")

image outsideMunchkinBar = Placeholder("bg")
image insideMunchkinBar = Placeholder("bg")

# chapter 4
image outsideMansion = Placeholder("bg")
image insideMansion = Placeholder("bg")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene big ben exterior

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show dorothy happy

    # These display lines of dialogue.

    #dorothy "Oh, I just LOVE looking down on London from the top of Big Ben!"
    #dorothy "All those lovely people don't even know that they are getting their photos taken!"

    #hide dorothy happy

    #"*Click!"

    #scene london photo

    #"You snap a picture.  Looks great!"

    #heartless "Hey, you there!  Come away from the edge!"
    #dorothy "Oh, bug off, mister!"
    #"*So rude...*"

    #scene big ben exterior
    #show dorothy happy

    #dorothy "This is the only way I can get the *best photos*, anyways!"
    #dorothy "Now let's see... where's the button for..."
    #dorothy "...?!"

    # outsideBigBen bg

    "Your name is Dorothy and you are simply ecstatic to go to Big Ben today to capture more of your favorite photos of London’s charming cityscape!"

    # dorothy portrait show

    dorothy "Oh, this is the perfect day for taking photos of London! We so rarely get sunny days like this."

    "You inhale a huge breath of fresh air and lift your arms all the way over your head so your skin can drink in the warm sun."

    "You decide to start waving at someone you have never seen before."

    dorothy "Hi there!"

    # lion portrait show

    janitor "{i}Unreasonably scared{/i} GAAAH! Uhm, hello...?!"

    dorothy "Beautiful day, isn’t it?!"

    "You can’t help but notice how lion-like the janitor looks with his scruffy, red-orange hair."

    dorothy "Good day, officers!"

    # tinman portrait show

    tinman "Good day."

    # wiz portrait show 

    wiz "Good day young lady! Where are you off to?"

    dorothy "I’m off to Big Ben, so I can see the whole sky!"

    "You notice that the man there next to the investigator looks rather grumpy. What will you do?"

menu chapter00Choice:
    
    "Stop to cheer him up.":
        jump chapter00A

    "Yell something encouraging as you skip away.":
        jump chapter00B
    
    "Move on, he’ll cheer up on his own":
        jump chapter00C

label chapter00A:
    
    "You turn around with a twinkle in your eye and start skipping and waving towards the grumpy man."

    dorothy "{i}Cheerfully{/i} Excuse me, sir?! It's such a beautiful day!  Why the long…"

    "You’re still a few feet away when suddenly your vision is crowded with the color green! A strange man in a green shirt has just cut in front of you!"

    jump chapter00D

label chapter00B:
    
    "You turn your head back to smile at the officers."

    dorothy "Hey! I’ll bet you’d look more handsome if you smiled!"

    "You have no time to imagine it though, because a strange-looking man in a green shirt has suddenly started addressing you!"

    jump chapter00D

label chapter00C:
    
    "You keep skipping on your merry way, trying to imagine what the grumpy man might look like if he was more cheerful."

    dorothy "{i}To self{/i} I’ll bet his smile looks rather handsome"

    "You have no time to imagine it though, because a strange-looking man in a green shirt has suddenly started addressing you!"

    jump chapter00D
    
label chapter00D:

    # scarecrow portrait show 

    scarecrow "Excuse me, miss, but may I ask you a question?"

    dorothy "{i}Dumbfounded{/i} Uhm... uh..."

    scarecrow "Those shoes of yours are really quite pathetic. Haven’t you ever thought of walking about in something more stylish?"

    dorothy "{i}offended{/i} Excuse me?! These shoes suit me just fine for long walks, thanks!" 

    scarecrow "Well, there are those who would kill for a pricey pair of stylish shoes. Hm… {i}thinks for a moment, then smiles{/i}"
    
    scarecrow "I guess that makes you one less person to worry about! Good day, miss!"

    "You shake your head in disbelief as the stranger turns to walk away."

    # Go to chapter1
    jump chapter01