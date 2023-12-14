import sys

# welcome message 
print("""

      Hello! Here is how the game works: 

        1. The user will enter a six letter word into the program
        2. The guesser will then have 10 tries to guess the word the user input
        3. You have 10 tries to guess the word or you fail
      
      Enjoy!

      """)

# user section
# initial variable
playing = "yes"

# creating while loop to stay in game for user
while playing == "yes":

    # user input word
    word = input("Please enter a six letter word: ").lower()

    # condition to make sure length of word is six
    if len(word) == 6:
        print(" ")
        print("Excellent! Pass the device to the guesser")
        print(" ")
        break
    else: 
        print(" ")
        print("Error! Not a six letter word!")
        print(" ")
        playing = input("Would you like to keep playing? (yes or no) ").lower()

if playing == "no":
    sys.exit()

# guesser section
# initial variables
turns = 10
blanks = ["_", "_", "_", "_", "_", "_"]

# making an empty list to store used letters
used_letters = []

# creaing for loop
# checkpoint
for turn in range(turns):
    print("-------------------------")
    print(blanks)
    print(" ")
    print(f"Used Letters: {used_letters}")
    print("-------------------------")
    print(" ")

    # letter input
    letter = input("Enter a letter: ").lower()

    # conditional if the letter has already been used
    if letter in used_letters:
        print(" ")
        print("You already guessed that letter")
        continue


    # conditional to see if letter is in the word
    if letter in word:
        print("Excellent")
        print(" ")
        # creaing for loop cycle through blanks
        for i in range(len(word)):

            # updating blanks with the correct letter
            if word[i] == letter:
                blanks[i] = letter
   
    # appending used letters to list 
    else:
        print("Incorrect!")
        print(" ")
        used_letters.append(letter)

    # conditional to see if word is complete
    if "_" not in blanks:
        print("You guessed the word!")
        break

# outgoing message
print(f"Congrats! The word was {word}.")