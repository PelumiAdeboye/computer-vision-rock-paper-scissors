import random


def get_computer_choice():
    options = ["Rock", "Paper", "Scissors"]
    return random.choice(options)


def get_user_choice():
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").capitalize()
        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")


def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("It is a tie!")
    elif (
        (computer_choice == "Rock" and user_choice == "Scissors") or
        (computer_choice == "Paper" and user_choice == "Rock") or
        (computer_choice == "Scissors" and user_choice == "Paper")
    ):
        print("You lost!")
    else:
        print("You won!")


def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)


# Call the play function to start the game
play()

