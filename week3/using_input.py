# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   3.21 Lab - Using Input
# Date:         15 September 2025

# Import the sin and pi functions from the math library
# Import the math library for math.log function

import math
from math import sin, pi

print("This program calculates the Reynolds number given velocity, length, and viscosity")
velocity = float(input("Please enter the velocity (m/s): "))
length = float(input("Please enter the length (m): "))
viscosity = float(input("Please enter the viscosity (m^2/s): "))
reynoldsNumber = (velocity * length) / viscosity
reynoldsNumber = round(reynoldsNumber)
print("Reynolds number is", reynoldsNumber)
print()

print("This program calculates the wavelength given distance and angle")
distance = float(input("Please enter the distance (nm): "))
angle = float(input("Please enter the angle (degrees): "))
wavelength = (distance * sin(angle * (pi / 180))) / 0.5
wavelength = round(wavelength, 4)
print(f"Wavelength is {wavelength:.4f} nm")
print()

print("This program calculates the production rate given time, initial rate, and decline rate")
time = float(input("Please enter the time (days): "))
initialRate = float(
    input("Please enter the initial rate (barrels/day): "))
declineRate = float(input("Please enter the decline rate (1/day): "))
productionRate = (initialRate) / (1 + 0.8 * declineRate * time) ** (1 / 0.8)
print(f"Production rate is {productionRate:.2f} barrels/day")
print()

print("This program calculates the change of velocity given initial mass, final mass, and exhaust velocity")
initialMass = float(input("Please enter the initial mass (kg): "))
finalMass = float(input("Please enter the final mass (kg): "))
exhaustVelocity = float(input("Please enter the exhaust velocity (m/s): "))
changeOfVelocity = exhaustVelocity * math.log(initialMass / finalMass)
changeOfVelocity = round(changeOfVelocity, 1)
print("Change of velocity is", changeOfVelocity, "m/s")
