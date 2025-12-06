# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   Topic 12 Individual Lab: Pretty Plot
# Date:         25 Nov 2025

import numpy as np
import matplotlib.pyplot as plt


def main():
    # Starting point
    v = np.array([0, 1])

    # Given matrix
    M = np.array([
        [1.02, 0.095],
        [-0.095, 1.02]
    ])

    # Store points
    xs = []
    ys = []

    # Multiply 250 times
    for _ in range(250):
        v = M @ v
        xs.append(v[0])
        ys.append(v[1])

    # Plot
    plt.figure()
    plt.plot(xs, ys, marker='.', linestyle='none')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Repeated matrix multiplication plot")
    plt.show()


if __name__ == "__main__":
    main()
