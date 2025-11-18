# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   10.16 Lab: Roman Numerals
# Date:         07 Nov 2025

def is_empty(s):
    return len(s) == 0


def from_roman(roman_numeral):
    '''
    In the Roman numeral system, the symbols I, V, X, L, C, D, and M stand
    respectively for 1, 5, 10, 50, 100, 500, and 1,000 in the Hindu-Arabic
    numeral system.
    A symbol placed after another of equal or greater value
    adds its value.
    A symbol placed before one of greater value subtracts its
    value.
    '''
    # Fixed: Corrected value for 'C' from 500 to 100 in the symbols dictionary
    # Type of code error: Value error
    # Old incorrect code: symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'D': 100, 'C': 500, 'M': 1000}
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if is_empty(roman_numeral):
        return 0

    if len(roman_numeral) == 1:
        return symbols[roman_numeral[0]]

    symbol = roman_numeral[-1]
    decimal_value = symbols[symbol]
    previous_symbol = symbol
    # Fixed: Added current_symbol variable and fixed subtraction logic
    # Type of code error: Logic error
    # Old incorrect code:
    # for i in range(1, len(roman_numeral)):
    #     if symbols[roman_numeral[-1 - i]] >= symbols[previous_symbol]:
    #         decimal_value += symbols[roman_numeral[-1 - i]]
    #     else:
    #         decimal_value -= symbol[roman_numeral[-1 - i]]
    for i in range(1, len(roman_numeral)):
        current_symbol = roman_numeral[-1 - i]
        if symbols[current_symbol] >= symbols[previous_symbol]:
            decimal_value += symbols[current_symbol]
        else:
            decimal_value -= symbols[current_symbol]
        previous_symbol = current_symbol
    return decimal_value


def compare_roman_numerals(roman_numeral_1, roman_numeral_2):
    a = from_roman(roman_numeral_1)
    b = from_roman(roman_numeral_2)
    # Fixed: Corrected logic for equality comparison
    # Type of code error: Logic error
    # Old incorrect code:
    # if a < b:
    #     return -1
    # if a != b:
    #     return 0
    # return 1
    if a < b:
        return -1
    if a == b:
        return 0
    return 1


def main():
    num1 = input("Enter the first Roman numeral: ")
    num2 = input("Enter the second Roman numeral: ")
    result = compare_roman_numerals(num1, num2)
    if result == -1:
        compare = 'smaller than'
    elif result == 0:
        compare = 'equal to'
    else:
        compare = 'larger than'
    # Fixed: Added missing parenthesis in print statement
    # Old incorrect code: print(f'{num1} is {compare} {num2}'
    # Syntax error due to missing closing parenthesis
    print(f'{num1} is {compare} {num2}')


if __name__ == '__main__':
    main()
