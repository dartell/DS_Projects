# Your program must have a header.
# Your program must have a welcome message for the user.
# Your program must have one class called CashRegister.
# Your program will have an instance method called addItem which takes one parameter for price. The method should also keep track of the number of items in your cart.
# Your program should have two getter methods.
# getTotal – returns totalPrice
# getCount – returns the itemCount of the cart
# Your program must have a properly defined main function and a call to main.
# Your program must create an instance of the CashRegister class within your main function.
# Your program should have a loop in main which allows the user to continue to add items to the cart until they request to quit.
# Your program should print the total number of items in the cart.
# Your program should print the total $ amount of the cart.
# The output should be formatted as currency. Be sure to investigate the locale class. You will need to call locale.setlocale and locale.currency.
# Your program should adhere to PEP8 guidelines especially as it pertains to variable names.

import locale
locale.setlocale(locale.LC_ALL, '') 


class CashRegister:
    """ Initializes Class that adds items to carts.  Keeps tracks of items through the addItem method.  
    getTotal and getCount returns the total price and total items in the cart."""
    def __init__(self, initial_price = 0):
        self.price = initial_price
        self.items = int()
        # self.items = 0

    def addItem(self, amount):
        self.price = self.price + amount
        self.items = self.items + 1
        

    def getTotal(self):
        return self.price

    def getCount(self):
        return self.items


def main():
    """Calls the CashRegister class which allows the user to enter the price of items."""
    user_input = 'y'
    register = CashRegister()
    while user_input == 'y':
        print("Welcome to the class register program.  Please insert the price of item 1")
        try:
            register.addItem(float(input('Insert Price' '\n')))
        except ValueError: 
            print("Please enter a number")
            main()
        print('Total price of items in cart: ', locale.currency(register.getTotal(), grouping=True))
        print('Total amount of items in cart: ', register.getCount())
        user_input = input('Would you like to add another? Enter "y" to add another.  Enter "n" to close the program' '\n')
        if user_input == 'n':
            print('Total price of items in cart: ', locale.currency(register.getTotal(), grouping=True))
            print('Total amount of items in cart: ', register.getCount())
            print('Closing program')
            exit()


if __name__ == '__main__':
    main()

# Change#:1
# Change(s) Made: Created cash register program using classes.
# Date of Change: 5/29/2022
# Author: Darius Dinkins
# Change Approved by: Darius Dinkins
# Date Moved to Production: 5/29/2022
    

            

