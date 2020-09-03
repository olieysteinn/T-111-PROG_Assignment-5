
# Don't change these lines
number = int(input("Find the square root of integer: "))
guess = int(input("Initial guess: "))
tolerance = float(input("What tolerance: "))

# Implement the Babylonian square root algorithm
previous_guess = 0
count = 0
while abs(guess - previous_guess) > tolerance:
    previous_guess = guess
    guess = (guess + (number / guess)) / 2
    count += 1

# Don't change these lines
print("Square root of", number, "is", round(guess, 4))
print("Took", count, "reps to get it to tolerance")
