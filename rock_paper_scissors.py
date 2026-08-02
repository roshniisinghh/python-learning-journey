from random import choice
import sys

options = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

while True:
    user_choice = input("Choose Rock, Paper, or Scissors: ").strip().title()

    if user_choice not in options:
        print("Invalid choice!")
        continue

    computer_choice = choice(options)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a Draw!")
    elif user_choice == "Rock" and computer_choice == "Paper":
        print("Computer Wins!")
        computer_score += 1
    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("You Win!")
        user_score += 1
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("You Win!")
        user_score += 1
    elif user_choice == "Paper" and computer_choice == "Scissors":
        print("Computer Wins!")
        computer_score += 1
    elif user_choice == "Scissors" and computer_choice == "Rock":
        print("Computer Wins!")
        computer_score += 1
    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("You Win!")
        user_score += 1

    print("------ SCORE ------")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

    while True:

        replay = input("Do you want to play again? (Yes/No): ").strip().title()

        if replay == "Yes":
            break          
        elif replay == "No":
            print("Thanks for playing!")
            sys.exit()        
        else:
            print("Choose a valid option (Yes/No)")