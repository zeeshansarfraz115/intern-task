import random

choices = ["Rock", "Paper", "Scissors"]

while True:
    user_choice = input(
        "Enter your move (Rock, Paper, Scissors) or type 'end' to stop: "
    )

    # Exit the game
    if user_choice.lower() == "end":
        print("Game over. Thanks for playing!")
        break

    # to solve upper and lower case problem
    user_choice = user_choice.capitalize()

    # Validate input
    if user_choice not in choices:
        print("Invalid choice! Please enter Rock, Paper, or Scissors.\n")
        continue

    # Computer's choice
    computer_choice = random.choice(choices)

    print(f"Computer chose: {computer_choice}")

    # finding winner
    if user_choice == computer_choice:
        print("It's a tie!")

    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("You win! Rock smashes Scissors.")

    elif user_choice == "Paper" and computer_choice == "Rock":
        print("You win! Paper covers Rock.")

    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("You win! Scissors cut Paper.")

    elif computer_choice == "Rock" and user_choice == "Scissors":
        print("Computer wins! Rock smashes Scissors.")

    elif computer_choice == "Paper" and user_choice == "Rock":
        print("Computer wins! Paper covers Rock.")

    else:
        print("Computer wins! Scissors cut Paper.")

    