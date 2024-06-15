# Create rock, paper, or scissors game on console
import random

print("Welcome to Rock, Paper, Scissors Game!")
print("You will play against computer.")
print("Rock beats scissors. Scissors beats paper. Paper beats rock.")

# Initialize scores
user_score = 0
computer_score = 0

while True:
    # Get user's choice
    user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
    if user_choice == 'exit':
        break

    # Get computer's choice
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    # Print computer's choice
    print(f"Computer chose: {computer_choice}")

    # Determine the winner and update scores
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
    else:
        print("Invalid input! You have not entered rock, paper, or scissors, try again.")

# Print final scores
print(f"Final Scores:\nYou: {user_score}\nComputer: {computer_score}")
if user_score > computer_score:
    print("You are the overall winner!")
elif user_score < computer_score:
    print("Computer is the overall winner!")
else:
    print("It's a tie overall!")
