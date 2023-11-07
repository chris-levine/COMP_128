# calculator project

# setting inital variable to check status if calculator is still in use

status = "yes"

# displaying welcome message
print("""
---------------------------------------
      
    Hello, this is a calculator program!
    Instuctions:
        1. Enter the first number
        2. Enter the operation (+, -, *, /)
        3. Enter the second number
    Enjoy this program

---------------------------------------    
""")

# creating a while loop to show that we are still using the calculator 
while status == "yes":

    num1 = int(input("Enter the first number: "))
    print(" ")
    print("---------------------------------------")
    print(" ")
    operator = input("Enter the operation: ")
    print(" ")
    print("---------------------------------------")
    print(" ")
    num2 = int(input("Enter the second number: "))
    print(" ")
    print("---------------------------------------")

    # running conditionals
    if operator == "+":
        print(" ")
        print("You entered " + str(num1) + " + " + str(num2))
        print("The answer is: " + str((num1 + num2)))
        print(" ") 
    elif operator == "-":
        print(" ")
        print("You entered " + str(num1) + " - " + str(num2))
        print("The answer is: " + str((num1 - num2)))
        print(" ") 
    elif operator == "*":
        print(" ")
        print("You entered " + str(num1) + " * " + str(num2))
        print("The answer is: " + str((num1 * num2)))
        print(" ") 
    elif operator == "/" and num2 == 0:
        print(" ")
        print("You cannot divide by zero!")
        print(" ")
    elif operator == "/":
        print(" ")
        print("You entered " + str(num1) + " / " + str(num2))
        print("The answer is: " + str((num1 / num2)))
        print(" ") 
    else:
        break

    status = input("Would you like to make another calculation? (yes or no) ")
print("---------------------------------------")
print(" ")
print("Thank you for using my program!")
print(" ")
print("---------------------------------------")
        

    