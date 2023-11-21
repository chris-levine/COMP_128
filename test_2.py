# Q1: Create a game similar to magic 8-ball game. Ask user to enter a number. 
# If number entered is 1, display "You can count on it". If number entered is 2, display "My sources say no". 
# If number entered is 3, display "Concentrate and ask again". If number entered is 4, display "Very doubtful”. 
# For any other number, display “Incorrect entry!”

print(" ")
print("--------------------")
user_input = int(input("Please enter a number: (1 - 4)"))
print(" ")
print("--------------------")

if user_input == 1:
    print("You can count on it!")
elif user_input == 2:
    print("My sources say no.")
elif user_input == 3:
    print("Concentrate and ask again!")
elif user_input == 4:
    print("Very doubtful.")
else:
    print("Incorrect entry!")


# Write a program that determines the shipping cost for a purchase from an online company. Suppose that the shipping rates are the following, based on the total price of the purchase:
## For any total less than $20, it's $1.5.
## For any total between $21 and $50, it's $4.
## For any total between $51 and $100, it's $7.
## For any total larger than $100, it's $10.
# The program should start by asking the user for the total price of the purchase, then display the shipping cost to the user.

print(" ")
print("--------------------")
user_input2 = int(input("What is the total price of your purchase? $"))
print("--------------------")
print(" ")

if user_input2 < 20:
    print("Your shipping cost is $1.5 bringing your total to $" + str(user_input2 + 1.5))
elif user_input2 >= 20 and user_input2 < 50:
    print("Your shipping cost is $4 bringing your total to $" + str(user_input2 + 4))
elif user_input2 >= 50 and user_input2 < 100:
    print("Your shipping cost is $7 bringing your total to $" + str(user_input2 + 7))
elif user_input2 >= 100:
    print("Your shipping cost is $10 bringing your total to $" + str(user_input2 + 10))
else: 
    print("Error!")

# Q3: Meal Planner: Ask the user for their dietary preferences. 
# Based on their response, print specific lunch options: Grilled Seitan for Vegan, Seared Salmon for Pescatarian, 
# Caprese Salad for Vegetarian, and Club Sandwich for None.

print(" ")
print("--------------------")
user_input3 = input("What is your dietary preference? (vegan, vegetarian, pescatarian, none)")
print("--------------------")
print(" ")

user_input_lower = user_input3.lower()

if user_input_lower == "vegan":
    print("Your lunch option is Grilled Seitan")
elif user_input_lower == "vegetarian":
    print("Your lunch option is a Caprese Salad")
elif user_input_lower == "pescatarian":
    print("Your lunch option is a Seared Salmon")
elif user_input_lower == "none":
    print("Your lunch option is a Club Sandwich")
else:
    print("Please select a designated option")