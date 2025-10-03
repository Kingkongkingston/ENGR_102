# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   6.20 LAB: Co-balancing numbers
# Date:         3 October 2025

# Program checks if a number is a co-balancing number.
n = int(input("Enter a value for n: "))

left_sum = 0
for i in range(1, n + 1):
    left_sum += i

right_sum = 0
r = 0
found = False

while right_sum < left_sum:
    r += 1
    right_sum += (n + r)
    if right_sum == left_sum:
        found = True
        break

if found:
    print(f"{n} is a co-balancing number with r={r}")
else:
    print(f"{n} is not a co-balancing number")
