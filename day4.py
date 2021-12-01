import random
# import math
# Generating random numbers
# Generating random integers
# random_int = random.randint(0,10);
# print(random_int)

# Generating random floats:

# random_float = math.floor(random.random()*100);
# print(random_float)

# LISTS IN PYTHON
# list_of_friends = ["Raghav", "Rajit", "Ravi","Jyoti"]

# payee = random.randint(0,3)
# print("Today, the bill will be paid by " + list_of_friends[payee])

# Accessing list is as per usual in Python. Except, if you add negative numbers, you start accessing the list from the end. 
# LIST METHODS EXAMPLE
# list_of_friends.append("Rohit")
# list_of_friends.extend(["Ronit","Rasputin"])
# print(list_of_friends)

# BANKER ROULETTE
# names = input("Add a few names sista\n")
# names_list=names.split(", ")

# print(names_list[random.randint(0,len(names_list)-1)] + " will pay the bill today")

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[1][1])

moves = ["rock","paper","scissor"]
computer_move = moves[random.randint(0,2)]

your_move = input("Rock, Paper or Scissor?\n").lower()

if(your_move== "rock" and computer_move=="scissor"):
    print("You played " + your_move.capitalize() + " and the computer played " + computer_move.capitalize() + ". You win!")
elif(your_move== "rock" and computer_move=="paper"):
    print("You played " + your_move.capitalize() + " and the computer played " + computer_move.capitalize() + ". You lose!")
elif(your_move== "rock" and computer_move=="rock"):
    print("You played " + your_move.capitalize() + " and the computer played " + computer_move.capitalize() + ". Draw!")
elif(your_move== "paper" and computer_move=="scissor"):
    print("You played " + your_move.capitalize() + " and the computer played " + computer_move.capitalize() + ". You lose!")
elif(your_move== "paper" and computer_move=="paper"):
    print("You played " + your_move.capitalize() + " and the computer played " + computer_move.capitalize() + ". Draw!")
elif(your_move== "paper" and computer_move=="rock"):
    print("You played " + your_move.capitalize() + " and the computer played " + computer_move.capitalize() + ". You win!")
elif(your_move== "scissor" and computer_move=="scissor"):
    print("You played " + your_move.capitalize() + " and the computer played " + computer_move.capitalize() + ". Draw!")
elif(your_move== "scissor" and computer_move=="paper"):
    print("You played " + your_move.capitalize() + " and the computer played " + computer_move.capitalize() + ". You win!")
elif(your_move== "scissor" and computer_move=="rock"):
    print("You played " + your_move.capitalize() + " and the computer played " + computer_move.capitalize() + ". You lose!")

