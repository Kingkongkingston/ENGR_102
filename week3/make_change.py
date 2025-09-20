# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kingston Alexander
#               Maya Ayoubi
#               Divyamaukthika Challa
#               Gia Huynh
# Section:      509
# Assignment:   4.16 Lab - Make Change
# Date:         19/09/2025

paid = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))

change = paid - cost
print(f"You received ${change:.2f} in change. That is...")

# Convert to cents to avoid floating point issues
cents = round(change * 100)

# Calculate coins
quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents

# Print results
if quarters > 0:
    print(f"{quarters} quarter{'s' if quarters != 1 else ''}")
if dimes > 0:
    print(f"{dimes} dime{'s' if dimes != 1 else ''}")
if nickels > 0:
    print(f"{nickels} nickel{'s' if nickels != 1 else ''}")
if pennies > 0:
    print(f"{pennies} penn{'ies' if pennies != 1 else 'y'}")
