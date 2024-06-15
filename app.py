# Create rock, paper, or scissors game on console
import random

print("Welcome to Rock, Paper, Scissors Game!")
print("You will play against computer.")
print("Rock beats scissors. Scissors beats paper. Paper beats rock.")

# Get user's choice
user_choice = input("Enter rock, paper, or scissors: ").lower()

# Get computer's choice
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

# Print computer's choice
print(f"Computer chose: {computer_choice}")

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win!")
    else:
        print("Computer wins!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    else:
        print("Computer wins!")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")
else:
    print("Invalid input! You have not entered rock, paper, or scissors, try again.")
    exit()

# Ask user to play again
play_again = input("Do you want to play again? (yes/no): ").lower()
if play_again != "yes":
    # End of the game
    print("Thanks for playing Rock, Paper, Scissors Game!")
    exit()
else:
    # Play again
    print("Let's play again!")
    print()
    # Run the game again
    exec(open("app.py").read())
