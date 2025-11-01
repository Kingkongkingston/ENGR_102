# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   9.20 Lab: Small Functions
# Date:         31 October 2025

import math


def parta(numbers):
    # Check to see if list empty
    if not numbers:
        raise ValueError("List cannot be empty.")
    nums = sorted(numbers)
    n = len(nums)
    mid = n // 2
    if n % 2 == 1:
        median = nums[mid]
    else:
        median = (nums[mid - 1] + nums[mid]) / 2
    return min(nums), median, max(nums)


def partb(times, distances):
    # Lists must be same length
    if len(times) != len(distances):
        raise ValueError("Lists must be the same length.")
    if len(times) < 2:
        return []
    velocities = []
    for i in range(len(times) - 1):
        dt = times[i + 1] - times[i]
        if dt == 0:
            raise ValueError("Time values must be increasing.")
        velocities.append((distances[i + 1] - distances[i]) / dt)
    return velocities


def partc(numbers):
    # Check to see if list has at least 2 numbers
    seen = set()
    for num in numbers:
        target = 2029 - num
        if target in seen:
            return num * target
        seen.add(num)
    return False


def partd(n):
    if n <= 0:
        return False

    # Try sequences of length k (at least 2)
    for k in range(2, n // 2 + 1):
        # average of sequence = n / k
        # even numbers are spaced by 2
        # first term a = avg - (k - 1)
        a = (n / k) - (k - 1)
        if a % 2 == 0 and a > 0:
            seq = [int(a + 2 * i) for i in range(k)]
            if sum(seq) == n:
                return seq
    return False


def parte(r_sphere, r_hole):
    # Check that hole radius is smaller than sphere radius
    if r_hole >= r_sphere:
        raise ValueError("Hole radius must be smaller than sphere radius.")
    h = 2 * math.sqrt(r_sphere**2 - r_hole**2)
    volume = (math.pi / 6) * h**3
    return volume


def partf(border_char, name, company, email):
    # Create framed business card
    entries = [name, company, email]
    longest = max(len(e) for e in entries)
    inner_width = longest + 4  # 2 spaces padding on each side
    border = border_char * (inner_width + 2)
    lines = [border]
    for e in entries:
        padding_right = inner_width - len(e) - 2
        lines.append(f"{border_char}  {e}{' ' * padding_right}  {border_char}")
    lines.append(border)
    return "\n".join(lines)


def partg(x, tolerance):
    # Check that x is between -1 and 1
    if not (-1 < x < 1):
        raise ValueError("x must be between -1 and 1 (exclusive)")
    n = 1
    total = 0.0
    while True:
        term = (2 / (2 * n - 1)) * math.pow(x, 2 * n - 1)
        if abs(term) < tolerance:
            break
        total += term
        n += 1
    return total
