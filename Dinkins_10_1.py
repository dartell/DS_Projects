# We’ve already looked at several examples of API integration from a Python perspective and this week we’re going to write a program that uses an open API to obtain data for the end user.
# Create a program which uses the Request library to make a GET request of the following API: Chuck Norris Jokes.
# The program will receive a JSON response which includes various pieces of data.
# You should parse the JSON data to obtain the “value” key. The data associated with the value key should be displayed for the user (i.e., the joke).
# Your program should allow the user to request a Chuck Norris joke as many times as they would like.
# You should make sure that your program does error checking at this point.
# If you ask the user to enter “Y” and they enter y, is that ok? Does it fail? If it fails, display a message for the user.
# There are other ways to handle this. Think about included string functions you might be able to call.
# Your program must include a header as in previous weeks.
# Your program must have a properly defined main method and a properly defined call to main.
# Your program should adhere to PEP8 guidelines especially as it pertains to variable names.
# Your program must include a welcome message for the user.
# Your program must generate “pretty” output. Simply dumping a bunch of data to the screen with no context doesn’t represent “pretty.”


import requests


def main():
    """ Requests json data from Chuck Norris joke generator API.  Includes a try block that catches user inputs that are not integers"""
    user_input = 0
    error_print = 'Please enter a number "1" or "2"'
    while user_input == 0:
            try:
                print('Welcome to the Chuck Norris joke generator, Ranger!')
                user_input = int(input('1.) Enter "1" to produce a Chuck Norris Joke' '\n'
                                       '2.) Enter "2" to close the program' '\n'))
            except ValueError:
                print(error_print)
                user_input == 0
                main()
            while user_input == 1:
                if user_input == 1:
                    r = requests.get('https://api.chucknorris.io/jokes/random')
                    r = r.json()
                    print('Joke:', r.get('value'))
                    try:
                        user_input= int(input('Type "1" to hear another Chuck Norris joke.  Type "2" to close the program' '\n'))
                    except ValueError:
                        print(error_print)
                        main()
                    # if user_input != 1 or user_input != 2:
                    #     print(error_print)
    if user_input == 2:
        print('Closing the Chuck Norris program, Ranger.')
        exit()
    else:
        error_print
        main()



main()

if __name__ == "__main__":
    main()


# Change#:1
# Change(s) Made: Initial file that requests a chuck norris joke from an API.
# Date of Change: 5/22/2022
# Author: Darius Dinkins
# Change Approved by: Darius Dinkins
# Date Moved to Production: 5/22/2022
