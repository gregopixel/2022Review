choice = ["rock", "paper", "scissors"]
def ask():
    global choose
    choose = input(f"What do you choose? {choice}\n")
    while not choose.lower() in choice:
        choose = input(f"Unexpected input! What do you choose? {choice}\n")
    return choose.lower()
def lose(x):
    print(f"I chose {x}. You lose")
def again():
    again = input("Play again? (Y/N)")
    while not again.lower() in ['y', 'yes', 'n', 'no']:
        again = input("Unexpected input! Do you want to play again? (Y/N)")
    if again.lower() in ["y", "yes"]:
        game()
    return again
def game():
    ask()
    print(f"You chose {choose}.")
    if choose == choice[0]: # If player chose rock
        lose(choice[1])
    elif choose == choice[1]: # If player chose paper
        lose(choice[2])
    elif choose == choice[2]: # If player chose scissors
        lose(choice[0])
    again()
game()

