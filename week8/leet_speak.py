# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   8.18 LAB: Leet speak
# Date:         24 October 2025

# Create a dictionary for letter-to-number conversions
leet_dict = {
    'a': '4',
    'e': '3',
    'o': '0',
    's': '5',
    't': '7'
}

# Get input from user
text = input("Enter some text: ")

# Convert each character using the dictionary
leet_text = ""
for char in text:
    # If the lowercase version of the character is in the dictionary, replace it
    if char.lower() in leet_dict:
        leet_char = leet_dict[char.lower()]
        leet_text += leet_char
    else:
        leet_text += char

print(f'In leet speak, "{text}" is:')
print(leet_text)
