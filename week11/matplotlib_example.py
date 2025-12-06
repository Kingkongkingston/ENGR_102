# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Divyamaukthika Challa
#       Maya Ayoubi
#       Gia Huynh
#       Kingston Alexander
# Section: 509
# Assignment: Lab: Topic 12 (matplotlib – team)
# Date: 17 November 2025
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

import numpy as np
import matplotlib.pyplot as plt


# create x values
x = np.linspace(-2.0, 2.0, 200)

# compute y values
f1 = 2
f2 = 6
y1 = (1 / (4 * f1)) * x**2
y2 = (1 / (4 * f2)) * x**2

plt.figure()
plt.plot(x, y1, color='red', linewidth=2.0, label='f = 2')
plt.plot(x, y2, color='blue', linewidth=6.0, label='f = 6')

plt.title("Parabola plots with varying focal length")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# plot 25 points for polynomial

x2 = np.linspace(-4.0, 4.0, 25)
y2 = 2 * x2**3 + 3 * x2**2 - 11 * x2 - 6

plt.figure()
plt.plot(x2, y2, 'y*', markersize=6, label='Cubic Polynomial')

plt.title("Plot of cubic polynomial")
plt.xlabel("x values")
plt.ylabel("y values")
plt.grid(True)
plt.show()


# subplots for sinx and cosx
x3 = np.arange(-2*np.pi, 2*np.pi, 0.01)
y_sin = np.sin(x3)
y_cos = np.cos(x3)
plt.figure()
plt.title("Plot of cos(x) and sin(x)")

plt.axis("off")

# Subplot for cosx
plt.subplot(2, 1, 1)
plt.plot(x3, y_cos, 'r-', linewidth=2, label='cos(x)')
plt.xlabel("x")
plt.ylabel("x=cos(x)")
plt.grid(True)
plt.legend()


# Subplot for sinx
plt.subplot(2, 1, 2)
plt.plot(x3, y_sin, linewidth=2, label='sin(x)', color=(0.5, 0.5, 0.5))
plt.xlabel("x")
plt.ylabel("y=sin(x)")
plt.grid(True)
plt.legend()
