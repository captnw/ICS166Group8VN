# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define dorothy = Character("Dorothy", color="#ff3300")
define scarecrow = Character("Scarecrow", color="#9999ff")
define tinman = Character("Tin Man", color="#99cc00")
define lion = Character("Lion", color="#ffcc00")

# placeholder character portraits
image ScarecrowPlaceholder = Placeholder("boy")
image dorothyPlaceholder = Placeholder("girl")
image lionPlaceholder = Placeholder("boy")

# chapter 3
image bartenderPlaceholder = Placeholder("boy")

# placeholder bg

# chapter 3
image randomStreet = Placeholder("bg")
image outsideMunchkinBar = Placeholder("bg")
image insideMunchkinBar = Placeholder("bg")

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

    "narrator" "wow this is the prologue"

    # Go to chapter1
    jump chapter01