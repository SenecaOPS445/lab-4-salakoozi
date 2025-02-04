#!/usr/bin/env python3
# Author ID: salakoozi
'''
Purpose: return True if all the characters in the string are all digits, 
i.e 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9; return False if any one of the characters 
is not a digit.
'''

def is_digits(sobj):
    for char in sobj: # Loop through each character in the string. 
        if char not in '0123456789': # If the character is not a digit
            return False
    return True # If the loop completes, and all characters are digits. 


if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')