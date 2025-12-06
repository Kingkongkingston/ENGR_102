# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Divyamaukthika Challa
#       Maya Ayoubi
#       Gia Huynh
#       Kingston Alexander
# Section: 509
# Assignment: Lab: Topic 12 (numpy – team)
# Date: 17 November 2025
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

import numpy as np

# create 3 matrix of A,B and C  for each matrix the first element should be zero
A = np.arange(12).reshape(3, 4)
B = np.arange(8).reshape(4, 2)
C = np.arange(6).reshape(2, 3)

# each matrix with single blank line in between
print("A =", A, "\n")
print("B =", B, "\n")
print("C =", C, "\n")


# matrix multiplcation the @ symbol
D = A @ B @ C
print("D =", D, "\n")

# print d - transpose
print("D^T =", D.T, "\n")


# e is the square root of (D/2)
E = np.sqrt(D)/2
print("E =", E)
