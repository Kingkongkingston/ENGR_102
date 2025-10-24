# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   7.18 Lab: Name Game
# Date:         11 October 2025

# Get name from user
name = input("What is your name? ")
lower_name = name.lower()

# Treat vowels normally
vowels = "aeiou"

# if name starts with 'y', treat 'y' as a vowel
if lower_name[0] == 'y':
    vowels += 'y'

idx = 0
while idx < len(lower_name) and lower_name[idx] not in vowels:
    idx += 1

if idx > 0 and lower_name[idx] == 'y':
    short_name = lower_name[idx:]
else:
    short_name = lower_name[idx:] if idx < len(lower_name) else lower_name

print(f"{name}, {name}, Bo-B{short_name}")
print(f"Banana-Fana Fo-F{short_name}")
print(f"Me Mi Mo-M{short_name}")
print(f"{name}!")
