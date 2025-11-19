# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Divyamaukthika Challa
#       Maya Ayoubi
#       Gia Huynh
#       Kingston Alexander
# Section: 509
# Assignment: Lab: Topic 11.9 (passport checker A)
# Date: 14 November 2025
#
#

# Ask the user for the file name
filename = input("Enter the name of the file: ")

# Open the file and read all the text
with open(filename, "r") as file:
    data = file.read()

# Split passports by blank line
passports = data.strip().split("\n\n")

valid_passports = []
valid_count = 0

# Loop through each passport
for passport in passports:

    # Replace newlines with spaces to make splitting easier
    cleaned = passport.replace("\n", " ")

    # Split into individual key:value pairs
    pieces = cleaned.split()

    # Make a list of just the keys
    keys = []
    for item in pieces:
        key, value = item.split(":")
        keys.append(key)

    required_fields = ["iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

    valid = True       # We assume it's valid first

    for field in required_fields:
        if field not in keys:
            valid = False       # Missing field → invalid

    if valid:
        valid_passports.append(passport)
        valid_count += 1


# Print how many are valid
print("There are", valid_count, "valid passports")

# Write valid passports to a new file
with open("valid_passports.txt", "w") as outfile:
    for i in range(len(valid_passports)):
        outfile.write(valid_passports[i])

        # Write a blank line between passports (but not after last one)
        if i != len(valid_passports) - 1:
            outfile.write("\n\n")
