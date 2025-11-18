# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   11.15 Lab: Barcode Checker
# Date:         18 Nov 2025

def is_valid(barcode):
    digits = [int(d) for d in barcode]

    first_group = digits[0:12:2]
    second_group = digits[1:12:2]

    s1 = sum(first_group)
    s2 = sum(second_group) * 3

    total = s1 + s2
    check_digit = (10 - (total % 10)) % 10

    return check_digit == digits[-1]


valid = []

with open("barcodes.txt", "r") as f:
    for line in f:
        code = line.strip()
        if len(code) == 13 and code.isdigit() and is_valid(code):
            valid.append(code)

with open("valid_barcodes.txt", "w") as out:
    for v in valid:
        out.write(v + "\n")

print(f"There are {len(valid)} valid barcodes")
