# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   11.15 Lab: Barcode Checker
# Date:         18 Nov 2025

filename = input("Enter the name of the file: ")


def is_valid(code):
    digits = [int(d) for d in code]

    first_group = digits[0:12:2]
    second_group = digits[1:12:2]

    total = sum(first_group) + 3 * sum(second_group)
    check_digit = (10 - (total % 10)) % 10

    return check_digit == digits[-1]


valid_count = 0

with open(filename, "r") as f:
    for line in f:
        code = line.strip()
        if len(code) == 13 and code.isdigit() and is_valid(code):
            with open("valid_barcodes.txt", "a") as out:
                out.write(code + "\n")
            valid_count += 1

print(f"There are {valid_count} valid barcodes")
