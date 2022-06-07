# Purpose: This program takes the user's inputs and performs various calculations
# DSC 510
# Week 5
# Programming Assignment Week 5
# Author Darius Dinkins
# 4/12/2022

# This program should do the following:
# Perform addition, subtraction, division, and multiplication of two numbers provided by the user.
# Provide an average for the user based on their input.
# Provide a main method that calls the calculation functions based on the user's input
# Include appropriate comments throughout the program.
# Program should adhere to PEP8 guidelines especially as it pertains to variable names.

# PROGRAM START

# Function that takes the user's input to perform addition, subtraction, multiplication, and division
def performCalculation(operator):
    numberOne = int()
    numberTwo = int()
    calculationOne = float()
    operator = int(input("Please type the following operation for use \
    1 = Addition, 2 = Subtraction, 3 = Multiplication, and 4 = Division \n"))
    if operator == 1:
        print("Thanks, you chose addition")
        numberOne = input("Please type in the first number for calculation.\n")
        print("Thanks")
        numberTwo = input("Please type in the second number for calculation.\n")
        calculationOne = int(numberOne) + int(numberTwo)
    elif operator == 2:
        numberOne = input("Please type in the first number for calculation.\n")
        print("Thanks")
        numberTwo = input("Please type in the second number for calculation.\n")
        calculationOne = int(numberOne) - int(numberTwo)
    elif operator == 3:
        numberOne = input("Please type in the first number for calculation.\n")
        print("Thanks")
        numberTwo = input("Please type in the second number for calculation.\n")
        calculationOne = int(numberOne) * int(numberTwo)
    elif operator == 4:
        numberOne = input("Please type in the first number for calculation.\n")
        print("Thanks")
        numberTwo = input("Please type in the second number for calculation.\n")
        calculationOne = int(numberOne) / int(numberTwo)
    else:
        print("Please enter a number 1 through 4")
        performCalculation(-1)
    print("Thanks")
    print("Your calculation is ", calculationOne, "\nReturning you back to the main menu.")
    return calculationOne


# Function that calculates the average from the user's input.  Displays the running total and current average.
def calculateAverage():
    count = 0
    userNumber = 0
    count = int(input("Enter number of numbers you want to average. \n"))
    print("Thanks, you entered ", count, " numbers ready to be averaged!")
    for w in range(count):
        userNumber = userNumber + float(input("Enter your number \n"))
        print("The running total is ", userNumber)
        print("The current average is ", userNumber / (w + 1))
    else:
        print("Calculation complete, bringing you back to the main menu.")


# Main module function.  All calculation functions are called from main(). Also allows user to quit the program.
def main():
    calucationFunction = int()
    while calucationFunction == 0:
        calucationFunction = int(input("Please type in the calculation you would like to use. \n \
        1 = Addition, Subtraction, Multiplication, or Division. 2 = Average. 3 = Quit the Program \n"))
        if calucationFunction == int(1):
            performCalculation(-1)
        elif calucationFunction == int(2):
            calculateAverage()
        elif calucationFunction == int(3):
            print("Thanks for using the program.")
            break
    else:
        main()


if __name__ == "__main__":
    main()

# Change#:1
# Change(s) Made: Created calculator program that takes the input of user to perform various operations
# Date of Change: 4/12/2022
# Author: Darius Dinkins
# Change Approved by: Darius Dinkins
# Date Moved to Production: 4/12/2022
