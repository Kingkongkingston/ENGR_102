# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   6.17 LAB: Computing sums
# Date:         3 October 2025

# Program computes the sum of all integers between two values.
a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))

start = min(a, b)
end = max(a, b)

total = 0
for i in range(start, end + 1):
    total += i

print(f"The sum of all integers from {start} to {end} is {total}")
