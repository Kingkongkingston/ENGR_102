# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   2.8 Lab - Linear Interpolation
# Date:         30 August 2025

position_10 = 2029
position_55 = 23029

# 55 is 45 minutes after 10 minutes, and 10 minutes is the starting point. Use 55-10 for x values.
slope = (position_55 - position_10) / (55-10)

# 25 - 10 because 25 minutes is 15 minutes after 10 minutes, which is change in x.
position_25 = slope * (25-10) + position_10
position_300 = slope * (300-10) + position_10

print("Part 1:")
print("For t = 25 minutes, the position p =", position_25, "kilometers")
print("Part 2:")
print("For t = 300 minutes, the position p =", position_300, "kilometers")
