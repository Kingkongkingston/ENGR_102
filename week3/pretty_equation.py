# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kingston Alexander
#               Maya Ayoubi
#               Divyamaukthika Challa
#               Gia Huynh
# Section:      509
# Assignment:   4.17 Lab - Pretty Equation
# Date:         19/09/2025

# Get coefficient inputs from user
A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))

equation = "The quadratic equation is "

if A != 0:
    if A == 1:
        equation += "x^2"
    elif A == -1:
        equation += "- x^2"
    else:
        equation += f"{A}x^2"

if B != 0:
    if B > 0:
        if A != 0:
            equation += " + "
        else:
            equation += ""
        if B == 1:
            equation += "x"
        else:
            equation += f"{B}x"
    else:
        if A != 0:
            equation += " - "
        else:
            equation += "- "
        if B == -1:
            equation += "x"
        else:
            equation += f"{-B}x"

if C != 0:
    if C > 0:
        if A != 0 or B != 0:
            equation += " + "
        equation += f"{C}"
    else:
        if A != 0 or B != 0:
            equation += " - "
        else:
            equation += "-"
        equation += f"{-C}"

equation += " = 0"
print(equation)
