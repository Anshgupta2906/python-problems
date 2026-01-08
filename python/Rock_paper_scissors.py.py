import random

def get_choices():
    player_choices=input("Enter a choice (Rock, Paper, Scissors) :")
    options= ["Rock","Paper","Scissors"]
    computer_choices= random.choice(options)
    choices={"Player" : player_choices , "computer": computer_choices}
    return choices

def check_win(Player,computer):
    print(f"you chose {Player}, computer chose {computer}")
    if Player==computer:
        return "It's a tie!"
    elif Player=="Rock":
        if computer== "Scissors":
            return " Rock smashes Scissors!You win!"
        else:
            return "Paper covers Rock! you lose!"
        
    elif Player=="Paper":
        if computer== "Scissors":
            return "Scissors cut paper !You lose!"
        else:
            return "Paper covers Rock! you Win!"
        
    elif Player=="Scissors":
        if computer== "Rock":
            return " Rock smashes Scissors! You lose!"
        else:
            return "Scissors cut paper !You Win!"
        
choices=get_choices()
result=check_win(choices["Player"], choices["computer"] )
print (result)
