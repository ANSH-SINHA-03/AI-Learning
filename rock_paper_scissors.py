import random

def get_choices():
    player_choice = input("Enter a choice(rock, paper, scissors): ")
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)

    choices = {"player":player_choice, "computer":computer_choice}
    return choices

def check_win(player, computer):
    print(f"You Chose {player}, Computer Chose {computer}.")
    
    if player == computer:
        return "Its a tie!"
    
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes Scissors, you win :)"
        else: 
            return "Paper covers Rock, you loose :("
        
    elif player == "paper":
        if computer == "rock":
            return "Paper covers Rock, you win :)"
        else: 
            return "Scissors cuts Paper, you loose :("
        
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts Paper, you win :)"
        else: 
            return "Rock smashes Scissors, you loose :("
        
while True:

    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    print(result)

    play_again = input("Play again? (y/n): ").lower()

    if play_again != "y":
        print("Thanks for playing!")
        break


