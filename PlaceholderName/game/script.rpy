# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define dorothy = Character("Dorothy")
define brainless = Character("Scarecrow")
define heartless = Character("Tin Man")
define coward = Character("Lion")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene big ben exterior

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show dorothy happy

    # These display lines of dialogue.

    dorothy "Oh, I just LOVE looking down on London from the top of Big Ben!"
    dorothy "All those lovely people don't even know that they are getting their photos taken!"

    hide dorothy happy

    "*Click!"

    scene london photo

    "You snap a picture.  Looks great!"

    heartless "Hey, you there!  Come away from the edge!"
    dorothy "Oh, bug off, mister!"
    "*So rude...*"

    scene big ben exterior
    show dorothy happy

    dorothy "This is the only way I can get the *best photos*, anyways!"
    dorothy "Now let's see... where's the button for..."
    dorothy "...?!"

    # This ends the game.

    return
