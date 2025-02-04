#!/usr/bin/env python3

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(string):
    # Place code here - refer to function specifics in section below
    return (string[0:5])

def last_seven(string):
    # Place code here - refer to function specifics in section below
    return (string[-7:])

def middle_number(number :int) -> str:
    # Place code here - refer to function specifics in section below
    #Accepts a integer as a argument
    #Returns a string containing the second and third characters in the number
    number_str = str(number)
    return number_str[1] + number_str[2]

def first_three_last_three(arg1, arg2):
    # Place code here - refer to function specifics in section below
    first_three = arg1[:3]
    last_three = arg2[-3:]
    return first_three + last_three



if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))