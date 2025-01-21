# virtual dice game if you role six you win if not you lose a life

from random import randint

lives = 3
while lives > 0:
    dice_roll = randint(1, 6)
    if dice_roll == 6:

        print("Congrats! You rolled a 6 you win")
        break
    else:
        lives = lives - 1  # lose a life
        print(f"You rolled a {dice_roll} You lose a life, lives left {lives}")

else:
    print("You lose")

