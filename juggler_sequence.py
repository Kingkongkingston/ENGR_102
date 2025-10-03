# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   6.19 LAB: Juggler sequence
# Date:         3 October 2025

# Program generates and prints the Juggler sequence.
import math

n = int(input("Enter a positive integer: "))

print(f"The Juggler sequence starting at {n} is:")

count = 0
sequence = str(n)

while n != 1:
    if n % 2 == 0:  # even
        n = math.floor(math.sqrt(n))
    else:  # odd
        n = math.floor(n ** 1.5)
    sequence += f", {n}"
    count += 1

print(sequence)
print(f"It took {count} iterations to reach 1")
