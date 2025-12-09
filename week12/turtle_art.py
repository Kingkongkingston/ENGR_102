import turtle as t
import math

# Set up the turtle screen once
t.setup(800, 800)
t.speed(0)  # Fastest drawing speed
t.hideturtle()  # Hide the turtle icon
t.colormode(255)  # Use RGB for colors (optional, but good practice)


def get_iterations(angle_sum):
    """
    Calculates the smallest number of iterations (n) required for the total 
    rotation (n * angle_sum) to be a multiple of 360 degrees, 
    so the turtle returns to its initial direction.

    This function relies on the fact that the total angle turned must be a 
    multiple of 360 degrees for the turtle to return to its starting direction.
    The smallest such number 'n' is found by simplifying the fraction 
    (360 / angle_sum) to its lowest terms, where the numerator is 'n'.
    """
    if angle_sum == 0:
        return 1  # Or handle as an error/special case, but 1 iteration is a return for 0 angle

    # Calculate the Greatest Common Divisor (GCD) of the total angle (angle_sum)
    # and a full circle (360)
    # The absolute value is used because angle_sum can be negative.
    gcd = math.gcd(int(round(angle_sum)), 360)

    # The number of iterations 'n' is 360 divided by the GCD.
    # This gives the smallest integer 'n' such that (n * angle_sum) is a multiple of 360.
    return 360 // gcd


def parta(turn_angle):
    """
    Takes a turn angle, determines the smallest number of iterations 
    needed for the turtle to return to its starting point, and plots the figure. 
    The distance moved is fixed at 300 units per step.
    """
    # Use 300 as the distance, based on the example in the prompt [cite: 14]
    distance = 300

    # The total angle for a single iteration is just the turn_angle parameter.
    num_iterations = get_iterations(turn_angle)

    print(f"\n--- Part A: Angle {turn_angle} degrees ---")
    print(f"Iterations needed: {num_iterations}")

    # Reset turtle state for new drawing (position, heading, color)
    t.reset()
    t.speed(0)
    t.hideturtle()

    t.dot(10, "red")  # Mark the starting point [cite: 14]

    for _ in range(num_iterations):
        t.left(turn_angle)  # Turn the specified angle
        t.forward(distance)  # Move forward a fixed distance

    t.update()  # Ensure all drawing is complete


def partb(sequence):
    """
    Takes a sequence of '0's and '1's. '0' is a 30-degree turn, '1' is a 
    -114-degree turn. Determines the smallest number of iterations needed for 
    the turtle to return to its starting point and plots the figure.
    The distance moved is fixed at 300 units per step.
    """
    # Based on the prompt: 0: 30 degrees, 1: -114 degrees [cite: 22]
    angle_zero = 30
    angle_one = -114
    distance = 300

    # Calculate the total turn angle for one full iteration of the sequence
    total_angle_per_sequence = 0
    for char in sequence:
        if char == '0':
            total_angle_per_sequence += angle_zero
        elif char == '1':
            total_angle_per_sequence += angle_one

    num_iterations = get_iterations(total_angle_per_sequence)

    print(f"\n--- Part B: Sequence '{sequence}' ---")
    print(f"Angle per sequence: {total_angle_per_sequence} degrees")
    print(f"Iterations needed: {num_iterations}")

    # Reset turtle state for new drawing (position, heading, color)
    t.reset()
    t.speed(0)
    t.hideturtle()

    t.dot(10, "red")  # Mark the starting point

    for _ in range(num_iterations):
        for char in sequence:
            if char == '0':
                t.left(angle_zero)
                t.forward(distance)
            elif char == '1':
                t.left(angle_one)
                t.forward(distance)

    t.update()  # Ensure all drawing is complete


