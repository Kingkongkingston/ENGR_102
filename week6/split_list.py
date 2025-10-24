# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   7.19 Lab: Split List
# Date:         11 October 2025

# Get numbers from user, seperate into list, convert to integers
nums = input("Enter numbers: ").split()
nums = [int(n) for n in nums]

found = False
for i in range(1, len(nums)):
    left_sum = 0
    for j in range(i):
        left_sum += nums[j]
    right_sum = 0
    for k in range(i, len(nums)):
        right_sum += nums[k]
    if left_sum == right_sum:
        print(f"Left: {nums[:i]}")
        print(f"Right: {nums[i:]}")
        print(f"Both sum to {left_sum}")
        found = True
        break

if not found:
    print("Cannot split evenly")
