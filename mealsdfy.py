from cookbook import (get_breakfasts, get_lunches, get_dinners, get_snacks, get_desserts)
import random

# receive a mood, receive a number of meals in that mood,
# print: names of x amount of meals
# create a list of all the ingredients I will need for the meals I want

# Asks the user for a number 0-3 until it receives that
while True:
    mood_choice = int(input("Select the meal's mood:\n0) Breakfasts, 1) Dinners, 2) Lunches, 3) Snacks, 4) Desserts\n"))
    if 0 <= mood_choice <= 4:
        break

# Asks the user for a number 1-32 until it receives that
while True:
    amount = int(input("(31 maximum) How many meals do you need? "))
    if 1 <= amount <= 31:
        break

# Would love to turn these into random messages, maybe even include the user's name?
match mood_choice:
    case 0:
        print("Breakfasts! Excellent Choice!") 
        get_breakfasts(amount)
    case 1:
        print("Dinners, great for evenening cravings!")
        get_dinners(amount)
    case 2:
        print("Lunches are convenient and simple!")
        get_lunches(amount)
    case 3:
        print("Snacks are a great in-between meals option!")
        get_snacks(amount)
    case 4:
        print("Time for dessert!")
        get_desserts(amount)