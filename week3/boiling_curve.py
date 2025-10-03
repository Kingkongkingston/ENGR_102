# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Kingston Alexander
# Section: 509
# Assignment: 5.5 Lab - Boiling Curve
# Date: 26 September 2025
#
#
# YOUR CODE HERE

import math

# Function to calculate heat flux between two points (log-log interpolation)


def interpolate(x, x0, y0, x1, y1):
    m = math.log(y1 / y0) / math.log(x1 / x0)
    return y0 * ((x / x0) ** m)


# Boiling curve points (excess temperature [°C], heat flux [W/m^2])
A = (1.3, 1000)
B = (5, 7000)
C = (30, 1.5e6)
D = (120, 2.5e4)
E = (1200, 1.5e6)

# User input
excess_temp = float(input("Enter the excess temperature: "))

# Check if temperature is in range
if excess_temp < A[0] or excess_temp > E[0]:
    print("Surface heat flux is not available")
else:
    # Determine interval and calculate flux
    if A[0] <= excess_temp <= B[0]:
        q = interpolate(excess_temp, *A, *B)
    elif B[0] <= excess_temp <= C[0]:
        q = interpolate(excess_temp, *B, *C)
    elif C[0] <= excess_temp <= D[0]:
        q = interpolate(excess_temp, *C, *D)
    else:  # Between D and E
        q = interpolate(excess_temp, *D, *E)

    # Round and output
    q_rounded = round(q)
    print(f"The surface heat flux is approximately {q_rounded} W/m^2")
