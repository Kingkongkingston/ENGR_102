# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   11.15 Lab: Barcode Checker
# Date:         18 Nov 2025

def is_valid_barcode(code_str):

    if len(code_str) != 13:
        return False

    # Convert string to list of integers
    numbers = [int(ch) for ch in code_str]

    first_12 = numbers[:-1]
    evens = first_12[0::2]
    odds = first_12[1::2]

    sum_evens = sum(evens)
    sum_odds = sum(odds) * 3

    total_sum = sum_evens + sum_odds

    last_digit_calc = total_sum % 10
    check_digit = 10 - last_digit_calc

    return check_digit == numbers[-1]


def main():

    # Prompt user for input file
    file_input = input("Enter the name of the file: ").strip()

    try:
        with open(file_input, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return

    valid_list = [item for item in lines if is_valid_barcode(item)]

    with open("valid_barcodes.txt", "w") as f_out:
        for valid_code in valid_list:
            f_out.write(valid_code + "\n")

    print("There are", len(valid_list), "valid barcodes")


if __name__ == "__main__":
    main()
