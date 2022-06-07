# Purpose: Gather's input from the user which includes company name, feet of fiber optic cable to be installed.
# Also calculates installation cost of fiber optic cable and prints a receipt of that information
# DSC 510
# Week 3
# 3.1 Programming Assignment
# Author Darius Dinkins
# 03/21/2022

# This program should do the following:
# Display a welcome message for your user.
# Retrieve the company name from the user.
# Retrieve the number of feet of fiber optic cable to be installed from the user.
# Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
# If the user purchases a certain number of feet, they get a discount.  100ft = $0.80, 250ft = $0.70, 500ft = $0.50
# Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost,
# and total cost in a legible format.
# Include appropriate comments throughout the program.
# Your program should adhere to PEP8 guidelines especially as it pertains to variable names.

# PROGRAM START
# Program welcomes user
print("Welcome to the fiber optic installation cost calculator program")

# Asks the user to input the company name
company = input("What is the name of your company?\n")
print("Thanks")

# Asks the user how long the cable is
feet_cable = input("How long is the fiber optic cable you are installing in feet?\n")
int(feet_cable)
print("Thanks")

# Installation cost calculation
installation_cost = int(feet_cable) \
                    * 0.87

# If statement that gives discount over 100, 250, 500 ft.
if int(feet_cable) <= 100:
    installation_cost = int(feet_cable) \
                        * 0.87
elif int(feet_cable) <= 250:
    installation_cost = int(feet_cable) \
                        * 0.80
elif int(feet_cable) <= 500:
    installation_cost = int(feet_cable) \
                        * 0.75
elif int(feet_cable) > 500:
    installation_cost = int(feet_cable) \
                        * 0.50

# Print receipt from user's input
print("Here is your receipt")
print(" Company: ", company,
      "\n", "Length of Cable: ", feet_cable,
      "\n", "Installation cost: $", float(installation_cost))

# Change#: 1
# Change(s) Made: Added ability to give discount based on number of feet purchased
# Date of Change: 03/29/2022
# Author: Darius Dinkins
# Change Approved by: Darius Dinkins
# Date Moved to Production: 03/29/2022
