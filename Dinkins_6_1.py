# Purpose: This program takes the user's inputs and records temperatures in a list
# DSC 510
# Week 6
# Programming Assignment Week 6
# Author Darius Dinkins
# 4/24/2022

# This program should do the following:
# Record temperatures from user input
# Put these temperatures within a list
# Provide a main method that calls the temperature recorder based on the user's input
# Include appropriate comments throughout the program.
# Program should adhere to PEP8 guidelines especially as it pertains to variable names.

# PROGRAM START

# Function that takes user inputs into a list called "temp"
def temperature_choice():
    a = 5
    b = int(-1)
    temp = []
    rerun = str()
    e = 'Invalid input detected, please enter valid temperature'
    if b == -1:
        try:
            while a == 5:
                temp.append(float(input(" Please enter temperature(s), enter any alphabet character to stop\n")))  # Let's the user add temperatures and displays user inputs
                print(temp)
                print("Temperature(s) entered: ", temp)
                print("Highest Temperature: ", max(temp))
                print("Lowest Temperature: ", min(temp))
                print("Total temperatures entered: ", len(temp))
        except ValueError as e: # Catches incorrect user inputs
                rerun = input("Inputs stopped, would you like to enter another set of temperatures?  If so enter 'y'.  If not, enter 'n'.  Press any other key to close the program. \n")
                if rerun == 'y':
                  temperature_choice()
                elif rerun == 'n':
                    print("Bringing you back to the main menu")
                    main()


# Main function that can call temperature choice function or quit the program.
def main():
    user_input = 0
    try:
        while user_input == 0:
            user_input = int(
                input("Welcome to the temperature recorder program. To start entering temperature(s), please enter '1'."
                      "To exit, enter '2'\n"))
            if user_input == 1:
                temperature_choice()
            elif user_input == 2:
                print("Closing the program")
                break
            else:
                print("Please enter '1' or '2'")
                main()
    except ValueError as e:
        print("Please enter '1' or '2'")
        main()


# Calls the main function
if __name__ == "__main__":
    main()


# Change#:1
# Change(s) Made: Created temperature recorder program that takes the input the user into a list
# Date of Change: 4/24/2022
# Author: Darius Dinkins
# Change Approved by: Darius Dinkins
# Date Moved to Production: 4/24/2022
