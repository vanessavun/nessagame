define v = Character("Nessa", color="#ffafcc")
define m = Character("Me", color="#a2d2ff")
image room = "sitting room.png"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show nessa

    # These display lines of dialogue.

    v "Welcome to the Nessa Game."

    m "Thanks, I think."

    v "Let's play Rock Paper Scissors!"

menu:

    "Rock!":
        jump rock

    "Paper!":
        jump paper
    
    "Scissors!":
        jump scissors

label rock:

    v "I play rock too. It's a tie!"

    jump end

label paper:

    v "I play rock. I lose!"

    jump end

label scissors:

    v "I play rock. I win!"

    jump end

label end:

    v "Thanks for playing!"

    return
