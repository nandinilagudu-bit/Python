"""
Python Problem-Solving Practice: Dictionaries and Algorithms
-------------------------------------------------------------
A third beginner-friendly practice file.

How to run:
    python dictionary_algorithm_practice.py

Topics: number guessing, linear search, list statistics, word frequency,
        and checking whether a number is an Armstrong number.
"""


def number_guessing_game():
    """Let the user guess a secret number with helpful hints."""
    secret_number = 17
    attempts = 0
    print("Guess the secret number between 1 and 50.")

    while True:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low. Try a larger number.")
        elif guess > secret_number:
            print("Too high. Try a smaller number.")
        else:
            print(f"Correct! You guessed it in {attempts} attempt(s).")
            break


def linear_search():
    """Find the position of a target value in a list."""
    numbers = [int(item) for item in input(
        "Enter integers separated by spaces: "
    ).split()]
    target = int(input("Number to search for: "))

    # Check each element in order until the target is found.
    for index, value in enumerate(numbers):
        if value == target:
            print(f"Found {target} at index {index} (position {index + 1}).")
            return

    print("That number is not in the list.")


def list_statistics():
    """Display the count, total, average, minimum, and maximum."""
    numbers = [float(item) for item in input(
        "Enter numbers separated by spaces: "
    ).split()]

    if not numbers:
        print("Please enter at least one number.")
        return

    print("Count:", len(numbers))
    print("Sum:", sum(numbers))
    print("Average:", sum(numbers) / len(numbers))
    print("Smallest:", min(numbers))
    print("Largest:", max(numbers))


def word_frequency():
    """Count how many times each word appears in a sentence."""
    sentence = input("Enter a sentence: ").lower()
    words = sentence.split()
    counts = {}

    for word in words:
        # A dictionary stores each word and its count.
        counts[word] = counts.get(word, 0) + 1

    if not counts:
        print("No words were entered.")
        return

    for word, count in sorted(counts.items()):
        print(f"{word}: {count}")


def is_armstrong_number():
    """Check whether a number equals the sum of its digits to a power."""
    number = int(input("Enter a non-negative integer: "))

    if number < 0:
        print("Please enter a non-negative integer.")
        return

    digits = str(number)
    power = len(digits)

    # Example: 153 = 1**3 + 5**3 + 3**3 = 153.
    total = sum(int(digit) ** power for digit in digits)

    if total == number:
        print(number, "is an Armstrong number.")
    else:
        print(number, "is not an Armstrong number.")


def main():
    """Show the exercise menu until the user chooses to exit."""
    exercises = {
        "1": ("Number guessing game", number_guessing_game),
        "2": ("Linear search", linear_search),
        "3": ("List statistics", list_statistics),
        "4": ("Word frequency counter", word_frequency),
        "5": ("Armstrong number checker", is_armstrong_number),
    }

    while True:
        print("\n=== DICTIONARIES AND ALGORITHMS ===")
        for key, (description, _) in exercises.items():
            print(f"{key}. {description}")
        print("0. Exit")

        choice = input("Choose an exercise: ").strip()

        if choice == "0":
            print("Well done. Keep practising!")
            break

        if choice not in exercises:
            print("Invalid choice. Please select a listed option.")
            continue

        try:
            exercises[choice][1]()
        except ValueError:
            print("Please enter a valid number and try again.")


if __name__ == "__main__":
    main()
