# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kingston Alexander
#               Maya Ayoubi
#               Divyamaukthika Challa
#               Gia Huynh
# Section:      509
# Assignment:   ASCII Clock Program - Individual Part
# Date:         24 October 2025

# --------------------------------------------
# SECTION 5: Main Function
# Assigned to: Team Member 5 (or integrator)
# --------------------------------------------
def main():
    """
    Main driver function:
    1. Get inputs
    2. Convert time if needed
    3. Create ASCII dictionary
    4. Display final ASCII art time
    """
    time_str, clock_type, preferred_char = get_user_input()
    if clock_type == 12:
        converted_time, suffix = convert_to_12hr_format(time_str, clock_type)
    else:
        converted_time, suffix = time_str, ""
    ascii_dict = create_ascii_digits(preferred_char)
    display_ascii_time(converted_time, ascii_dict, suffix)
