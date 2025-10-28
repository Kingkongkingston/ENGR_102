# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Divyamaukthika Challa
#               Maya Ayoubi
#               Gia Huynh
#               Kingston Alexander
# Section:      509
# Assignment:   Lab: Team lab 9
# Date:         27 October 2025
# ---------------------------------------------------------

# print puzzle
def print_puzzle(puzzle):
    """Print puzzle as a long division problem."""
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")
    print()

# check_user_guess


def get_valid_letters(puzzle):
    """Return a string of 10 unique letters from the puzzle."""
    letters = [ch.upper() for ch in puzzle if ch.isalpha()]
    unique_letters = []
    for ch in letters:
        if ch not in unique_letters:
            unique_letters.append(ch)
        if len(unique_letters) == 10:
            break
    return ''.join(unique_letters)

# check length of guess


def is_valid_guess(valid_letters, guess):
    """Return True if guess has exactly 10 unique letters from valid_letters."""
    guess = guess.upper().strip()
    if len(guess) != 10 or len(set(guess)) != 10:
        return False
    for ch in guess:
        if ch not in valid_letters:
            return False
    return True

# check user guess


def check_user_guess(dividend, quotient, divisor, remainder):
    """Return True if Dividend = Quotient * Divisor + Remainder."""
    return dividend == quotient * divisor + remainder

# convert word to integer


def make_number(word, guess):
    """Convert a word to an integer based on user's guess mapping."""
    mapping = {ch: str(i) for i, ch in enumerate(guess)}
    return int(''.join(mapping[ch] for ch in word))

# make tuples


def make_numbers(puzzle, guess):
    """Return a tuple of integers (dividend, quotient, divisor, remainder)."""
    left, right = puzzle.split('|')
    left_parts = [x.strip() for x in left.split(',') if x.strip()]
    right_parts = [x.strip() for x in right.split(',') if x.strip()]

    quotient_word = left_parts[0]
    divisor_word = left_parts[1]
    dividend_word = right_parts[0]
    remainder_word = right_parts[-1]

    return (
        make_number(dividend_word, guess),
        make_number(quotient_word, guess),
        make_number(divisor_word, guess),
        make_number(remainder_word, guess)
    )

# main


def main():
    puzzle = input('Enter a word arithmetic puzzle: \n')
    print_puzzle(puzzle)

    valid_letters = get_valid_letters(puzzle)
    guess = input('Enter your guess, for example ABCDEFGHIJ: ').strip().upper()

    if not is_valid_guess(valid_letters, guess):
        print('Your guess should contain exactly 10 unique letters used in the puzzle.')
        return

    dividend, quotient, divisor, remainder = make_numbers(puzzle, guess)

    if check_user_guess(dividend, quotient, divisor, remainder):
        print('Good job!')
    else:
        print('Try again!')


# Final output
if __name__ == '__main__':
    main()
