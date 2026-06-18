print("Welcome to today's activity ")
name=input("Please enter your name: ")
print("Nice to meet you, " + name )
age=int(input("How old are you?"))
if age < 1:
    print("You are a baby")
elif age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
else:
    print("You are an adult")             