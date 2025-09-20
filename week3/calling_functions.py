# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   3.22 Lab - Calling Functions
# Date:         15 September 2025

import math


# Function to report the results of the area based on shape and side length
def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')


side = float(input("Please enter the side length: "))

triangle_area = (math.sqrt(3) / 4) * side * side
square_area = side * side
pentagon_area = 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side * side
hexagon_area = (3 * math.sqrt(3) / 2) * side * side
dodecagon_area = 3 * (2 + math.sqrt(3)) * (side) ** 2

printresult("triangle", side, triangle_area)
printresult("square", side, square_area)
printresult("pentagon", side, pentagon_area)
printresult("hexagon", side, hexagon_area)
printresult("dodecagon", side, dodecagon_area)
