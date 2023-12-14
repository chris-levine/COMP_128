# initial varible to set while loop
shopping = "yes"

# list to track pie purchases
pie_purchases = [0, 0, 0, 0, 0, 0, 0]

# list to track pie prices
pie_prices = [10.00, 12.00, 13.00, 9.00, 15.00, 11.00, 21.00]

# list to track if pies are taxable
pie_tax = [True, True, False, False, True, False, False]

# list of pies
pie_list = ["Pecan Pie", "Apple Pie", "Blueberry Pie", "Chocolate Pie", "Cherry Pie", "Rhubarb Pie", "American Pie"]

# amount purchased
total = 0

# welcome message
print(" ")
print("Welcome to the Old Pie Shop. Here is our selection of pies.")
print(" ")
print("----------------------")
print(""" Here are our seletion of pies:
      (1) Pecan Pie..$10.00, (2) Apple Pie..$12.00, (3) Blueberry Pie..$13.00, (4) Chocolate Pie..$9.00, 
      (5) Cherry Pie..15.00, (6) Rhubarb Pie..$15.00 (7) American Pie..$21.00
""")
print(" ")
print("The pies that are taxable are (1), (2), and (5) and they are taxable by 4%")
print("----------------------")

# creating a while loop to allow purchases
while shopping == "yes":
    
    # asking the user which pies they would like
    pie_choice = input("Which pie would you like? ")

    # getting the right index to keep track of choices 
    pie_choice_index = int(pie_choice) - 1

    # adding to the pie purchases
    pie_purchases[pie_choice_index] += 1

    # calculating the total price
    if pie_tax[pie_choice_index] == False:
        total = pie_prices[pie_choice_index] + total
    elif pie_tax[pie_choice_index] == True:
        total = (pie_prices[pie_choice_index] * 1.04) + (total)

    # adding a message to see what you have purchased
    print(" ")
    print(f"Great we will have {pie_list[pie_choice_index]} right out for you")
    print("----------------------")

    shopping = input("Would you like to continue shopping? (yes or no) ")


print("----------------------")
for pies in range(len(pie_list)):
    pie_count = str(pie_purchases[pies])
    pie_name = str(pie_list[pies])
    print(f"{pie_count} {pie_name}")

print(" ")
print(f"Your total is ${total}")

