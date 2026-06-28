import colorama
from colorama import Fore, Style
from textblob import TextBlob
colorama.init()
print(f"{Fore.CYAN}??????????? Welcome to Sentiments Spy?{Style.RESET_ALL}")
user_name = input("Please enter your name: ")
if not user_name:
    print("Welcome Mystery User!")
conversation_history = []
print(f"{Fore.RED}Hello {user_name}!")
print("Type your sentensce and  I will analyse the sentiment of your text. Type 'exit' to quit the program.")
while True:
    user_input=input(f"{Fore.GREEN}>> {Style.RESET_ALL}")
    if not user_input:
        print("Enter some valid command")
        continue
    if user_input.lower() == "exit":
        print(f"{Fore.BLUE}Goodbye {user_name}!{Style.RESET_ALL}")
        break
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.MAGENTA}Conversation history cleared.{Style.RESET_ALL}")
        continue        
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history available.{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}Conversation History:{Style.RESET_ALL}") 

    elif user_input.lower() == "history":

        if not conversation_history:

            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")

        else:

            print(f"{Fore.CYAN}???? Conversation History:{Style.RESET_ALL}")

            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):

                if sentiment_type == "Positive":

                    color = Fore.GREEN

                    emoji = "????"

                elif sentiment_type == "Negative":

                    color = Fore.RED

                    emoji = "????"

                else:

                    color = Fore.YELLOW

                    emoji = "????"



                print(f"{idx}. {color}{emoji} {text} "

                    f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")

        continue
    polarity = TextBlob(user_input).sentiment.polarity 
    if polarity > 0.25:
        sentiment_type = "Positive"
        emoji = "😊"
        print(f"{Fore.GREEN}Your text is Positive! {emoji}{Style.RESET_ALL}")
    elif polarity < -0.25:
        sentiment_type = "Negative"
        emoji = "😢"
        print(f"{Fore.RED}Your text is Negative! {emoji}{Style.RESET_ALL}")
    else:
        sentiment_type= "Neutral"
        emoji = "😐"
        print(f"{Fore.YELLOW}Your text is Neutral! {emoji}{Style.RESET_ALL}")        
    conversation_history.append((user_input, polarity, sentiment_type))