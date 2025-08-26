# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   1.13 Lab - Follow Directions
# Date:         26 August 2025

import math

print("This shows the evaluation of (1-cos(x))/x^2 evaluated close to x=0")
print("My guess is 0")
testNumbers = [1.0, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001]

for testNumber in testNumbers:
    print((1-math.cos(testNumber))/(testNumber**2))

# Used sep parameter to add line before my guess statement
print("", "My guess was a little off", sep="\n")