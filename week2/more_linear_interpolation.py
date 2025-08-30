# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   2.10 Lab - More Linear Interpolation
# Date:         30 August 2025

import sys

x_12 = 8
y_12 = 6
z_12 = 7

x_85 = -5
y_85 = 30
z_85 = 9

x_velocity = (x_85 - x_12) / (85 - 12)
y_velocity = (y_85 - y_12) / (85 - 12)
z_velocity = (z_85 - z_12) / (85 - 12)

times = [30.0, 37.5, 45.0, 52.5, 60.0]

# Use counter to number outputs (the numbers after x, y, and z)
# f strings for convenient concatenation
i = 1
for time in times:
    x_position = x_velocity * (time - 12) + x_12
    y_position = y_velocity * (time - 12) + y_12
    z_position = z_velocity * (time - 12) + z_12
    print(f"At time {time} seconds:")
    print(f"x{i} = {x_position} m")
    print(f"y{i} = {y_position} m")
    print(f"z{i} = {z_position} m")
    i += 1
    # Prevent printing separator after last output using sys.exit()
    if time != times[-1]:
        print("-----------------------")