def partc(sequence, angle_zero, angle_one, distance_scale=1.0):
    """
    Plots a figure based on a sequence of '0's and '1's with custom turn 
    angles for '0' and '1'.

    distance_scale is an optional parameter to adjust the step size 
    (e.g., for very long sequences like the 50 ones spiral).
    """
    distance = 50 * distance_scale  # Adjust base distance as needed

    print(f"\n--- Part C: Custom Sequence ---")
    print(
        f"Sequence length: {len(sequence)}. Angle '0': {angle_zero}. Angle '1': {angle_one}.")

    # Reset turtle state for new drawing (position, heading, color)
    t.reset()
    t.speed(0)
    t.hideturtle()

    t.dot(10, "red")  # Mark the starting point

    # Initialize the distance for the first '1' in the spiral sequence
    current_distance = distance

    for char in sequence:
        if char == '0':
            t.left(angle_zero)
            t.forward(current_distance)
        elif char == '1':
            t.left(angle_one)
            t.forward(current_distance)

            # The '1' in the spiral sequence also marks the increase in distance
            # for the subsequent moves to create the spiral effect.
            # *Note: The prompt describes the spiral by the number of zeros
            # *following each one. The simplest implementation for a square spiral
            # *is to increase the distance after each '1' (turn), which is what
            # *the visual suggests[cite: 31, 32, 33].

            # A simpler approach for the given description "1 followed by an
            # increasing number of zeros" is to let the loop run through the
            # full sequence *string* and just increase distance after each '1'
            # or handle the sequence generation externally.

            # Since the sequence is passed as a string, let's assume the
            # sequence generation (e.g., '1101001000...') is handled before
            # calling this function, and the distance scaling should be
            # handled inside here to produce the increasing square spiral.

            # For the square spiral (90 degree turn) each segment must increase
            # in length. Since '1' corresponds to the 90-degree turn[cite: 33],
            # we can use the following logic to grow the distance:

            if angle_one == 90 and angle_zero == 0:
                # Increase distance for the next segment (square spiral)
                current_distance += distance

            # For non-spiral shapes (e.g., 30, 150, 108 degree turns),
            # a fixed distance is generally used, so we'll revert to the base distance.
            else:
                current_distance = distance

    t.update()  # Ensure all drawing is complete


def generate_spiral_sequence(num_ones):
    """
    Generates the spiral sequence '1101001000...' [cite: 31]
    The first '1' is followed by 0 zeros, the second '1' by 1 zero, etc.
    """
    sequence = ""
    for i in range(num_ones):
        sequence += '1'
        # i is the number of zeros following the (i+1)th '1'
        sequence += '0' * i
    return sequence

# --- Main Execution Block --- [cite: 37]


# Create sequences for Part C
seq1 = generate_spiral_sequence(20)  # Sequence with 20 ones [cite: 40]
seq2 = generate_spiral_sequence(50)  # Sequence with 50 ones [cite: 41]

# Part A calls [cite: 39]
parta(160)
# Pause program [cite: 48, 51]
input("Press Enter to continue to the next plot...")
t.reset()  # Clear the window [cite: 49, 52]

parta(141)
input("Press Enter to continue to the next plot...")
t.reset()

# Part B calls [cite: 40, 53, 54]
partb("01001")
input("Press Enter to continue to the next plot...")
t.reset()

partb("01001011")
input("Press Enter to continue to the next plot...")
t.reset()

# Part C calls [cite: 40, 41, 57, 58, 60, 63, 64]
# For the square spiral (90 deg), a smaller scale is needed to fit 20 segments
partc(seq1, 0, 90, distance_scale=0.1)
input("Press Enter to continue to the next plot...")
t.reset()

partc(seq1, 0, 30, distance_scale=0.2)
input("Press Enter to continue to the next plot...")
t.reset()

# For the 50-ones sequence, an even smaller scale is needed
partc(seq2, 0, 150, distance_scale=0.04)
input("Press Enter to continue to the next plot...")
t.reset()

partc(seq2, 5, 108, distance_scale=0.04)
input("Press Enter to close the window...")
t.reset()

t.done()  # Prevents the window from closing immediately [cite: 65, 66]
