# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   11.16 Lab: Loan Calculator
# Date:         18 Nov 2025

# Get user input
filename = input("Enter the output filename: ")
P = float(input("Enter the principal amount: "))
N = int(input("Enter the term length (months): "))
i = float(input("Enter the annual interest rate: "))

# Calculate monthly payment
M = (P * i / 12) / (1 - (1 / (1 + i / 12)) ** N)

# Initialize variables
balance = P
total_interest = 0.0
month = 0

# Open the file for writing
with open(filename, "w") as f:
    f.write("Month,Total Accrued Interest,Loan Balance\n")
    f.write(f"{month},${total_interest:.2f},${balance:.2f}\n")

    # Loop through each month
    while balance > 0.01:
        month += 1
        interest = balance * i / 12
        total_interest += interest
        balance = balance + interest - M

        if balance < 0:
            balance = 0.0

        f.write(f"{month},${total_interest:.2f},${balance:.2f}\n")
