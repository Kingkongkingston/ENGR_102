# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   4.20 Lab - How Many Gadgets
# Date:         22 September 2025

import sys

day = int(input("Please enter a positive value for day: "))
if day < 1:
    print("You entered an invalid number!")
    sys.exit()

if 1 <= day <= 10:
    gadgets = 10 * day
elif 11 <= day <= 50:
    # First 10 days: 10*10 = 100
    # Days 11 to 'day': sum of integers from 11 to 'day'
    gadgets = 100 + (day * (day + 1) // 2 - 10 * 11 // 2)
elif 51 <= day <= 100:
    # First 10 days: 100
    # Days 11-50: sum from 11 to 50 = (50*51//2 - 10*11//2) = 1220
    # Days 51 to 'day': each day adds 50 gadgets
    gadgets = 100 + 1220 + 50 * (day - 50)
elif day >= 101:
    # Factory stops producing after day 100
    gadgets = 3820

print(f"The sum total number of gadgets produced on day {day} is {gadgets}")
