# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   4.19 Lab - Largest Number
# Date:         22 September 2025

# Get number inputs
number1 = float(input("Enter number 1: "))
number2 = float(input("Enter number 2: "))
number3 = float(input("Enter number 3: "))

# Determine and print the largest number
if (number1 >= number2) and (number1 >= number3):
    print(f"The largest number is {number1:.1f}")
elif (number2 >= number1) and (number2 >= number3):
    print(f"The largest number is {number2:.1f}")
else:
    print(f"The largest number is {number3:.1f}")
