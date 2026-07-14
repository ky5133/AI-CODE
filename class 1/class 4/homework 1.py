import random
from colorama import init, Fore, Style
init(autoreset=True)
print(Fore.CYAN + "Welcome to Rock, Paper, Scissors!" + Style.RESET_ALL)
print(Fore.BLUE + "Please enter your name: " + Style.RESET_ALL)
name = input("Please enter your name: ")
def user_choice():
    player_symbol = ''
    while player_symbol not in ['rock', 'paper', 'scissors']:
        player_symbol = input(Fore.GREEN + "Choose rock, paper, or scissors: " + Style.RESET_ALL).strip().lower()
    return player_symbol

def play():
    player_symbol = user_choice()
    options=["rock","paper","scissors"]
    ai_choice=random.choice(options)
    if player_symbol==ai_choice:
        print(Fore.YELLOW + f"AI chose {ai_choice}. It's a tie!" + Style.RESET_ALL)
    elif (player_symbol=="rock" and ai_choice=="scissors") :
        print(Fore.GREEN + f"AI chose {ai_choice}. {name} you win!" + Style.RESET_ALL) 
    elif (player_symbol=="paper" and ai_choice=="rock"):
         print(Fore.GREEN + f"AI chose {ai_choice}. {name} you win!" + Style.RESET_ALL)
    elif (player_symbol=="scissors" and ai_choice=="paper"):
        print(Fore.GREEN + f"AI chose {ai_choice}. {name} you win!" + Style.RESET_ALL)     
    else:
        print(Fore.RED + f"AI chose {ai_choice}. AI wins HAHAHA AI is anyways better!" + Style.RESET_ALL)
 
    play_again = input(Fore.GREEN + "Do you want to play again? (y/n): " + Style.RESET_ALL).strip().lower()
    while play_again == 'y':
      play()
      break                          

        

if __name__ == "__main__":
    play()
