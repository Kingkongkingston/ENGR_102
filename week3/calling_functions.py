import math


def result(shape, side, area):
    print(f"A shape with side length {side:.3f} has an area of {area:.3f}")


side = float(input("Enter side length: "))

triangle_area = (math.sqrt(3) / 4) * side * side
square_area = side * side
pentagon_area = 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side * side
hexagon_area = (3 * math.sqrt(3) / 2) * side * side
dodegon_area = 3 * (2 + math.sqrt(3)) * (side) ** 2

result("triangle", side, triangle_area)
result("square", side, square_area)
result("pentagon", side, pentagon_area)
result("hexagon", side, hexagon_area)
result("dodegon", side, dodegon_area)
