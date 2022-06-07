# Purpose: This program takes the user's inputs and records temperatures in a list
# DSC 510
# Week 9
# Programming Assignment Week 8
# Author Darius Dinkins
# 5/10/2022

# This program should do the following:
# Open up a .txt file
# Contain a main function that runs three additional functions
# Process each individual line to add into a dictionary
# Clean up the dictionary input with a function that prints the input neatly on screen
# Include appropriate comments throughout the program.
# Program should adhere to PEP8 guidelines especially as it pertains to variable names.

# PROGRAM START

# Imports string function
import os
import string


def process_line(line, book):
    """ Processes each line separately.  Each line is then lower cased and stripped of spaces and punctuation.
        Additionally, the end of the function provides two argurements for the add word function"""
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        if word != '--':
            word = word.lower()
            word = word.strip()
            word = word.strip(string.punctuation)
            add_word(word, book)


def add_word(word, book):
    """Adds each word that was separated by the process line function into a dictionary."""
    if word in book:
        book[word] += 1
    else:
        book[word] = 1


# def pretty_print(book):
#     """Organizes the dictionary by providing a header.  The dictionary is turned into a list and neatly prints the data."""
#     value_key_list = []
#     for key, val in book.items():
#         value_key_list.append((val, key))
#     value_key_list.sort(reverse=False)
#     print('{:11s}{:11s}'.format("Word", "Count"))  # Header
#     print(' ' * 24)  # Spacing
#     for val, key in value_key_list:
#         print('{:12s} {:<3d}'.format(key, val))


def process_file(book):
    """Prints the file to a text document.  The dictionary is turned into a list and neatly prints the data."""
    value_key_list = []
    for key, val in book.items():
        value_key_list.append((val, key))
    value_key_list.sort(reverse=True)
    print('Thanks. You chose option one.  What would you like to name your new file?')
    with open(input(), 'w') as wf:
        file_name = wf
        dictionary_title = 'Dictionary Length : {:12s}'.format(str(len(book)))
        header = '{:11s}{:11s}'.format("Word ", "Count", '\n')
        wf.seek(0)
        wf.write(dictionary_title)
        wf.write('\n')
        wf.write('______________')
        wf.write('\n')
        wf.write(header)
        wf.write('\n')
        for val, key in value_key_list:
            wf.writelines('{:12s} {:<3d}'.format(key, val))
            wf.write('\n')
    print('File created as ', '"', file_name.name, '"',
          'Please open the file in your immediate directory.  Bringing you back to the main menu')
    main()


def main():
    """The main function that starts the program.  Calls the other three functions"""
    book = {}
    user_input = int(0)
    while user_input == 0:
        try:
            user_input = int(
                input(
                    'Welcome to the Word Counter program.' '\n'
                    '1.) Type 1 to begin the program and enter the file name. ' '\n'
                    '2.) Type 2 to view a list of files in your immediate directory' '\n'
                    '3.) Type 3 to exit the program' '\n'
                    'Remember to have the file in the same directory as the program.' '\n'))
        except ValueError as ve:
            print('Error! Please select an option between 1-3')
        if user_input == 1:
            print('Please enter the file name.  Example: gettysburg.txt')
            try:
                gba_file = open(input(), 'r')
            except FileNotFoundError as e:
                print("File not found, try again")
                user_input = 1
                main()
            for line in gba_file:
                process_line(line, book)
            process_file(book)
        elif user_input == 2:
            print('Here is a list of files in your immediate directory')
            directory_list = (os.listdir())
            for directory_loop_list in directory_list:
                print(directory_loop_list, '\n')
            print('Bringing you back to the main menu')
            user_input = 0
        elif user_input == 3:
            print('Roger that, exiting program')
            break
        else:
            print('Error! Please select an option between 1-3')
            main()


if __name__ == "__main__":
    main()

# Change#:1
# Change(s) Made: Initial file that opens up a text file and counts each word in an organized list
# Date of Change: 5/8/2022
# Author: Darius Dinkins
# Change Approved by: Darius Dinkins
# Date Moved to Production: 5/15/2022
