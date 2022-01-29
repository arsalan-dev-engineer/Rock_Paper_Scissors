import random

# list with 3 items
game = ["rock", "paper", "scissors"]
# random used for computer to choose a random item from the list
computer = random.choice(game)

# score
player = 0
bot = 0

# 3 plays
plays = 3
# after each game, plays will decerement by 1
while plays > 0:
    user = input("Choose rock, paper, scissors: ")
    # type "rock", "paper" or "scissors" in this input

    if user == "rock" and computer == "scissors":
        print(f"{user} beats {computer}\nyou win")
        # if this condition is true, player score will increase by 1
        player += 1
        # this will allow the user to choose 3 times in 1 game
        plays -= 1

    elif user == "paper" and computer == "rock":
        print(f"{user} beats {computer}\nyou win")
        player += 1
        plays -= 1

    elif user == "scissors" and computer == "paper":
        print(f"{user} beats {computer}\nyou win")
        player += 1
        plays -= 1

    elif user == computer:
        print(f"draw")
        plays -= 1
        # this statement executes is user and computer draw

    else:
        print(f"{computer} beats {user}\nyou lose")
        bot += 1
        plays -= 1
        # if user loses, bot scores a point


print("\nGame over!")
# results
print(f"You scored {player}, computer scored {bot}")
