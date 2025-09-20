# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kingston Alexander
#               Maya Ayoubi
#               Divyamaukthika Challa
#               Gia Huynh
# Section:      509
# Assignment:   4.18 Lab - Boolean Expressions
# Date:         19/09/2025

########## Part A ############
a_input = input("Enter True or False for a: ").upper()
b_input = input("Enter True or False for b: ").upper()
c_input = input("Enter True or False for c: ").upper()

a = a_input in ['T', 'TRUE']
b = b_input in ['T', 'TRUE']
c = c_input in ['T', 'TRUE']

########## Part B ############
print(f"a and b and c: {a and b and c}")
print(f"a or b or c: {a or b or c}")

########## Part C ############
xor = (a and not b) or (not a and b)
print(f"XOR: {xor}")

odd_count = (a and not b and not c) or (not a and b and not c) or (
    not a and not b and c) or (a and b and c)
print(f"Odd number: {odd_count}")

########## Part D ############
# Complex expression 1
complex1 = (not (a and not b) or (not c and b)) and (
    not b) or (not a and b and not c) or (a and not b)
# Simplified version 1
simple1 = not b

complex2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (
    a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))
simple2 = not c

print(f"Complex 1: {complex1}")
print(f"Complex 2: {complex2}")
print(f"Simple 1: {simple1}")
print(f"Simple 2: {simple2}")
