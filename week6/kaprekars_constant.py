# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   7.20 Lab: Kaprekar's Constant
# Date:         11 October 2025

# Get four-digit integer from user
num_str = input("Enter a four-digit integer: ")
num = int(num_str)


def kaprekar_step(n):
    s = f"{n:04d}"
    asc = "".join(sorted(s))
    desc = "".join(sorted(s, reverse=True))
    return int(desc) - int(asc)


if len(set(f"{num:04d}")) == 1:
    next_num = kaprekar_step(num)
    print(f"{num} > {next_num}")
    print(f"{num} reaches {next_num} via Kaprekar's routine in 1 iterations")
else:
    original = num_str.lstrip("0") or "0"
    sequence = [original]
    iterations = 0
    while num != 6174:
        num = kaprekar_step(num)
        if num == 0:
            sequence.append("0")
            break
        sequence.append(str(int(num)))  # strip leading zeros for display
        iterations += 1
    print(" > ".join(sequence))
    print(
        f"{sequence[0]} reaches {sequence[-1]} via Kaprekar's routine in {iterations} iterations")
