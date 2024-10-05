'''
1 for  rock
-1 for paper 
0 for scissor
'''
import random

# Computer randomly chooses rock, Paper, or Scissor
computer = random.choice([-1, 0, 1])

# User inputs choice, with 'r' for rock, 'p' for paper, and 's' for scissor
youstr = input("Enter your choice (r for rock , p for paper, s for scissor): ").lower()  # Lowercase to handle any capitalization

# Dictionary to map user input to corresponding values
youDict = {"r": 1, "p": -1, "s": 0}  

# Dictionary to reverse map values to strings
reverseDict = {1: "rock", -1: "paper", 0: "scissor"}  

# Error handling: Check if user input is valid
if youstr not in youDict:
    print("Invalid input! Please choose 'r' for rock, 'p' for paper, or 's' for scissor.")
else:
    # Convert user input to corresponding numeric value
    you = youDict[youstr]  

    # Print the choices of the user and computer
    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    # Check if it's a draw
    if computer == you:
        print("It's a Draw")
    else:
        # Check win/lose conditions based on traditional Rock-Paper-Scissors rules
        if (you == 1 and computer == 0):  # rock beats Scissors
            print("You win!")
        elif (you == 0 and computer == 1):  # Scissors lose to rock
            print("You lose!")
        elif (you == -1 and computer == 1):  # Paper beats rock
            print("You win!")
        elif (you == 1 and computer == -1):  # rock loses to Paper
            print("You lose!")
        elif (you == 0 and computer == -1):  # Scissors beat Paper
            print("You win!")
        elif (you == -1 and computer == 0):  # Paper loses to Scissors
            print("You lose!")
        else:
            print("Something went wrong")



