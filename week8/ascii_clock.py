# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Maya Ayoubi
#               Divya Challa
#               Gia Huynh
#               Kingston Alexander
# Section:      509
# Assignment:   Team Lab 4
# Date:         24 October 2025
#################################################################################

# -----------------------------------------
# SECTION 1: User Input & Validation
# --------------------------------------------

def get_user_input():

    # Prompts user for:
    #  - Time (in HH:MM)
    #  - Clock type (12 or 24)
    #  - Preferred character
    # Validates input format and allowed characters.
    # Returns: (time_str, clock_type, preferred_char)

    time_str = input("Enter the time: ").strip()
    clock_type = int(input("Choose the clock type (12 or 24): ").strip())
    preferred_char = input("Enter your preferred character: ").strip()
    preferred_char = validate_character(preferred_char)
    return time_str, clock_type, preferred_char

# validate the character


def validate_character(char):

    # Ensures the preferred character is allowed.
    # Only permits: abcdeghkmnopqrsuvwxyz@$&*=
    # If not allowed, ask again.
    # Returns: valid character

    allowed_chars = "abcdeghkmnopqrsuvwxyz@$&*="
    while True:
        if char == "" or char in allowed_chars:
            return char
        else:
            char = input("Character not permitted! Try again: ").strip()


# --------------------------------------------
# SECTION 2: Time Conversion
# --------------------------------------------

def convert_to_12hr_format(time_str, clock_type):

    # Converts 24-hour time to 12-hour if user selected 12-hour clock.
    # Adds AM or PM suffix if applicable.
    # Returns: (converted_time, suffix)

    hour, minute = time_str.split(":")
    hour = int(hour)
    suffix = ""

    if clock_type == 12:
        if hour == 0:
            hour = 12
            suffix = "AM"
        elif hour == 12:
            suffix = "PM"
        elif hour > 12:
            hour -= 12
            suffix = "PM"
        else:
            suffix = "AM"
        converted_time = f"{hour}:{minute}"
    else:
        converted_time = time_str

    return converted_time, suffix


# --------------------------------------------
# SECTION 3: ASCII Dictionary
# --------------------------------------------

def create_ascii_digits(preferred_char):

    # Builds and returns a dictionary mapping each digit (0-9), colon (:),
    # and letters A, M, P (for AM/PM) to their ASCII art patterns.
    # Use preferred_char for drawing the digits.

    font_variables = {
        "0": ["111", "101", "101", "101", "111"],
        "1": ["010", "110", "010", "010", "111"],
        "2": ["111", "001", "111", "100", "111"],
        "3": ["111", "001", "111", "001", "111"],
        "4": ["101", "101", "111", "001", "001"],
        "5": ["111", "100", "111", "001", "111"],
        "6": ["111", "100", "111", "101", "111"],
        "7": ["111", "001", "001", "001", "001"],
        "8": ["111", "101", "111", "101", "111"],
        "9": ["111", "101", "111", "001", "111"],
        ":": ["0", "1", "0", "1", "0"],
        "A": ["010", "101", "111", "101", "101"],
        "P": ["111", "101", "111", "100", "100"],
        "M": ["10001", "11011", "10101", "10001", "10001"],
    }

    ascii_dict = {}

    for char, pattern in font_variables.items():
        lines = []
        for row in pattern:
            line = ""
            for bit in row:
                if bit == "1":
                    if char in [":", "A", "M", "P"]:
                        line += char
                    elif preferred_char == "":
                        line += char
                    else:
                        line += preferred_char
                else:
                    line += " "
            lines.append(line)
        ascii_dict[char] = lines

    return ascii_dict


# --------------------------------------------
# SECTION 4: Display Function
# --------------------------------------------

def display_ascii_time(time_str, ascii_dict, suffix=""):

    # Uses the ascii_dict to print the time in ASCII art line by line.
    # Prints suffix (AM/PM) when applicable.

    full_str = time_str + suffix
    rows = ["", "", "", "", ""]

    for ch in full_str:
        if ch not in ascii_dict:
            continue
        for r in range(5):
            if rows[r] != "":
                rows[r] += " "
            rows[r] += ascii_dict[ch][r]

    print()
    for line in rows:
        print(line.rstrip())


# --------------------------------------------
# SECTION 5: Main Function
# --------------------------------------------

def main():

    # Main driver function:
    # 1. Get inputs
    # 2. Convert time if needed
    # 3. Create ASCII dictionary
    # 4. Display final ASCII art time

    time_str, clock_type, preferred_char = get_user_input()
    converted_time, suffix = convert_to_12hr_format(time_str, clock_type)
    ascii_dict = create_ascii_digits(preferred_char)
    display_ascii_time(converted_time, ascii_dict, suffix)


# --------------------------------------------
# SECTION 6: Program Execution Guard
# --------------------------------------------
if __name__ == "__main__":
    main()
