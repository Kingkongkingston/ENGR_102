# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   11.15 Lab: Barcode Checker
# Date:         18 Nov 2025

def valid_barcode(barcode):
    if len(barcode) != 13:
        return False

    digits = [int(d) for d in barcode]
    group1 = digits[0::2]  # Odd digits
    group2 = digits[1::2]  # Even digits

    total = sum(group1) + 3 * sum(group2)
    check_digit = (10 - (total % 10)) % 10

    return check_digit == digits[-1]


def main():
    filename = input("Enter the name of the file: ").strip()

    try:
        with open(filename, "r") as f:
            barcodes = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return

    valid_barcodes = [code for code in barcodes if valid_barcode(code)]

    with open("valid_barcodes.txt", "w") as f:
        for code in valid_barcodes:
            f.write(code + "\n")

    print("There are", len(valid_barcodes), "valid barcodes")


if __name__ == "__main__":
    main()
