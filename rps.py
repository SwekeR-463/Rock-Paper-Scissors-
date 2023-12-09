import random

user_win = 0
computer_win = 0

choices = ["rock","paper","scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit\n").lower()
    if user_input == "q":
        break

    if user_input not in choices:
        continue

    random_number = random.randint(0,2)

    computer_pick = choices[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Win!")
        user_win = user_win + 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You Win!")
        user_win = user_win + 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Win!")
        user_win = user_win + 1

    elif user_input == computer_pick:
        print("No Result!")

    else :
        print("You Lose!")
        computer_win = computer_win + 1

print("You won", user_win, "times.")
print("The computer won", computer_win, "times.")
print("Goodbye!")