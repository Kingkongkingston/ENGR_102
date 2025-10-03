# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   4.21 Lab - Calculate Roots
# Date:         22 September 2025

coefficientA = float(input("Please enter the coefficient A: "))
coefficientB = float(input("Please enter the coefficient B: "))
coefficientC = float(input("Please enter the coefficient C: "))

# Check for invalid case: A and B both zero
if coefficientA == 0 and coefficientB == 0:
    print("You entered an invalid combination of coefficients!")
# A is zero, B is not zero
elif coefficientA == 0:
    if coefficientB == 0:
        print("You entered an invalid combination of coefficients!")
    else:
        root = -coefficientC / coefficientB
        print(f"The root is x = {root:.1f}")
else:
    discriminant = coefficientB**2 - 4 * coefficientA * coefficientC
    # Real roots
    if discriminant > 0:
        root1 = (-coefficientB + discriminant**0.5) / (2 * coefficientA)
        root2 = (-coefficientB - discriminant**0.5) / (2 * coefficientA)
        print(f"The roots are x = {root1:.1f} and x = {root2:.1f}")
    elif discriminant == 0:
        root = -coefficientB / (2 * coefficientA)
        print(f"The root is x = {root:.1f}")
    else:
        realPart = -coefficientB / (2 * coefficientA)
        imaginaryPart = (-discriminant)**0.5 / (2 * coefficientA)
        print(
            f"The roots are x = {realPart:.1f} + {imaginaryPart:.1f}i and x = {realPart:.1f} - {imaginaryPart:.1f}i")
