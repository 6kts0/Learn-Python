"""
Errors should never pass silently.
Faba Kouyate, Fall 2025
"""
import random
import numpy as np

def rock_paper_scissors():

    # Initialize list of choices
    elements = ['rock', 'paper', 'scissors']

    # Start loop
    while True:
        quitFunction = input("\nType quit to exit the game otherwise press enter: ") # Implemented from the average calculator
        if quitFunction.lower() == 'quit':
            print("Exiting program")
            break
        
        try:
            print("Good luck, this computer is pretty smart!")
            print("+-" * 25)

            player_choice = input(str("Enter your play: ")).lower()
            compute_choice = random.choice(elements) # Computers choice will be a random word within elements

            # Rejects any input that isnt within the list of choices 
            if player_choice not in elements:
                raise ValueError("Invalid entry")

            # If computer picks rock this code block runs
            if compute_choice == 'rock' and player_choice == 'rock':
                print("\nTie!")
            elif compute_choice == 'rock' and player_choice =='paper':
                print("\nYou beat the computer!")
            elif compute_choice == 'rock' and player_choice == 'scissors':
                print("\nMark Zuckerberg wins again... dont worry he's still listening!")
            
            # If computer picks paper this code block runs
            elif compute_choice == 'paper' and player_choice == 'rock':
                print("\nSam Altman has taken the W... and your data.")
            elif compute_choice == 'paper' and player_choice == 'paper':
                print("\nTie!")
            elif compute_choice == 'paper' and player_choice == 'Scissors':
                print("\nYou beat the computer!")
            
            # If computer picks scissors this code block runs
            elif compute_choice == 'scissors' and player_choice == 'rock':
                print("\nYou beat the computer!")
            elif compute_choice == 'scissors' and player_choice == 'paper':
                print("\nElon Musk has taken the victory... but he payed to win.")
            elif compute_choice == 'scissors' and player_choice == 'scissors':
                print("\nTie!")
        # When an input is anything other than a string this code executes
        except ValueError:
            print("\n*INVALID ENTRY* Please enter rock paper or scissors")

rock_paper_scissors()
