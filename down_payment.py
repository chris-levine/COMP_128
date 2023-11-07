# down payment calculator 

# initial variable to track if using
status = "yes"

# displaying welcome message
print(" ")
print("---------------------------------------")
print("Hello! I am here to help you with the purchase of your house.")
print("This program will help you calculate the down payment you must make based on the price of your house!")
print("---------------------------------------")

# creating a while loop to show we are still using this calculator 

while status == "yes":
    print(" ")
    house_price = int(input("What is the price of your house? (please enter an amount) $"))
    print(" ")
    down_payment = 0
    
    # writing condition statements 
    if house_price >= 0 and house_price < 200000:
        down_payment = down_payment + round(house_price * .20, 2)
        print("A house that is $" + str(house_price) + " requires a 20% down payment!")
        print("You will need to put $" + str(down_payment) + " down")
        print(" ")
        print("---------------------------------------")
        print(" ")
    
    elif house_price >= 200000 and house_price < 399999:
        down_payment = down_payment + round(house_price * .15, 2)
        print("A house that is $" + str(house_price) + " requires a 15% down payment!")
        print("You will need to put $" + str(down_payment) + " down")
        print(" ")
        print("---------------------------------------")
        print(" ")
    
    elif house_price >= 400000: 
        down_payment = down_payment + round(house_price * .1, 2)
        print("A house that is $" + str(house_price) + " requires a 10% down payment!")
        print("You will need to put $" + str(down_payment) + " down")
        print(" ")
        print("---------------------------------------")
        print(" ")

    else:
        print("Invalid response!")
        print(" ")
    status = input("Woud you like to enter another number? (yes or no) ")

print("Thank you for using this program!")