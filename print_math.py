# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Kingston Ronnie Alexander
# Section: 509
# Assignment: Lab 1.12 - Print Math
# Date: 26 August 2025

# Import the sin and pi functions from the math library
# Import the math library for math.log function
import math
from math import sin, pi

reynoldsNumber = (0.875*9)/(0.0015)
productionRate = (100)/(1 + 0.8*2*10)**(1/0.8)
# Convert the degrees to radians for sin or trig functions in general
wavelength = (2*0.029*sin(35*pi/180))/(1)
# Use math.log for natural logarithm
changeInVelocity = (2029)*math.log(11000/8300)

print(f"Reynolds number is {reynoldsNumber}")
print(f"Wavelength is {wavelength} nm")
print(f"Production rate is {productionRate} barrels/day")
print(f"Change in velocity is {changeInVelocity} m/s")
