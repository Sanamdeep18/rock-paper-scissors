
# '''
# 1 for stone (rock)
# -1 for paper 
# 0 for scissor
# '''
# This is a comment block explaining the numeric representations of each choice:
# 1 is for stone (or rock),
# -1 is for paper,

# 0 is for scissors.
# import random
# This imports the random module, which allows us to use the random.choice() function to make the computer's choice random.

# # Computer randomly chooses Stone, Paper, or Scissor
# computer = random.choice([-1, 0, 1])
# random.choice([-1, 0, 1]) randomly selects one value from the list [-1, 0, 1], which corresponds to paper (-1), scissors (0), or stone (1). This is the computer's choice.

# # User inputs choice, with 'r' for stone, 'p' for paper, and 's' for scissor
# youstr = input("Enter your choice (r for stone, p for paper, s for scissor): ").lower()
# The user is asked to input their choice by typing 'r' (for rock/stone), 'p' (for paper), or 's' (for scissors).
# The .lower() method ensures that if the user enters uppercase letters (e.g., 'R', 'P', 'S'), it is converted to lowercase to avoid mismatches.

# # Dictionary to map user input to corresponding values
# youDict = {"r": 1, "p": -1, "s": 0}
# This dictionary maps the user’s input ('r', 'p', 's') to the corresponding numeric values:
# 'r' corresponds to 1 (stone),
# 'p' corresponds to -1 (paper),
# 's' corresponds to 0 (scissors).


# # Dictionary to reverse map values to strings
# reverseDict = {1: "stone", -1: "paper", 0: "scissor"}
# This dictionary maps the numeric values (1, -1, 0) back to their string representations for display purposes. It helps to print the corresponding names:
# 1 maps to "stone",
# -1 maps to "paper",
# 0 maps to "scissor".

# # Error handling: Check if user input is valid
# if youstr not in youDict:
#     print("Invalid input! Please choose 'r' for stone, 'p' for paper, or 's' for scissor.")
# This is an error-handling block to check whether the user's input (youstr) is valid. If the user enters anything other than 'r', 'p', or 's', it prints an error message and ends the process.

# else:
#     # Convert user input to corresponding numeric value
#     you = youDict[youstr]
# If the user's input is valid, the code converts the input ('r', 'p', 's') to the corresponding numeric value using the youDict dictionary and assigns it to the variable you.

# # Print the choices of the user and computer
# print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
# The program prints both the user's choice and the computer's choice. It uses reverseDict to convert the numeric values back to readable names (like "stone", "paper", or "scissors").

# # Check if it's a draw
# if computer == you:
#     print("It's a Draw")
# This checks whether the user and the computer made the same choice. If they did, the game is a draw, and the message "It's a Draw" is printed.

# else:
#     # Check win/lose conditions based on traditional Rock-Paper-Scissors rules
# If the game is not a draw, the program moves on to the next step: determining who wins based on the rules of Rock-Paper-Scissors.

# if (you == 1 and computer == 0):  # Stone beats Scissors
#     print("You win!")
# Stone beats scissors, so if the user chose stone (you == 1) and the computer chose scissors (computer == 0), the user wins.

# elif (you == 0 and computer == 1):  # Scissors lose to Stone
#     print("You lose!")
# Scissors lose to stone, so if the user chose scissors (you == 0) and the computer chose stone (computer == 1), the user loses.

# elif (you == -1 and computer == 1):  # Paper beats Stone
#     print("You win!")
# Paper beats stone, so if the user chose paper (you == -1) and the computer chose stone (computer == 1), the user wins.

# elif (you == 1 and computer == -1):  # Stone loses to Paper
#     print("You lose!")
# Stone loses to paper, so if the user chose stone (you == 1) and the computer chose paper (computer == -1), the user loses.

# elif (you == 0 and computer == -1):  # Scissors beat Paper
#     print("You win!")
# Scissors beat paper, so if the user chose scissors (you == 0) and the computer chose paper (computer == -1), the user wins.

# elif (you == -1 and computer == 0):  # Paper loses to Scissors
#     print("You lose!")
# Paper loses to scissors, so if the user chose paper (you == -1) and the computer chose scissors (computer == 0), the user loses.

# else:
#     print("Something went wrong")
# This is a catch-all statement in case something unexpected happens, though in this case, it’s not likely to run because all possible outcomes are already covered. It prints "Something went wrong" if there is an unexpected condition.

# Summary:
# The program lets the user play a game of Rock-Paper-Scissors against the computer.
# The computer makes a random choice, and the user inputs their choice.
# The program checks whether it's a draw or evaluates the game based on the rules of Rock-Paper-Scissors and prints the appropriate outcome (win, lose, or draw).
# If the user enters an invalid choice, it gives an error message.
