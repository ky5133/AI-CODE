import re, random
from colorama import Fore, init
init(autoreset=True)
fast_food ={
       "KFC":["Fried Chicken", " Chicken Burgers", "Fries"],
       "McDonald's":[" veg Burgers", " chessy Fries", "Chicken Nuggets"],
       "Burger King":["Whopper", "Paneer King Burger", "Onion Rings","superMax fries"]
}

jokes= [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call a fake noodle? An impasta!"
    "Why did the scarecrow win an award? Because he was outstanding in his field!"
]

def normalise_input(user_input):
    return re.sub(r'\s+', ' ', user_input.strip().lower())

def reccomend():
    print(Fore.BLUE+"Which fast food restaurant would you like a recommendation from? (KFC, McDonald's, Burger King)")
    preference = input(Fore.GREEN+"You: ")
    preference = normalise_input(preference)
    if preference in fast_food:
     while True:

      suggestion = random.choice(fast_food[preference])

      print(Fore.LIGHTBLUE_EX + f"Chatbot : How about {suggestion}?")

      response = normalise_input(input(Fore.YELLOW + "You (yes/no): "))

      if response == "yes":

       print(Fore.LIGHTMAGENTA_EX + "Chatbot: Great! Enjoy your food!")

       break

      elif response == "no":

       print(Fore.LIGHTRED_EX + "Chatbot: Let me suggest another dish.")

      else:

       print(Fore.LIGHTRED_EX + "Please answer with yes or no.")
           
    
    
    show_help()


def packing_tips():
    print(Fore.BLUE+"Where to?:")
    location = input(Fore.GREEN+"You: ")
    location = normalise_input(location)
    print(Fore.LIGHTBLUE_EX+f"Chatbot: How many days")
    days = input(Fore.GREEN+"You: ")
    days = normalise_input(days)

    print(Fore.LIGHTBLUE_EX+f"Chatbot: Here are some packing tips for {location} for {days} days:")  
    print(Fore.LIGHTMAGENTA_EX+"1. Pack light and versatile clothing.")
    print(Fore.LIGHTMAGENTA_EX+"2. Don't forget your travel documents and ID.")
    print(Fore.LIGHTMAGENTA_EX+"3. Bring a first aid kit and any necessary medications.")
    print(Fore.LIGHTMAGENTA_EX+"4. Check the weather forecast and pack accordingly.")


def show_help():
    print(Fore.BLUE+"Chatbot: Here are some things you can ask me:")
    print(Fore.YELLOW+"1. Recommend a Fast food ")
    print(Fore.YELLOW+"2. Give packing tips")
    print(Fore.YELLOW+"3. tell a joke")
    print(Fore.YELLOW+"4. Exit")

def main():
    print(Fore.BLUE+"Chatbot: Hello! I'm your chat assistant. How can I help you today?")
    while True:
        show_help()
        choice = input(Fore.GREEN+"You: ")
        choice = normalise_input(choice)
        if choice == "1.Recommend a Fast food" or choice == "1":
            reccomend()
            
        elif choice == "2. Give packing tips" or choice == "2":
           packing_tips()
        elif choice == "3. tell a joke" or choice == "3":
            print(Fore.LIGHTBLUE_EX+f"Chatbot: Here's a joke for you: {random.choice(jokes)}")
        elif choice == "4. Exit" or choice == "4":
            print(Fore.LIGHTMAGENTA_EX+"Chatbot: Goodbye! Safe travels and have a great meal!")
            break

        else:
            print(Fore.LIGHTRED_EX+"Chatbot: I didn't understand that. Please choose a valid option.")


if __name__ == "__main__":
    main()            
