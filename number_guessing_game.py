import random

while True:

    difficulty_level = input("Choose difficulty level(Easy/Medium/Hard):").strip().title()

    if difficulty_level == "Easy":
        secret_number = random.randint(1, 50)
    elif difficulty_level == "Medium":
        secret_number = random.randint(1, 100)
    elif difficulty_level == "Hard":
        secret_number = random.randint(1, 500)
    else:
        print("Choose valid option!!!")
        continue

    won = False

    for i in range(1,11):   #Number of attempts is 10
        guess = int(input("Enter your guess: "))
        if guess > secret_number:
            print("Too High!")
        elif guess < secret_number:
            print("Too Low!")
        else:
            print("Congratulations! You guessed it.")
            print(f"You guessed it in {i} attempts!")
            won = True
            break

    if not won:
        print("Game Over!")
        print(f"The secret number was {secret_number}")

    replay = input("Do you want to play again(Yes/No): ").strip().title()
    if replay == "No":
        print("Thanks for playing!")
        break

    