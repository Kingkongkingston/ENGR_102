# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Divyamaukthika Challa
#       Maya Ayoubi
#       Gia Huynh
#       Kingston Alexander
# Section: 509
# Assignment: Lab: Topic 11.10 (passport checker B)
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

    # Split into key:value pieces
    pieces = cleaned.split()

    # Store key:value in a dictionary for easy lookup
    p = {}
    for item in pieces:
        key, value = item.split(":")
        p[key] = value

    # Required fields (same as Part A)
    required_fields = ["iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

    # First: check all required fields exist
    valid = True
    for field in required_fields:
        if field not in p:
            valid = False

    # If missing field, skip further checks
    if not valid:
        continue

    # Validate iyr (2015–2025)
    if not p["iyr"].isdigit() or not (2015 <= int(p["iyr"]) <= 2025):
        continue

    # Validate eyr (2025–2035)
    if not p["eyr"].isdigit() or not (2025 <= int(p["eyr"]) <= 2035):
        continue

    # Validate hgt
    hgt = p["hgt"]
    if hgt.endswith("cm"):
        num = hgt[:-2]
        if not num.isdigit() or not (150 <= int(num) <= 193):
            continue
    elif hgt.endswith("in"):
        num = hgt[:-2]
        if not num.isdigit() or not (59 <= int(num) <= 76):
            continue
    else:
        continue  # invalid units

    # Validate hcl (# + 6 hex digits)
    hcl = p["hcl"]
    if len(hcl) != 7 or hcl[0] != "#":
        continue
    valid_hcl = True
    for ch in hcl[1:]:
        if ch not in "0123456789abcdef":
            valid_hcl = False
    if not valid_hcl:
        continue

    # Validate ecl
    if p["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        continue

    # Validate pid (exactly 9 digits)
    pid = p["pid"]
    if not pid.isdigit() or len(pid) != 9:
        continue

    # Validate cid (3 digits, no leading zero)
    cid = p["cid"]
    if not cid.isdigit() or len(cid) != 3 or cid[0] == "0":
        continue

    # If all checks passed → passport is valid
    valid_passports.append(passport)
    valid_count += 1


# Print how many are valid
print("There are", valid_count, "valid passports")

# Write valid passports to a new file
with open("valid_passports2.txt", "w") as outfile:
    for i in range(len(valid_passports)):
        outfile.write(valid_passports[i])

        # Write a blank line between passports (but not after last one)
        if i != len(valid_passports) - 1:
            outfile.write("\n\n")
