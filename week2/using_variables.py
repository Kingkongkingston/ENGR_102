# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   2.9 Lab - Using Variables
# Date:         30 August 2025

# Import the sin and pi functions from the math library
# Import the math library for math.log function
import math
from math import sin, pi

reynolds_number = (0.875*9)/(0.0015)
wavelength = (2*0.029*sin(35*pi/180))/(1)
production_rate = (100)/(1 + 0.8*2*10)**(1/0.8)
change_of_velocity = (2029)*math.log(11000/8300)

print("Reynolds number is", reynolds_number)
print("Wavelength is", wavelength, "nm")
print("Production rate is", production_rate, "barrels/day")
print("Change of velocity is", change_of_velocity, "m/s")
