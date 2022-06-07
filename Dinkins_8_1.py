# Purpose: This program takes the user's inputs and records temperatures in a list
# DSC 510
# Week 8
# Programming Assignment Week 8
# Author Darius Dinkins
# 5/8/2022

# This program should do the following:
# Open up a .txt file
# Contain a main function that runs three additional functions
# Process each individual line to add into a dictionary
# Clean up the dictionary input with a function that prints the input neatly on screen
# Include appropriate comments throughout the program.
# Program should adhere to PEP8 guidelines especially as it pertains to variable names.

# PROGRAM START

# Imports string function
import string


# Process each line separately.  Each line is then lower cased and stripped of spaces and punctuation.
# Additionally, the end of the function provides two argurements for the add word function
def process_line(line, book):
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        if word != '--':
            word = word.lower()
            word = word.strip()
            word = word.strip(string.punctuation)
            add_word(word, book)


# Adds each word that was separated by the process line function into a dictionary.
def add_word(word, book):
    if word in book:
        book[word] += 1
    else:
        book[word] = 1


# Organizes the dictionary by providing a header.  The dictionary is turned into a list and neatly prints the data.
def pretty_print(book):
    value_key_list = []
    for key, val in book.items():
        value_key_list.append((val, key))
    value_key_list.sort(reverse=False)
    print('{:11s}{:11s}'.format("Word", "Count"))
    print(' ' * 24)
    for val, key in value_key_list:
        print('{:12s} {:<3d}'.format(key, val))


# The main function that begins the brings and calls the other three functions.
def main():
    book = {}
    try:
        gba_file = open('gettysburg.txt', 'r')
    except FileNotFoundError as e:
        print(e)
    for line in gba_file:
        process_line(line, book)
    print("Length of the dictionary", len(book))
    pretty_print(book)


if __name__ == "__main__":
    main()

# Change#:1
# Change(s) Made: Initial file that opens up a text file and counts each word in an organized list
# Date of Change: 5/8/2022
# Author: Darius Dinkins
# Change Approved by: Darius Dinkins
# Date Moved to Production: 5/8/2022
