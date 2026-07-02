import re, random
from colorama import Fore, init
init(autoreset=True)
destinations={
    "beaches":["Maldives", "Bali", "Hawaii", "Phuket", "Bahamas"],
    "mountains":["Swiss Alps", "Rocky Mountains", "Himalayas", "Andes", "Mount Fuji"],
    "cities":["New York", "Paris", "Tokyo", "London", "Dubai"],
}

jokes = [
    "Why don't progarammers like nature ? It has too many bugs.",
    "why did the computer go to the doctor ? It caught a virus.",
    "Why did the programmer quit his job? He didn't get arrays."
]

def normalise_input(user_input):
    return re.sub(r'\s+', ' ', user_input.strip().lower())

def reccomend():
    print(Fore.BLUE+"Travelbot: Beaches, mountains, or cities? ")
    preference = input(Fore.GREEN+"You: ")
    preference = normalise_input(preference)
    if preference in destinations:
        suggestion=random.choice(destinations[preference])
        print(Fore.LIGHTBLUE_EX+f"Travelbot: How about {suggestion}!")
        print(Fore.CYAN+"Do you like it? (yes/no)")
        response = input(Fore.YELLOW+"You: ")
        response = normalise_input(response)
        if response == "yes":
            print(Fore.LIGHTMAGENTA_EX+"Travelbot: Great! Have a wonderful trip!")
        if response == "no":
            print(Fore.LIGHTRED_EX+"Travelbot: No worries! Let's try again.")
            reccomend()
        else:
            print(Fore.LIGHTRED_EX+"Travelbot: I will suggest you again.")
            reccomend()
    else:
        print(Fore.LIGHTRED_EX+"Travelbot: I don't have recommendations for that.")
        reccomend()
    show_help()


def packing_tips():
    print(Fore.BLUE+"Where to?:")
    location = input(Fore.GREEN+"You: ")
    location = normalise_input(location)
    print(Fore.LIGHTBLUE_EX+f"Travelbot: How many days")
    days = input(Fore.GREEN+"You: ")
    days = normalise_input(days)

    print(Fore.LIGHTBLUE_EX+f"Travelbot: Here are some packing tips for {location} for {days} days:")  
    print(Fore.LIGHTMAGENTA_EX+"1. Pack light and versatile clothing.")
    print(Fore.LIGHTMAGENTA_EX+"2. Don't forget your travel documents and ID.")
    print(Fore.LIGHTMAGENTA_EX+"3. Bring a first aid kit and any necessary medications.")
    print(Fore.LIGHTMAGENTA_EX+"4. Check the weather forecast and pack accordingly.")

def tell_joke():
    joke = random.choice(jokes)
    print(Fore.LIGHTBLUE_EX+f"Travelbot: Here's a joke for you: {joke}")


def show_help():
    print(Fore.BLUE+"Travelbot: Here are some things you can ask me:")
    print(Fore.YELLOW+"1. Recommend a travel destination")
    print(Fore.YELLOW+"2. Give packing tips")
    print(Fore.YELLOW+"3. Tell a joke")
    print(Fore.YELLOW+"4. Exit")

def main():
    print(Fore.BLUE+"Travelbot: Hello! I'm your travel assistant. How can I help you today?")
    while True:
        show_help()
        choice = input(Fore.GREEN+"You: ")
        choice = normalise_input(choice)
        if choice == "1.Recommend a travel destination" or choice == "1":
            reccomend()
        elif choice == "2. Give packing tips" or choice == "2":
            packing_tips()
            print(Fore.MAGENTA+"Have a safe trip")
            break
        elif choice == "3. Tell a joke" or choice == "3":
            tell_joke()
        elif choice == "4. Exit" or choice == "4":
            print(Fore.LIGHTMAGENTA_EX+"Travelbot: Goodbye! Safe travels!")
            break

        else:
            print(Fore.LIGHTRED_EX+"Travelbot: I didn't understand that. Please choose a valid option.")


if __name__ == "__main__":
    main()            
