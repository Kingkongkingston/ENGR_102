# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   6.16 LAB: Howdy Whoop
# Date:         3 October 2025

# Program prints numbers 1–100, replacing multiples with Howdy/Whoop.
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

for i in range(1, 101):
    if i % num1 == 0 and i % num2 == 0:
        print("Howdy Whoop")
    elif i % num1 == 0:
        print("Howdy")
    elif i % num2 == 0:
        print("Whoop")
    else:
        print(i)
